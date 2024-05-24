from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from users.models import Profile


@login_required
# Create your views here.
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("posts:post_list")
    return render(request, "posts/new_post.html", {'form': form})


def post_list(request):
    posts = Post.objects.all()
    profile = Profile.objects.all()
    logged_user = request.user
    return render(request, "posts/post_list.html",
                  {'posts': posts,
                   "profile": profile,
                   "logged_user": logged_user})


def like(request):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect("posts:post_list")
