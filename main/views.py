from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Main
from plans.models import Plan
# from challenges.models import Challenge

from .forms import MainForm, CommentForm
# Create your views here.
def index(request):
    mains = Main.objects.all()
    plans = Plan.objects.all()
    # challenges = Challenge.objects.all()
    context = {
        'mains': mains,
        'plans': plans,
        # 'challenges' : challenges,
    }
    return render(request, 'main/index.html', context)


def detail(request, pk):
    main = Main.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = main.comment_set.all()
    context = {
        'main': main,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'main/detail.html', context)

