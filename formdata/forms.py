from django.forms import ModelForm

from formdata.models import FormData


class Form(ModelForm):
    class Meta:
        model = FormData
        fields = '__all__'