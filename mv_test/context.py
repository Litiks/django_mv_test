from blog.models import Post

def mv_test(request):
    return {
        'mv_profile': request.mv_profile,
    }
    
#eof
