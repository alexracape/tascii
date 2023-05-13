from datetime import timedelta
from django.utils import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from feed.models import Post 
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Rating 
from .models import NewUser

class NewUserForm(NewUser):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    venmo_tag = forms.CharField(max_length=20, required=True)
    rating = forms.IntegerField(initial=5, widget=forms.HiddenInput())
    tasks_completed = forms.IntegerField(initial=0, widget=forms.HiddenInput())
    tasks_posted = forms.IntegerField(initial=0, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "venmo_tag", "password1", "password2", "rating", "tasks_completed", "tasks_posted")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.venmo_tag = self.cleaned_data["venmo_tag"]
        user.rating = self.cleaned_data["rating"]
        user.tasks_completed = self.cleaned_data["tasks_completed"]
        user.tasks_posted = self.cleaned_data["tasks_posted"]
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
    expiration_date = forms.DateTimeField(
        label='Expiration:',
        widget=DateTimePickerInput(options={
            "format": "YYYY-MM-DD HH:mm a",
            "showClose": True,
            "showClear": True,
            "showTodayButton": True,
            "sideBySide": True,
            "stepping": 15,
            "ignoreReadonly": True,
        }, attrs={"readonly": True})
    )
    time_estimate = forms.ChoiceField(label = 'Time Estimate:', choices=TIME_ESTIMATE_CHOICES, initial=5)

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
    
class RatingForm(forms.Form):

    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    comment = forms.CharField(label='Comment:', max_length=500)
    rating = forms.ChoiceField(label='Rating:', choices=RATING_CHOICES, widget=forms.RadioSelect())

    def save(self, post, user):
        cleaned_data = super().clean()
        rating = Rating(
            post=post,
            user=user,
            comment=cleaned_data['comment'],
            rating=cleaned_data['rating'],
        )
        rating.save()
        return rating

