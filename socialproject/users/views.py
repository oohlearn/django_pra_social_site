from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, ProfileForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
from .models import Profile
from posts.models import Post
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # 把LoginForm post的結果存進form變數
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"])
            # authenticate的功能是會去資料庫裡尋找是否符合的資料，有就會存成一個User object
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse("user authentication failed")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return render(request, "users/logout.html")

@login_required
def home(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user).first()
    posts = Post.objects.filter(user=current_user)
    return render(request, "posts/post_list.html", {'posts': posts,
                                                "profile": profile})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            Profile.objects.create(user=user)
            return render(request, "users/register_done.html")
    
    return render(request, "users/register.html", {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(request.POST, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("home")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, "users/edit.html",
                  {'user_form': user_form, 'profile_form': profile_form})