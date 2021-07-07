from django import forms


class ArticlesAdminForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        show_on_main_page = cleaned_data.get('show_on_main_page')
        quote = cleaned_data.get('quote')
        if not quote and show_on_main_page:       
            message = ('Заполните Цитату статьи для отображения '
                       'на Главной Странице.')
            raise forms.ValidationError(message)
