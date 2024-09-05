from django import forms
from .models import Task


# create a form that will fetch the task data

class TaskForm(forms.ModelForm):
    template_name = "accounts/form_template.html"

    time = forms.DateTimeField(widget=forms.TextInput(attrs={"type": "datetime-local"}))

    def save(self, commit=True, *args, **kwargs):
        task = super().save(commit=False)

        task.time = self.cleaned_data['time']
        if commit:
            super().save()

    class Meta:
        model = Task
        fields = ['title', 'description',]
