from django import forms
from django.contrib.auth.models import User

from mymsg.models import *

class msgForm(forms.ModelForm):

    class Meta():
        model = msg
        fields = ('receiver','title','text')

        widgets = {
            'receiver':forms.TextInput(attrs = {'class':'textinputclass'}),
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'text':forms.Textarea(attrs = {'class':'textinputclass'})
        }
    def clean_receiver(self):
        receiver = self.cleaned_data['receiver']
        if not User.objects.filter(username = receiver).exists():
            raise forms.ValidationError("Invalid receiver.")
        return receiver
