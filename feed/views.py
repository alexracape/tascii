from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from .forms import NewUserForm
from .forms import PostForm
from feed.models import Post
from datetime import timedelta
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RatingForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Main feed view
def feed(request, sort="created_at"):
    
    query = request.GET.get('query')
    sort = sort if sort == 'expiration_date' else '-' + sort
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(start_loc__icontains=query) | Q(end_loc__icontains=query)
        ).order_by(sort)
    else:
        posts = Post.objects.filter(Q(status='open')).order_by(sort)
    
    context = {
        'query': query,
        'posts': posts
    }
    
    return render(request, 'feed.html', context)


# View to render profile page
def profile(request):
    active_tasks = Post.objects.filter(
        Q(status='accepted') and Q(filled_by=request.user)
    )

    complete_tasks = Post.objects.filter(
        Q(status='completed')
        # Q(status='completed'and Q(filled_by=user.username)
    )

    posted_tasks = Post.objects.filter(
        Q(user_id=request.user)
    )



    context = {
        'user': request.user,  # This is the currently logged in user hopefully
        'active_tasks': active_tasks,
        'history': complete_tasks,
        'posted_tasks': posted_tasks
    }
    return render(request, 'profile.html', context)


# View to handle accepting a post
def post_accept(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # Handle post acceptance here, e.g. update the post status to accepted
        # and notify the poster
        post.status = 'accepted'
        post.filled_by = request.user
        post.save()

        messages.success(request, 'Post accepted!')
        return redirect('profile')

    context = {'post': post}
    return render(request, 'profile.html', context)


# View to inspect the details of a post and possibly chat later
def post_details(request, pk):

    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }

    return render(request, 'post_details.html', context)


# View for registering a new user
def register_request(request):

    context = {}
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("feed")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        print(form.is_valid())

        # if form.errors:
        #     messages.error(request, "Unsuccessful registration. Invalid information.")
        #     context['errors'] = form.errors
    else:
        form = NewUserForm()
        
    context["register_form"] = form
    return render (request=request, template_name="register.html", context=context)


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
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

# View for making a post
def make_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save(request.user)
            return redirect('profile')
    
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'make_post.html', {'form': form})


def edit_post(request, pk):
    print("ENTERING EDIT VIEW")
    post = Post.objects.get(pk=pk)
    form = PostForm(request.POST or None, initial={
        'title': post.title,
        'price': post.price,
        'start_loc': post.start_loc,
        'end_loc': post.end_loc,
        'expiration_date': post.expiration_date,
        'time_estimate': post.time_estimate,
    })
    if form.is_valid():
        print("FORM WAS VALID")
        post.title = form.cleaned_data['title']
        post.price = form.cleaned_data['price']
        post.start_loc = form.cleaned_data['start_loc']
        post.end_loc = form.cleaned_data['end_loc']
        post.expiration_date = form.cleaned_data['expiration_date']
        post.time_estimate = timedelta(minutes=int(form.cleaned_data['time_estimate']))
        post.save()
        return redirect('post_details', pk=post.pk)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'edit_post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("feed")

def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

# View to handle creating a review
@login_required
def make_review(request, user_id):
    reviewed_user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            review = form.save(post=Post.objects.filter(user=reviewed_user).first(), user=request.user)
            messages.success(request, 'Review saved!')
            return redirect('profile')

    else:
        form = RatingForm()

    context = {'form': form, 'reviewed_user': reviewed_user}
    return render(request, 'make_review.html', context)
