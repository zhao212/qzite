from django import forms
from myresume.models import *

class ResBasicForm(forms.ModelForm):

    class Meta():
        model = res_basic
        fields = ('last_name','first_name','birthday','email','phone','address','title','city','state','zipcode')

        widgets = {
            # 'author':forms.HiddenInput(initial = user),
            'last_name':forms.TextInput(attrs = {'class':'textinputclass'}),
            'last_name':forms.TextInput(attrs = {'class':'textinputclass'}),
            'birthday':forms.DateInput(attrs = {'class':'textinputclass','format':'%m/%d/%Y'}),
            'email':forms.EmailInput(attrs = {'class':'textinputclass'}),
            'phone':forms.TextInput(attrs = {'class':'textinputclass'}),
            'address':forms.TextInput(attrs = {'class':'textinputclass'}),
            'city':forms.TextInput(attrs = {'class':'textinputclass'}),
            'state':forms.TextInput(attrs = {'class':'textinputclass'}),
            'zipcode':forms.TextInput(attrs = {'class':'textinputclass'}),
            'title':forms.TextInput(attrs = {'class':'textinputclass'}),
                   }

class ResEduForm(forms.ModelForm):

    class Meta():
        model = res_education
        fields = ('education_name','degree','major','start_date','end_date')

        widgets = {
            # 'author':forms.HiddenInput(initial = user),
            'education_name':forms.TextInput(attrs = {'class':'textinputclass'}),
            'degree':forms.TextInput(attrs = {'class':'textinputclass'}),
            'major':forms.TextInput(attrs = {'class':'textinputclass'}),
            'start_date':forms.DateInput(attrs = {'class':'textinputclass','format':'%m/%d/%Y'}),
            'end_date':forms.DateInput(attrs = {'class':'textinputclass','format':'%m/%d/%Y'}),
                   }

class ResProForm(forms.ModelForm):

    class Meta():
        model = res_project
        fields = ('project_name','description','start_date','end_date')

        widgets = {
            # 'author':forms.HiddenInput(initial = user),
            'project_name':forms.TextInput(attrs = {'class':'textinputclass'}),
            'start_date':forms.DateInput(attrs = {'class':'textinputclass','format':'%m/%d/%Y'}),
            'end_date':forms.DateInput(attrs = {'class':'textinputclass','format':'%m/%d/%Y'}),
            'description':forms.Textarea(attrs = {'class':'textinputclass'}),
                   }


class ResWorkForm(forms.ModelForm):

    class Meta():
        model = res_work
        fields = ('work_title','company_name','description','start_date','end_date')

        widgets = {
            # 'author':forms.HiddenInput(initial = user),
            'work_title':forms.TextInput(attrs = {'class':'textinputclass'}),
            'company_name':forms.TextInput(attrs = {'class':'textinputclass'}),
            'start_date':forms.DateInput(attrs = {'class':'textinputclass','format':'%m/%d/%Y'}),
            'end_date':forms.DateInput(attrs = {'class':'textinputclass','format':'%m/%d/%Y'}),
            'description':forms.Textarea(attrs = {'class':'textinputclass'}),
                   }

class ResSkillForm(forms.ModelForm):

    class Meta():
        model = res_skill
        fields = ('skill_name',)
        widgets = {
            'skill_name':forms.TextInput(attrs = {'class':'textinputclass'}),
        }

class ResAwardForm(forms.ModelForm):

    class Meta():
        model = res_award
        fields = ('award_name','get_year')
        widgets = {
            'skill_name':forms.TextInput(attrs = {'class':'textinputclass'}),
            'get_year':forms.DateInput(attrs = {'class':'textinputclass','format':'%m/%d/%Y'}),
        }
