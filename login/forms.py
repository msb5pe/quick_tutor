from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
import requests


class set_location_form(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("location",)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            # 'username',
            'first_name',
            'last_name',
            'email',
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'first_name', 'last_name', 'email')



def call_star(str):
    r = requests.get("http://stardock.cs.virginia.edu/louslist/courses/view/" + str + "?JSON")
    ret_ary = []
    for line in r.text.split("\n"):
        s = line.split(';')
        try:
            ret_ary.append(s[0] + " " + s[1])
        except:
            pass
    ret_ary = list(set(ret_ary))
    return ret_ary

class ClassesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ClassesForm, self).__init__(*args, **kwargs)
        self.fields['ClassesForm'] = forms.ChoiceField(
            choices=call_star(args))