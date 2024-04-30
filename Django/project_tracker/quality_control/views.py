from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import BugReport, FeatureRequest

# def index(request):
#     #another_page_url = reverse('quality_control:another_page')
#     bugs_page_url = reverse('quality_control:bug_list')
#     features_page_url = reverse('quality_control:feature_list')
#     html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов<br /></a><a href='{features_page_url}'>Запросы на улучшение</a>"
#     return HttpResponse(html)

def index(request):
    return render(request, 'quality_control/index.html')

# def bug_list(request):
#     bugs = BugReport.objects.all()
#
#     bugs_html = "<h1>Cписок отчетов об ошибках</h1>"
#     for bug in bugs:
#         bugs_html += (f'<h3>{bug.title}</h3>Статус: {bug.status}<br /><a href="{bug.id}/">Подробнее</a>')
#     bugs_html += "</ul>"
#     return HttpResponse(bugs_html)

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list':bugs})

# def feature_list(request):
#     features = FeatureRequest.objects.all()
#
#     features_html = "<h1>Список запросов на улучшение</h1>"
#     for feature in features:
#         features_html += (f'<h3>{feature.title}</h3>Статус: {feature.status}<br /><a href="{feature.id}/">Подробнее</a>')
#
#     features_html += "</ul>"
#     return HttpResponse(features_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list':features})

# def bug_detail(request, bug_id:int):
#     html = f"<a>Детали бага {bug_id}</a>"
#     return HttpResponse(html)


# def feature_id_detail(request, feature_id:int):
#     html = f"<a>Детали улучшения {feature_id}</a>"
#     return HttpResponse(html)




######################################################

from django.views import View
from django.views.generic import DetailView

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         bugs_page_url = reverse('quality_control:bug_list')
#         features_page_url = reverse('quality_control:feature_list')
#         html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов<br /></a><a href='{features_page_url}'>Запросы на улучшение</a>"
#         return HttpResponse(html)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

# class BugDetailView(DetailView):
#     model = BugReport # модель работает с представлением объектов BugReport
#     pk_url_kwarg = 'bug_id'
#     def get(self, request, *args, **kwargs):
#
#         bug = self.get_object()
#
#         response_html = f'<h1>{bug.title}</h1><li><b>Описание:</b> {bug.description}</li>' +\
#                         f'<li><b>Статус:</b> {bug.status}</li><li><b>Приоритет:</b> {bug.priority}</li>' +\
#                         f'<li><b>Проект:</b> {bug.project}</li><li><b>Задача:</b> {bug.task}</li>'
#         return HttpResponse(response_html)

class BugDetailView(DetailView):
    model = BugReport # модель работает с представлением объектов BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

# class FeatureDetailView(DetailView):
#     model = FeatureRequest # модель работает с представлением объектов FeatureRequest
#     pk_url_kwarg = 'feature_id'
#     def get(self, request, *args, **kwargs):
#
#         feature = self.get_object()
#
#         response_html = f'<h1>{feature.title}</h1><li><b>Описание:</b> {feature.description}</li>' +\
#                         f'<li><b>Статус:</b> {feature.status}</li><li><b>Приоритет:</b> {feature.priority}</li>' +\
#                         f'<li><b>Проект:</b> {feature.project}</li><li><b>Задача:</b> {feature.task}</li>'
#         return HttpResponse(response_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest # модель работает с представлением объектов FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'