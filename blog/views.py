from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import BlogPostForm


def get_posts(request):
    """
    Display all blog posts ordered by date created
    """
    posts = Post.objects.order_by("created_date")
    return render(request, "blogposts.html", {"posts": posts})


def post_detail(request, pk):
    """
    Display full details of an individual blog post
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {"post": post})


@login_required
def create_post(request):
    """
    Allow the user to create a new blog post
    """
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.avatar = user.userprofile.avatar.url
            post.save()
            messages.success(request, "You have posted successfully")
            return redirect("get_posts")
        else:
            messages.error(request, "Unable to post at this time")
    else:
        form = BlogPostForm()
    return render(request, "blogpostform.html", {"form": form})
