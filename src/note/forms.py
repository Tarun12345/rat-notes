from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from sirtrevor.forms import SirTrevorFormField
from sirtrevor.widgets import SirTrevorWidget
from models import *
class UserAuthenticationForm(AuthenticationForm):
    # add your form widget here
    username = forms.CharField(max_length=30, widget = forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class CommitMetaForm(forms.Form):
    """These correspond to a particular commit or iteration of a note."""
    anonymous = forms.BooleanField(required=False)

class SetMetaForm(forms.Form):
    """Extra set options"""
    anyone_can_edit = forms.BooleanField(required=False)
    private = forms.BooleanField(required=False)
    expires = forms.ChoiceField(
        choices = (
            ("never", "Never"),
            ("hour", "1 Hour"),
            ("day", "1 Day"),
            ("month", "1 Month"),
        ), required=False
    )

class SetForm(forms.Form):
    name = forms.CharField(max_length=256, required=False,
            widget=forms.widgets.TextInput(attrs={
                'placeholder': 'Add set name...'
            }))

    def clean_name(self):
        d = self.cleaned_data.get('name')
        if d is None:
            return d
        if d == 'Add set name...':
            return ''
        return d


class NoteForm(forms.Form):
    priority = forms.IntegerField(initial=0)
    filename = forms.CharField(max_length=256, required=False,
            widget=forms.widgets.TextInput(attrs={
                'placeholder': 'Title of the note',
                'class': 'filename'
            }))
    note = SirTrevorFormField(widget=SirTrevorWidget, required=False)
    
    def clean_filename(self):
        d = self.cleaned_data.get('filename')
        if d is None:
            return d
        if d == 'Title of the note':
            return ''
        return d



class UserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget = forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Again.'}))
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args,
**kwargs)

    class Meta:
        model = User
        exclude = ('date_joined', 'last_login', 'password')

    def save(self, commit=True):
        """See ProfileForm for this error."""
        model = super(UserCreationForm, self).save(commit=False)
        model.username = self.cleaned_data['username']

        if commit:
            model.save()

        return model


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, widget=forms.Textarea)

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        exclude = ('user','masked_email','gravatar')
