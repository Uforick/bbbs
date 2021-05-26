from django import forms


class ProfileAdminForm(forms.ModelForm):
    def clean_city(self):
        city = self.cleaned_data['city']
        role = self.cleaned_data['role']
        if city.count() > 1 and role == 'MENTOR':
            raise forms.ValidationError(
                "У наставника не может быть больше одного города."
            )
        return city
