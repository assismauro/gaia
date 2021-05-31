from django import forms

class docForm(forms.Form):
    name = forms.CharField(max_length=50, label=" Nome" , help_text="Forneça o nome.")

    def clean_name(self):
        data = self.cleaned_data('name')
        return data
