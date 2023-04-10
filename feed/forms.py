from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from feed.models import Post 


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
    title = forms.CharField(label='Title:', max_length=100)
    price = forms.IntegerField(label = 'Price:')
    start_loc = forms.CharField(label = 'Origin:', max_length=100)
    end_loc = forms.CharField(label = 'Destination', max_length=100)
    expiration_date = forms.DateTimeField(label = 'Delivery window:')
    time_estimate = forms.DurationField(label = 'ETA:')
    #created_at = forms.DateTimeField(auto_now_add=True)
    status = forms.CharField(label = 'Order Status', max_length=20)

    def save(self, user, commit=True):
        cleaned_data = super().clean()
        post = Post(
            title=cleaned_data['title'],
            price=cleaned_data['price'],
            start_loc=cleaned_data['start_loc'],
            end_loc=cleaned_data['end_loc'],
            expiration_date=cleaned_data['expiration_date'],
            time_estimate=cleaned_data['time_estimate'],
            status=cleaned_data['status'],
            user=user
        )
        post.save()
        return post
