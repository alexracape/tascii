from datetime import date, datetime, timedelta
from django.utils import timezone

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from feed.models import Post 
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class PostForm(forms.Form):

    TIME_ESTIMATE_CHOICES = (
        (5, '5 minutes'),
        (10, '10 minutes'),
        (15, '15 minutes'),
        (30, '30 minutes'),
        (60, '1 hour'),
    )

    title = forms.CharField(label='Title:', max_length=100)
    price = forms.IntegerField(label = 'Price:')
    start_loc = forms.CharField(label = 'Start Location:', max_length=100)
    end_loc = forms.CharField(label = 'End Location', max_length=100)
    # expiration_date = forms.DateTimeField(label = 'Delivery window:')
    expiration_date = forms.DateTimeField(
        label='Expiration:',
        widget=DateTimePickerInput(options={
            "format": "YYYY-MM-DD HH:mm a",
            "showClose": True,
            "showClear": True,
            "showTodayButton": True,
            "sideBySide": True,
            "stepping": 15,
        })
    )
    time_estimate = forms.ChoiceField(label = 'Time Estimate:', choices=TIME_ESTIMATE_CHOICES, initial=5)
    #created_at = forms.DateTimeField(auto_now_add=True)

    def save(self, user, commit=True):
        cleaned_data = super().clean()
        post = Post(
            title=cleaned_data['title'],
            price=cleaned_data['price'],
            start_loc=cleaned_data['start_loc'],
            end_loc=cleaned_data['end_loc'],
            expiration_date=cleaned_data['expiration_date'],
            time_estimate= timedelta(minutes=int(cleaned_data['time_estimate'])),
            status='open',
            user=user
        )
        post.save()
        return post

