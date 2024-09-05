from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm

# Create your views here.

def tasks_view(request):
    tasks = Task.objects.all()
    empty_form = TaskForm()

    if request.method == "POST":
        if len(request.POST) <= 3:
            if request.POST['task_id']:
                task = Task.objects.get(id=request.POST['task_id'])
                if task:
                    task.delete()
                    return redirect(reverse("tasks:home"))
                
    
    else:

        context = {
            "tasks": tasks,
            "create_task": empty_form,
        }

    # create_tasks(request)

        return render(request, "tasks/tasks.html", context)


def save_tasks(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:home"))
        else:
            return render(request, "tasks/tasks.html", {"create_task": form})
