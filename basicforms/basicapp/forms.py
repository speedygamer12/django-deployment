from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with z!")
        #use check_for_z in charField, i.e valadators = [check_for_z]


class FormName(forms.Form):
    name = forms.CharField(validators=[ check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    verify_email = forms.EmailField(label="Enter your Email again!")
    botcatcher = forms.CharField(required=False, 
                                widget = forms.HiddenInput,
                                validators= [validators.MaxLengthValidator(0)])

"""
    #A function to catch bots using the botcatchers fiels without built in validators

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT!")
        return botcatcher
"""