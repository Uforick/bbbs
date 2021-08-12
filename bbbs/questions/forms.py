from django import forms


class QuestionAdminForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        show_on_main_page = cleaned_data.get('show_on_main_page')
        answer = cleaned_data.get('answer')
        if not answer and show_on_main_page:       
            message = ('Заполните поле Ответ!')
            raise forms.ValidationError(message)
