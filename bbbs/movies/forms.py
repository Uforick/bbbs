import re

from django import forms

DOMAIN = 'youtube'


class MovieAdminForm(forms.ModelForm):
    def clean(self):
        link = self.cleaned_data.get('link', None)
        image = self.cleaned_data.get('imageUrl', None)
        if not image and not re.findall(DOMAIN, link):
            raise forms.ValidationError(
                "Добавьте изображение к данному видео!"
            )
