from django import forms
from django.forms import ModelForm
from .models import Project, Task

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Bаше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(widget = forms.Textarea, label='Сообщение')

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)

        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('description', css_class='form-control', rows=3),
            Submit('submit', 'Submit', css_class='btn bin-primary')
        )

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'project', 'assignee']