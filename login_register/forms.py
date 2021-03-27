from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(
        label="Email", max_length=100, widget=forms.TextInput(attrs={"oninput":"validateScript('l_email')","id":"l_email","class":"form-control", "type":"email","name":"email"}))

    password = forms.CharField(
        label="Password", max_length=55,widget=forms.TextInput(attrs={"oninput":"validateScript('l_password')","id":"l_password","class":"form-control","type":"password","name": "password"}))

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="First Name", max_length=55, widget=forms.TextInput(attrs={"id":"first_name","class":"form-control","type":"text","name":"first_name" }))
    
    last_name = forms.CharField(
        label="Last Name", max_length=55, widget=forms.TextInput(attrs={"id":"last_name","class":"form-control","type":"text","name":"last_name" }))

    email = forms.CharField(
        label="Email", max_length=55, widget=forms.TextInput(attrs={"id":"email","class":"form-control", "type":"email","name":"email"}))
    
    password = forms.CharField(
        label="Password", max_length=55,widget=forms.TextInput(attrs={"id":"password","class":"form-control","type":"password","name": "password"}))

    confirm_password = forms.CharField(
        label="Confirm Password", max_length=55,widget=forms.TextInput(attrs={"id":"confirm_password","class":"form-control","type":"password","name": "confirm_password"}))
    
    birthday = forms.DateField(
        label="Birthday", widget=forms.DateInput(attrs={"type": "date", "name": "birthday", "id": "birthday", "placeholder": "MM/DD/YYYY"})
    )