from django import forms
from tinymce.widgets import TinyMCE
from .models import SinglePage


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PageForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = SinglePage
        fields = '__all__'
