from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import Project, Task
from django.shortcuts import render

# def index(request):
#     # another_page_url = reverse('tasks:another_page')
#     projects_list_url = reverse('tasks:projects_list')
#     quality_control_page_url = reverse('quality_control:quality_control')
#     html = f"<h1>Страница приложения tasks</h1><a href='{projects_list_url}'>\
#               Список всех проектов<br /></a><a href='{quality_control_page_url}'>Страница приложения quality_control</a>"
#     return HttpResponse(html)

def index(request):
    return render(request, 'tasks/index.html')

# def another_page(request):
#     return HttpResponse("Это другая страница приложения tasks.")

# def projects_list(request):
#     projects = Project.objects.all()
#
#     projects_html = '<h1>Список проектов</h1><ul>'
#     for project in projects:
#         projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
#     projects_html += "</ul>"
#
#     return HttpResponse(projects_html)

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list':projects})

# def project_detail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     tasks = project.tasks.all()
#
#     response_html = f'<h1>{project.name}</h1><p>{project.description}</p><h2>Задачи</h2><ul>'
#     for task in tasks:
#         response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
#     response_html += '</ul>'
#
#     return HttpResponse(response_html)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project':project})

# def task_detail(request, project_id, task_id):
#     project = get_object_or_404(Project, id=project_id)
#     task = get_object_or_404(Task, id=task_id, project=project)
#
#     response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
#
#     return HttpResponse(response_html)

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task':task})

######################################################
from django.views import View
from django.views.generic import ListView, DetailView

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         # projects_list_url = reverse('tasks:projects_list')
#         # html = f"<h1>Страница приложения task</h1><a href='{projects_list_url}'>Список параметров объекта</a>"
#         # return HttpResponse(html)
#
#         projects_list_url = reverse('tasks:projects_list')
#         quality_control_page_url = reverse('quality_control:quality_control')
#         html = f"<h1>Страница приложения tasks</h1><a href='{projects_list_url}'>Список всех проектов<br /></a><a href='{quality_control_page_url}'>Страница приложения quality_control</a>"
#         return HttpResponse(html)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')

# class ProjectsListView(ListView):
#     model = Project # модель работает с представлением объектов Project
#     def get(self, request, *args, **kwargs):
#         projects = self.get_queryset()
#
#         projects_html = '<h1>Список проектов</h1><ul>'
#         for project in projects:
#             projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
#         projects_html += '</ul>'
#
#         return HttpResponse(projects_html)

class ProjectsListView(ListView):
    model = Project # модель работает с представлением объектов Project
    template_name = 'tasks/projects_list.html'

# class ProjectDetailView(DetailView):
#     model = Project # модель работает с представлением объектов Project
#     pk_url_kwarg = 'project_id'
#     def get(self, request, *args, **kwargs):
#
#         self.object = self.get_object()
#         project = self.object
#         tasks = project.tasks.all()
#
#         response_html = f'<h1>{project.name}</h1><p>{project.description}</p><h2>Задачи</h2><ul>'
#         for task in tasks:
#             response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
#         response_html += '</ul>'
#
#         return HttpResponse(response_html)

class ProjectDetailView(DetailView):
    model = Project # модель работает с представлением объектов Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'

# class TaskDetailView(DetailView):
#     model = Task # модель работает с представлением объектов Task
#     pk_url_kwarg = 'task_id'
#     def get(self, request, *args, **kwargs):
#
#         task = self.get_object()
#
#         response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
#         return HttpResponse(response_html)

class TaskDetailView(DetailView):
    model = Task # модель работает с представлением объектов Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'