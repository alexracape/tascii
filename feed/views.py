from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from .forms import NewUserForm
from feed.models import Post

# Main feed view
def feed(request):
    
    query = request.GET.get('query')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(start_loc__icontains=query) | Q(end_loc__icontains=query)
        )
        print("GOT A QUERY")
    else:
        posts = Post.objects.all()
    
    context = {
        'query': query,
        'posts': posts
    }
    
    return render(request, 'feed.html', context)


# View to render profile page
def profile(request):
    context = {
        'user': request.user  # This is the currently logged in user hopefully
    }
    return render(request, 'profile.html', context)


# View to handle accepting a post
def post_accept(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # Handle post acceptance here, e.g. update the post status to accepted
        # and notify the poster
        post.status = 'accepted'
        post.save()
        messages.success(request, 'Post accepted!')
        return redirect('post_details', pk=post.pk)

    context = {'post': post}
    return render(request, 'post_accept.html', context)


# View to inspect the details of a post and possibly chat later
def post_details(request, pk):

    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }

    return render(request, 'post_details.html', context)


# View for registering a new user
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("feed")
            
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


# View for logging in a user
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("feed")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})
