from django import forms

class SearchForm(forms.Form):
    subreddit_name = forms.CharField(label='Subreddit Name', max_length=200)