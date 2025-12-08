from django import forms
from apps.bookmodule import models
from django.contrib.admin.widgets import FilteredSelectMultiple

class AddressChoiceField(forms.ModelChoiceField):
            def label_from_instance(self, obj):
                return obj.city # pyright: ignore[reportAttributeAccessIssue]

class AdditstuForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['name', 'age', 'address']
        field_classes = {
            'address': AddressChoiceField
        }
        name = forms.CharField(
            max_length=200,
            required=True,
            label='Student Name',
            widget=forms.TextInput(attrs={
                'placeholder': 'Enter student name'
            })
        )
        age = forms.IntegerField(
            min_value=0,
            required=True,
            label='Student Age',
            widget=forms.NumberInput(attrs={
                'placeholder': 'Enter student age'
            })
        )
        

        address = AddressChoiceField(
            queryset=models.Address.objects.all(),
            required=True,
            empty_label=None,
            label='Student Address'
        )

class DeleteStudentForm(forms.Form):
    confirm = forms.BooleanField(label='Confirm Deletion')

class AddressChoiceField2(forms.ModelMultipleChoiceField):
            def label_from_instance(self, obj):
                return obj.city # pyright: ignore[reportAttributeAccessIssue]
 
class AdditstuForm2(forms.ModelForm):
    address = AddressChoiceField2(
        queryset=models.Address2.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    class Meta:
        model = models.Student2
        fields = ['name', 'age', 'address']