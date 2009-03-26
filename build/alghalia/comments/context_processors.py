def comment_cookies(request):
    """
    A context processor that adds comment cookie data into the context
    """
    return {
        "COMMENT_AUTHOR": request.COOKIES.get("comment_author", None),
        "COMMENT_EMAIL": request.COOKIES.get("comment_email", None),
    }
