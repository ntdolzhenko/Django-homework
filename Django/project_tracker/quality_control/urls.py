from django.urls import path
from quality_control.views import index, bug_list, feature_list, bug_detail, feature_id_detail

app_name = 'quality_control'

urlpatterns = [
    path('', index, name='quality_control'),
    path('bugs/', bug_list, name='bug_list'),
    path('features/', feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', feature_id_detail, name='feature_id_detail')
]