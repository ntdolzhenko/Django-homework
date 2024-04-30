from django.http import HttpResponse
from django.urls import reverse

def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_page_url = reverse('quality_control:quality_control')
    html = f"<h1>Страница приложения tasks</h1><a href='{another_page_url}'>Перейти на другую страницу<br /></a><a href='{quality_control_page_url}'>Страница приложения quality_control</a>"
    return HttpResponse(html)
def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")
