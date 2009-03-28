/*
*	Core
*	A core JS class that contains utility methods
*	
*	Requires jQuery library (http://www.jquery.com),
*   jQuery.Class plug-in (http://github.com/taylanpince/jquery-class)
*	
*	Taylan Pince (taylanpince at gmail dot com) - February 18, 2009
*/

$.extend($.namespace("core"), {

    init_markers : function(container) {
    	$(container).find("li:last-child").addClass("last-child");
    	$(container).find("li:first-child").addClass("first-child");
    
    	$(container).find("input[type=text]").addClass("text");
    	$(container).find("input[type=submit], input[type=button]").addClass("submit");
    	$(container).find("input[type=password]").addClass("text");
    	$(container).find("input[type=file]").addClass("file");
    	$(container).find("input[type=radio]").addClass("radio");
    	$(container).find("input[type=checkbox]").addClass("checkbox");
    	$(container).find("input[type=image]").addClass("image");
    
    	$(container).find("hr").wrap('<div class="hr"></div>').each(function() {
    	    $(this).parent().addClass($(this).attr("class"));
    	});
    },

    init_html : function() {
    	$("html").addClass("has-js");
    },

    render_template : function(template, values) {
        for (val in values) {
            var re = new RegExp("%\\(" + val + "\\)", "g");
        
            template = template.replace(re, values[val]);
        }
    
        return template;
    },

    scroll_to : function(obj) {
        $("html, body").animate({
            "scrollTop" : parseInt($(obj).offset().top)
        }, 250);
    },

    parse_query : function(url) {
        var params = {};
    
        if (url.indexOf("#") > -1) {
            var queries = url.substring(url.indexOf("#") + 1).split("&");
        } else if (url.indexOf("?") > -1) {
            var queries = url.substring(url.indexOf("?") + 1).split("&");
        } else {
            return params;
        }
    
        for (var i = 0; i < queries.length; i++) {
            var pair = queries[i].split("=");
        
            if (pair[0] != "") {
                params[pair[0]] = pair[1];
            }
        }
    
        return params;
    },

    update_query : function(params) {
        var query_params = this.parse_query(window.location.toString());
    
        for (var key in params) {
            query_params[key] = params[key];
        }
    
        var params = [];
    
        for (var key in query_params) {
            if (query_params[key] != "" && key != ".") {
                params.push(key + "=" + query_params[key]);
            }
        }
    
        if (params.length > 0) {
            window.location.hash = "#" + params.join("&");
        } else {
            if (window.location.hash != "") {
                window.location.hash = "#.";
            }
        }
    },

    build_url : function(url, params) {
        var base_url = url.substring(0, url.indexOf("?"));
        var query = [];
        
        for (var key in params) {
            query.push(key + "=" + params[key]);
        }
        
        return base_url + "?" + query.join("&");
    },
    
    init : function() {
        this.init_html();
        this.init_markers("body");
    }

});

$(function() {
    core.init();
});
