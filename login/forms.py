from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import requests


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


class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserProfile # may have to be UserProfile
        exclude = (
            'user',
            'picture',
            'date_created',
            'password',
            'helped',

        )