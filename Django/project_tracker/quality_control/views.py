from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views.generic import CreateView, ListView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import BugReportForm, FeatureRequestForm
from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, UpdateView

# def index(request):
#     #another_page_url = reverse('quality_control:another_page')
#     bugs_page_url = reverse('quality_control:bug_list')
#     features_page_url = reverse('quality_control:feature_list')
#     html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов<br /></a><a href='{features_page_url}'>Запросы на улучшение</a>"
#     return HttpResponse(html)

##########################################################################################
def index(request):
    return render(request, 'quality_control/index.html')
# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         bugs_page_url = reverse('quality_control:bug_list')
#         features_page_url = reverse('quality_control:feature_list')
#         html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов<br /></a><a href='{features_page_url}'>Запросы на улучшение</a>"
#         return HttpResponse(html)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

##########################################################################################

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list':bugs})

# def bug_list(request):
#     bugs = BugReport.objects.all()
#
#     bugs_html = "<h1>Cписок отчетов об ошибках</h1>"
#     for bug in bugs:
#         bugs_html += (f'<h3>{bug.title}</h3>Статус: {bug.status}<br /><a href="{bug.id}/">Подробнее</a>')
#     bugs_html += "</ul>"
#     return HttpResponse(bugs_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list':features})

# def feature_list(request):
#     features = FeatureRequest.objects.all()
#
#     features_html = "<h1>Список запросов на улучшение</h1>"
#     for feature in features:
#         features_html += (f'<h3>{feature.title}</h3>Статус: {feature.status}<br /><a href="{feature.id}/">Подробнее</a>')
#
#     features_html += "</ul>"
#     return HttpResponse(features_html)

class BugsListView(ListView):
    model = BugReport # модель работает с представлением объектов BugReport
    template_name = 'quality_control/bug_list.html'

class FeaturesListView(ListView):
    model = FeatureRequest # модель работает с представлением объектов FeatureRequest
    template_name = 'quality_control/feature_list.html'

##########################################################################################

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bugreport':bug})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'featurerequest':feature})

class BugDetailView(DetailView):
    model = BugReport # модель работает с представлением объектов BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

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


#############################################################################################
def add_bugreport(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()

    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()

    return render(request, 'quality_control/feature_request_form.html', {'form': form})

class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:add_bugreport')

class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    def form_valid(self, form):
        form.instanse.project = get_object_or_404(FeatureRequest, pk=self.kwargs['feature_id'])
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('quality_control:feature_detail', kwargs={'feature_id': self.kwargs['feature_id']})

#############################################################################################

def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug':bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature_id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature':feature})

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    def get_success_url(self):
        return reverse('quality_control:feature_detail', kwargs={'feature_id': self.object.feature.id})


#############################################################################################


def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')

def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list')


class BugDeleteView(DeleteView):
    model = BugReport
    template_name = 'quality_control/bug_confirm_delete.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    def get_success_url(self):
        return reverse('quality_control:feature_detail', kwargs={'feature_id': self.object.feature.id})

#############################################################################################