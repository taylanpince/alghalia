def production():
    "Set the variables for the production environment"
    set(fab_hosts=["69.42.54.85"])
    set(fab_port=7777)
    set(fab_user="taylan")
    set(remote_dir="/home/taylan/sites/alghalia")


def deploy(hash="HEAD"):
    "Deploy the application by packaging a specific hash or tag from the git repo"
    # Make sure that the required variables are here
    require("fab_hosts", provided_by=[production])
    require("fab_user", provided_by=[production])
    require("remote_dir", provided_by=[production])
    
    # Set the commit hash (HEAD if not given)
    set(hash=hash)
    
    # Create a temporary local directory, export the given commit using git archive
    local("mkdir ../tmp")
    local("cd ..; git archive --format=tar --prefix=deploy/ $(hash) conf build/libs build/alghalia build/src | gzip > tmp/archive.tar.gz")
    
    # Untar the archive to minify js files
    local("cd ../tmp; tar -xzf archive.tar.gz; rm -f archive.tar.gz")
    local("python /usr/local/lib/yuicompressor/bin/jsminify.py --dir=../tmp/deploy/build/alghalia/media/js")
    
    # Tarball the release again
    local("cd ../tmp; tar -cf archive.tar deploy; gzip archive.tar")
    
    # Upload the archive to the server
    put("../tmp/archive.tar.gz", "$(remote_dir)/archive.tar.gz")
    
    # Extract the files from the archive, remove the file
    run("cd $(remote_dir); /usr/bin/tar -xzf archive.tar.gz; rm -f archive.tar.gz")
    
    # Move directories out of the build folder and get rid of it
    run("mv $(remote_dir)/deploy/build/* $(remote_dir)/deploy/")
    run("rm -rf $(remote_dir)/deploy/build")
    
    # Create a symlink for the Django settings file
    run("cd $(remote_dir)/deploy/alghalia; ln -s ../conf/settings.py settings_local.py")
    
    # Move the uploaded files directory from the active version to the new version, create a symlink
    run("mv $(remote_dir)/app/files $(remote_dir)/deploy/files")
    run("cd $(remote_dir)/deploy/alghalia/media; ln -s ../../files uploads")
    
    # Remove the active version of the app and move the new one in its place
    run("rm -rf $(remote_dir)/app")
    run("mv $(remote_dir)/deploy $(remote_dir)/app")

    # Sync the database and apply migrations
    run("cd $(remote_dir)/app/alghalia/; export PYTHONPATH=../libs; ./manage.py syncdb; ./manage.py migrate")

    # Restart Apache
    sudo("/usr/local/etc/rc.d/apache22 restart")
    
    # Remove the temporary local directory
    local("rm -rf ../tmp")
