from django.shortcuts import render
from feed.models import Post

# Main feed view
def feed(request):
    
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    
    return render(request, 'feed.html', context)


# View to inspect the details of a post and possibly chat later
def post_details(request, primary_key):

    post = Post.objects.get(pk=primary_key)
    context = {
        'post': post
    }
    
    return render(request, 'post_details.html', context)
