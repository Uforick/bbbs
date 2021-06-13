from django import forms

from bbbs.common.models import Profile


class ProfileAdminForm(forms.ModelForm):
    def clean(self):
        city = self.cleaned_data.get('city', None)
        if not city:
            raise forms.ValidationError(
                "Заполните поле город."
            )
        role = self.cleaned_data.get('role')
        if city.count() > 1 and role == Profile.PermissionChoice.MENTOR:
            raise forms.ValidationError(
                "У наставника не может быть больше одного города."
            )
