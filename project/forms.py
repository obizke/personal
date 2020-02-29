from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce import TinyMCE

from juben.models import Contact
from project.models import Post, Comment, Jwear, Item


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    profile = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'profile')


class UserDeleteForm(forms.Form):
    class Meta:
        model = User
        fields = []


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'max_length ': 30,

    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'max_length': 254,
        ' help_text': 'Required. Inform a valid email address.'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'max_length': 100,
        ' help_text': ' Message subject.'
    }))

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        message = cleaned_data.get('message')
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        subject = cleaned_data.get('subject')
        if not message and not name and not email and not subject:
            raise forms.ValidationError('You have to write something!')

    class Meta:
        model = Contact
        fields = ('message', 'name', 'email', 'subject')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Jwear
        fields = ('user',)


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(mce_attrs={'width': 800}))

    class Meta:
        model = Post
        fields = (
        'title', 'image', 'content', 'categories', 'status', 'featured', 'author', 'previous_post', 'next_post')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'category', 'image', 'descriptions', 'quantity', 'price', 'discount','status')
