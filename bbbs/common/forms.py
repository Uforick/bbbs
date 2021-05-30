from django import forms

from bbbs.common.models import Profile


class ProfileAdminForm(forms.ModelForm):
    def clean(self):
        city = self.cleaned_data['city']
        role = self.cleaned_data['role']
        if city.count() > 1 and role == Profile.PermissionChoice.MENTOR:
            raise forms.ValidationError(
                "У наставника не может быть больше одного города."
            )
