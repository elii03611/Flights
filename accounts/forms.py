from django import forms

from .models import Customer


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        

    # def __init__(self, user, *args, **kwargs):
    #     super(CustomersForm, self).__init__(*args, **kwargs)
    #     if not user.is_staff:
    #         self.fields['user'].widget = forms.HiddenInput()


