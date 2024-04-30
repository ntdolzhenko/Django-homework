from django.http import HttpResponse
from django.urls import reverse

def index(request):
    #another_page_url = reverse('quality_control:another_page')
    bugs_page_url = reverse('quality_control:bug_list')
    features_page_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов<br /></a><a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)
def bug_list(request):
    html = f"<h1>Cписок отчетов об ошибках</h1>"
    return HttpResponse(html)
def feature_list(request):
    html = f"<h1>Список запросов на улучшение</h1>"
    return HttpResponse(html)
def bug_detail(request, bug_id:int):
    html = f"<a>Детали бага {bug_id}</a>"
    return HttpResponse(html)

def feature_id_detail(request, feature_id:int):
    html = f"<a>Детали улучшения {feature_id}</a>"
    return HttpResponse(html)