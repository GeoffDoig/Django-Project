from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post
from .forms import BlogPostForm

# Create your views here.

def get_posts(request):
    """ Display all blog posts ordered by date created """
    posts = Post.objects.order_by("created_date")
    return render(request, "blogposts.html", {"posts": posts})
        
def post_detail(request, pk):
    """ Display full details of an individual blog post """
    post = get_object_or_404(Post, pk=pk)
    post.views +=1
    post.save()
    return render(request, "postdetail.html", {"post": post})
        
def create_or_edit_post(request, pk = None):
    """ Create a view that allows the user to create or edit a post depending
        if the Post_id is null or not """
    post = get_object_or_404(Post, pk=pk) if pk else None
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        form = BlogPostForm(request.POST, initial={"username": user}, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, "You have posted successfully")
            return redirect(post_detail, post.pk)
        else:
            messages.error(request, "Unable to post at this time")
    else:
        form = BlogPostForm(initial={"username": user}, instance=post)
    return render(request, "blogpostform.html", {"form": form})
