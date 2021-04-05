from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .forms import MentorForm


def index(request):
    return render(request, 'main/new.html')


def celebrity(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/celebrity.html', {'title': 'Main page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Form is invalid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new_notes.html', context)


def find_mentor(request):
    error = ''
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Form is invalid'
    form = MentorForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/mentorFind.html', context)
