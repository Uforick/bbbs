from django import forms


class EventAdminForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        start_at = cleaned_data.get('start_at')
        end_at = cleaned_data.get('end_at')
        if start_at > end_at:
            message = 'Дата начала события не может быть больше даты окончания.'
            raise forms.ValidationError(message)
