from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, ProfilePicForm
from issues.models import Issue, Comment
from blog.models import Post
from checkout.models import Order

# Create your views here.
def index(request):
    """ Display index.html file """
    return render(request, "index.html")

@login_required    
def logout(request):
    """ Log the user out """
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect("index")
    
def login(request):
    """ Display login page """
    if request.user.is_authenticated:
        return redirect("issues")
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect("issues")
            else:
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})
    
def registration(request):
    """ Display registration page """
    if request.user.is_authenticated:
        return redirect("issues")
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST["username"], password=request.POST["password1"])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:    
        registration_form = UserRegistrationForm()
    return render(request, "registration.html", {"registration_form": registration_form})

@login_required    
def user_profile(request):
    """ Display the user's profile page """
    user = User.objects.get(email=request.user.email)
    user_order = Order.objects.filter(user=user).first()
    user_blogposts = Post.objects.filter(author=user)
    num_user_blogposts = user_blogposts.count()
    bug_comments = Comment.objects.filter(issue__category="B", username=user)
    user_bug_comments = bug_comments.count()
    feature_comments = Comment.objects.filter(issue__category="F", username=user)
    user_feature_comments = feature_comments.count()
    user_bugs = Issue.objects.filter(category="B", username=user)
    num_user_bugs = user_bugs.count()
    user_features = Issue.objects.filter(category="F", username=user)
    num_user_features = user_features.count()
    args = {
        "user": user,
        "user_order": user_order,
        "num_user_blogposts": num_user_blogposts,
        "user_bug_comments": user_bug_comments,
        "user_feature_comments": user_feature_comments,
        "num_user_bugs": num_user_bugs,
        "num_user_features": num_user_features
    }
    return render(request, "profile.html", args)