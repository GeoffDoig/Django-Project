from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, ProfileUpdateForm
from issues.models import Issue, Comment
from blog.models import Post
from checkout.models import Order
import matplotlib.pyplot as plt
import io
import urllib, base64

# Create your views here.

def index(request):
    """ Display index.html file """
    blogposts = Post.objects.all().count()
    bug_issues = Issue.objects.filter(category="B").count()
    feature_issues = Issue.objects.filter(category="F").count()
    bug_comments = Comment.objects.filter(issue__category="B").count()
    feature_comments = Comment.objects.filter(issue__category="F").count()
    
    frequency = [blogposts, bug_comments, feature_comments, bug_issues, feature_issues]
    activities = ["Blog Posts", "Bug Comments", "Feature\nComments", "Bugs Raised", "Features Requested"]
    colors = ["maroon", "blue", "cyan", "green", "yellowgreen"]
    plt.pie(frequency, labels=activities, colors=colors, startangle=90, autopct="%1.1f%%", shadow=True)
    plt.title("Site Activities")
    
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return render(request, "index.html", {"pie_chart": uri})

def logout(request):
    """ Log the user out """
    auth.logout(request)
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
                return redirect("issues")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:    
        registration_form = UserRegistrationForm()
    return render(request, "registration.html", {"registration_form": registration_form})

@login_required    
def user_profile(request):
    """ Display the user's profile page """
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        update_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.userprofile)
        if update_form.is_valid:
            update_form.save()
            messages.success(request, "You have successfully updated your profile")
            return redirect("profile")
        else:
            messages.error(request, "Unable to update your profile at this time")
    else:
        update_form = ProfileUpdateForm(instance=user.userprofile)
    
    num_user_blogposts = Post.objects.filter(author=user).count()
    user_bug_comments = Comment.objects.filter(issue__category="B", username=user).count()
    user_feature_comments = Comment.objects.filter(issue__category="F", username=user).count()
    num_user_bugs = Issue.objects.filter(category="B", username=user).count()
    num_user_features = Issue.objects.filter(category="F", username=user).count()
    
    
    x = [1, 2, 3, 4, 5]
    y = [num_user_bugs, num_user_features, user_bug_comments, user_feature_comments, num_user_blogposts]
    plt.bar(x, y, color=["green", "yellowgreen", "blue", "cyan", "maroon"])
    plt.xlabel("Activity")
    plt.ylabel("Frequency")
    plt.title("Your Stats")
    
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
        
    
    args = {
        "user": user,
        "update_form": update_form,
        "num_user_blogposts": num_user_blogposts,
        "user_bug_comments": user_bug_comments,
        "user_feature_comments": user_feature_comments,
        "num_user_bugs": num_user_bugs,
        "num_user_features": num_user_features,
        "bar_chart": uri
    }
    return render(request, "profile.html", args)