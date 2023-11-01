from django.shortcuts import render,redirect
from .models import Challenge
from algorithms.models import Problem
from django.core.paginator import Paginator #페이지네이션 구현 모듈
from .forms import ChallengeForm
from django.utils import timezone
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            problem = Problem.objects.get(problem_num=challenge.problem)
            challenge.rank = problem.rank
            form.save()
            return redirect('challenges:index')
    else:
        form = ChallengeForm()
    now = timezone.now()
    challenges = Challenge.objects.all().order_by('-created_at')
    for challenge in challenges:
        if challenge.created_at.date() == now.date():
            challenge.is_today = 1
        else:
            challenge.is_today = 0
    # 페이지네이션 객체(paginator)
    paginator = Paginator(challenges,3) # challenge 리스트 3개 단위로 잘라 보여줌
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'challenges' : posts,
     
        'form' : form,
    }
    
    return render(request,'challenges/index.html',context)

def detail(request,challenge_pk):
    challenge = Challenge.objects.get(pk=challenge_pk)
    context = {
        'challenge' : challenge
    }
    return render(request,'challenges/detail.html',context)
