/*
*	Comments
*	A reusable JS class for providing AJAX comments submission and loading
*	
*	Requires jQuery library (http://www.jquery.com) with 
*   jQuery.Class plug-in (http://github.com/taylanpince/jquery-class)
*	
*	Taylan Pince (taylanpince at gmail dot com) - March 19, 2009
*/

$.namespace("core.Comments")

core.Comments = $.Class.extend({
    
    form_selector : "",
    list_selector : "",
    counter_selector : null,
    top_selector : null,
    total_comments : 0,
    captcha_url : null,
    
    error_template : '<p class="%(type)">%(message)</p>',
    
    comment_posted_copy : "Your comment has been posted.",
    comment_failed_copy : "There was an error with your request, please try again.",
    
    render_comment : function(data) {
        $(this.list_selector).find("li:last-child").removeClass("last-child");
        $("<li></li>").appendTo(this.list_selector).append(data).addClass("last-child");
        
        core.scroll_to(this.list_selector + " li:last-child");
        
        if (this.counter_selector && this.total_comments > 0) {
            $(this.counter_selector).text(this.total_comments);
        }
        
        $(this.form_selector).find("li.stand-by").removeClass("stand-by");
        $(this.form_selector).prepend(core.render_template(this.error_template, {
            "message" : this.comment_posted_copy,
            "type" : "success"
        }));
        
        this.reload_captcha();
    },
    
    parse_comment_form : function(data) {
        if (data.errors) {
            $(this.form_selector).find("li.stand-by").removeClass("stand-by");
            
	        for (error in data.errors) {
	            if (error == "__all__") {
	                for (e in data.errors[error]) {
        	            $(this.form_selector).prepend(core.render_template(this.error_template, {
        	                "message" : data.errors[error][e],
        	                "type" : "error"
        	            }));
	                }
	            } else {
    	            $(this.form_selector).find("[name*=" + error + "]").parent().prepend(core.render_template(this.error_template, {
    	                "message" : data.errors[error],
    	                "type" : "error"
    	            }));
	            }
	        }
	        
	        if (!("captcha" in data.errors)) {
	            this.reload_captcha();
	        }
	    } else {
	        this.total_comments = data.total;
	        
	        if (data.comment) {
                $.ajax({
                    url : data.comment,
                    type : "GET",
                    processData : false,
                    dataType : "html",
                    success : this.render_comment.bind(this)
                });
	        }
	        
	        $(this.form_selector + "-body").val("");
	    }
	            
	    $(this.form_selector).find("input[type=submit], input[type=image]").attr("disabled", false);
    },
    
    reload_captcha : function() {
        if (this.captcha_url) {
            $(this.form_selector).find("li.captcha").load(this.captcha_url);
        }
    },
    
    error_comment_form : function() {
        $(this.form_selector).prepend(core.render_template(this.error_template, {
            "message" : this.comment_failed_copy,
            "type" : "error"
        }));
        
        $(this.form_selector).find("input[type=submit], input[type=image]").attr("disabled", false);
    },
    
    submit_comment_form : function() {
        $(this.form_selector).find("p.error, p.success").fadeOut("slow");
	    $(this.form_selector).find("input[type=submit], input[type=image]").attr("disabled", true);
        $(this.form_selector).find("li.submit").addClass("stand-by");
	    
        $.ajax({
            url : $(this.form_selector).attr("action"),
            type : "POST",
            processData : false,
            data : $(this.form_selector).serialize(),
            dataType : "json",
            contentType : "application/json",
            success : this.parse_comment_form.bind(this),
            error : this.error_comment_form.bind(this)
        });
        
        if (this.top_selector) {
            core.scroll_to(this.top_selector);
        } else {
            core.scroll_to(this.form_selector);
        }
        
        return false;
    },
    
    init : function(form_selector, list_selector, options) {
        this.form_selector = form_selector;
        this.list_selector = list_selector;
        
        if (options) {
            for (opt in options) {
                this[opt] = options[opt];
            }
        }
        
        $(this.form_selector).submit(this.submit_comment_form.bind(this));
    }
    
});
