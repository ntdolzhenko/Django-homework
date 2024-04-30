from django.urls import path
from tasks.views import index, another_page

app_name = 'tasks'

urlpatterns = [
    path('', index, name='tasks'),
    path('another/', another_page, name='another_page'),
]
