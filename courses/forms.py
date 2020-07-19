from django.forms import ModelForm
from .models import course

class courseForm(ModelForm):
    class Meta:
        model=course
        fields=['CourseName','urlcourse','about']