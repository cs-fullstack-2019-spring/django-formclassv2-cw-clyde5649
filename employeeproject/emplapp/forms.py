from django import forms


class EmployeeApplication(forms.Form):
    name = forms.CharField(max_length=50)
    birthday = forms.DateTimeField()
    applying = forms.CharField(max_length=200)
    salary = forms.IntegerField(max_value=100)
