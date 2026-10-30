from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RegisterForm, PostForm, CommentForm, ProfileForm
from .models import Post, Comment, Like, Follow

def feed(request):
    posts = Post.objects.select_related("author", "author__profile").prefetch_related("comments__author", "likes")
    return render(request, "social/feed.html", {"posts": posts, "post_form": PostForm()})

def register(request):
    if request.user.is_authenticated:
        return redirect("feed")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Welcome to SocialHub!")
        return redirect("feed")
    return render(request, "social/register.html", {"form": form})

def profile(request, username):
    person = get_object_or_404(User.objects.select_related("profile"), username=username)
    following = request.user.is_authenticated and Follow.objects.filter(follower=request.user, following=person).exists()
    return render(request, "social/profile.html", {
        "person": person, "posts": person.posts.select_related("author").prefetch_related("comments__author", "likes"),
        "followers": person.follower_relations.count(), "following": person.following_relations.count(),
        "is_following": following,
    })

@login_required
def edit_profile(request):
    form = ProfileForm(request.POST or None, instance=request.user.profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Profile updated.")
        return redirect("profile", username=request.user.username)
    return render(request, "social/edit_profile.html", {"form": form})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been published.")
        else:
            messages.error(request, "Please enter a valid post.")
    return redirect(request.POST.get("next") or "feed")

@login_required
def delete_post(request, post_id):
    if request.method == "POST":
        get_object_or_404(Post, pk=post_id, author=request.user).delete()
        messages.success(request, "Post deleted.")
    return redirect(request.POST.get("next") or "feed")

@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post, comment.author = post, request.user
            comment.save()
    return redirect(request.POST.get("next") or "feed")

@login_required
def toggle_like(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
    return redirect(request.POST.get("next") or "feed")

@login_required
def toggle_follow(request, username):
    if request.method == "POST":
        person = get_object_or_404(User, username=username)
        if person != request.user:
            relation, created = Follow.objects.get_or_create(follower=request.user, following=person)
            if not created:
                relation.delete()
    return redirect("profile", username=username)
