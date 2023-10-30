from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
class tasklistview(ListView):
    model = Task
    template_name ='home.html'
    context_object_name = 'tasks'


class taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'tasks'

class taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'tasks'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detailview', kwargs={'pk': self.object.id})


class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')


def add(req):
    tasks = Task.objects.all()
    if req.method == "POST":
        name = req.POST.get('task', ' ')
        priority = req.POST.get('priority', ' ')
        date = req.POST.get('date', ' ')
        tasks = Task(name=name, priority=priority, date=date)
        tasks.save()
    return render(req, 'home.html', {'tasks': tasks})


# def detail(request):
#     return render(request,'detail.html',)
def delete(request, taskid):
    tasks = Task.objects.get(id=taskid)
    if request.method == "POST":
        tasks.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request,id):
    tasks = Task.objects.get(id = id)
    fo = todoforms(request.POST or None, instance=tasks)
    if fo.is_valid():
        fo.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': fo, 'tasks': tasks})
