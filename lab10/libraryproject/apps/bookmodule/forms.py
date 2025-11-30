from django import forms

from apps.bookmodule import models

class AdditBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'edition', 'price']
        title = forms.CharField(
            max_length=200,
            required=True,
            label='Book Title',
            widget=forms.TextInput(attrs={
                'placeholder': 'Enter book title'
            })
        )
        author = forms.CharField(
            max_length=100,
            required=True,
            label='Author',
            widget=forms.TextInput(attrs={
                'placeholder': 'Enter author name'
            })
        )
        edition = forms.IntegerField(
            max_value=100,
            required=True,
            label='Edition',
            widget=forms.NumberInput(attrs={
                'placeholder': 'Enter book edition'
            })
        )
        price = forms.FloatField(
            max_value=10000.00,
            required=True,
            label='Price',
            widget=forms.NumberInput(attrs={
                'placeholder': 'Enter book price'
            })
        )

class DeleteBookForm(forms.Form):
    confirm = forms.BooleanField(label='Confirm Deletion')