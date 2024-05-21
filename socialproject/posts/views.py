from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


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
    return render(request, "posts/post_list.html", {'posts': posts})
