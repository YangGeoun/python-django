from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from accounts.models import User
from accounts.forms import UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('main:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('main:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('main:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('main:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('main:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            print(request.FILES)
            user.image = request.FILES['image']
            user.save()
            return redirect('accounts:profile', user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:profile', user.pk)
    else:
        form = CustomPasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, user_pk):
    # user 의 detail 페이지
    # user 를 조회
    User = get_user_model()
    person = User.objects.get(pk=user_pk)

    # 남이 내 글에 좋아요 누른 개수 총 합
    like_cnt = person.like_plans.all().count()
    for plan in person.user_plans.all():
        like_cnt += plan.like_users.all().count()
    context = {
        'person': person,
        'like_cnt': like_cnt,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request,user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.pk)



class UserRegistrationView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/accounts/login'



class UserLoginView(LoginView):           # 로그인
    template_name = 'accounts/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)  