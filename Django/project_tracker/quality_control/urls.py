from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='quality_control'),
    path('', views.IndexView.as_view(), name='quality_control'),

    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),

    path('bugs/', views.BugsListView.as_view(), name='bug_list'),
    path('features/', views.FeaturesListView.as_view(), name='feature_list'),

    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),

    path('bugs/', views.BugsListView.as_view(), name='bug_list'),
    path('features/', views.FeaturesListView.as_view(), name='feature_list'),

    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),

    path('bugs/new/', views.add_bugreport, name='add_bugreport'),
    path('features/new/', views.add_feature, name='add_feature'),

    path('bugs/new/', views.BugCreateView.as_view(), name='add_bugreport'),
    path('features/new/', views.FeatureCreateView.as_view(), name='add_feature'),

    path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),

    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),

    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]