from django import forms
from .models import *

class MemberForm(forms.Form):
    member = forms.ModelChoiceField(Member.objects,  label='', empty_label='選択してください', to_field_name='name', required=False)

TEMPERATURE_CHOICES = (

                ('35.5', '35.5'),
                ('35.6', '35.6'),
                ('35.7', '35.7'),
                ('35.8', '35.8'),
                ('36.0', '36.0'),
                ('36.1', '36.1'),
                ('36.2', '36.2'),
                ('36.3', '36.3'),
                ('36.4', '36.4'),
                ('36.5', '36.5'),
                ('36.6', '36.6'),
                ('36.7', '36.7'),
                ('36.8', '36.8'),
                ('36.9', '36.9'),
                ('37.0', '37.0'),
                ('37.1', '37.1'),
                ('37.2', '37.2'),
                ('37.3', '37.3'),
                ('37.4', '37.4'),
                ('37.5', 'その他'),
)




class VisitorsForm(forms.ModelForm):
    temperature = forms.fields.ChoiceField(
        choices = TEMPERATURE_CHOICES,
        required = False,
    )
    accompany1_temp = forms.fields.ChoiceField(
        choices = TEMPERATURE_CHOICES,
        required = False,
    )
    accompany2_temp = forms.fields.ChoiceField(
        choices = TEMPERATURE_CHOICES,
        required = False,
    )
    accompany3_temp = forms.fields.ChoiceField(
        choices = TEMPERATURE_CHOICES,
        required = False,
    )
    class Meta:
        model = Visitors
        fields = ('date', 'time', 'company_name', 'visitor_name', 'temperature',
                'accompany1_name', 'accompany1_temp', 'accompany2_name', 'accompany2_temp',
                'accompany3_name', 'accompany3_temp', 'position', 'interviewer', 'content')
        labels={
           'date':'',
           'time':'',
           'company_name':'',
           'visitor_name': '',
           'temperature': '',
           'accompany1_name': '',
           'accompany1_temp': '',
           'accompany2_name': '',
           'accompany2_temp': '',
           'accompany3_name': '',
           'accompany3_temp': '',
           'position': '',
           'interviewer': '',
           'content': '',
        #    'is_contacted': '',
           }


class ContactForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     # first call parent's constructor
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     # there's a `fields` property now
    #     # for key in self.fields.keys():
    #     #     self.fields[key].required = False
    #     self.fields['interviewer'].required = False
    #     self.fields['time'].required = False
    #     self.fields['contents'].required = False
    # time = forms.TimeField(required=False)
    # contents = forms.CharField(widget=forms.Textarea, required=False) 
    class Meta:
        model = Contact
        fields = ('interviewer', 'time', 'contents')
        labels = {
            'interviewer': '',
            'time': '',
            'contents': '',
        }

        # fields = ('contact', 'interviewer', 'time', 'contents')
        # labels = {
        #     'contact': '',
        #     'interviewer': '',
        #     'time': '',
        #     'contents': '',
        # }