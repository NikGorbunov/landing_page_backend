from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
