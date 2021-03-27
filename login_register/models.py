from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import datetime
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}

        present = datetime.now()

        # convert to datetime format
        birthday_dt_obj = datetime.strptime(post_data["birthday"], '%Y-%m-%d')

        time_difference = relativedelta(present, birthday_dt_obj)
        difference_in_years = time_difference.years

        # empty list is False
        email = User.objects.filter(email=post_data["email"])
        
        if len(post_data["first_name"]) < 2:
            errors["first_name"] = "First name must be at least 2 characters long."
        if len(post_data["last_name"]) < 2:
            errors["last_name"] = "Last name must be at least 2 characters long."
        if not "@" in post_data["email"]:
            errors["email"] = "Email must be valid format."
        if len(post_data["password"]) < 8:
            errors["password"] = "Password must be at least 8 characters long."
        if post_data["password"] != post_data["confirm_password"]:
            errors["pw_mismatch"] = "Passwords do not match. Please make sure passwords match."
        if email:
            errors["user_exists"] = "A user with this email already exists. Please log in."
        if birthday_dt_obj >= present:
            errors["birthday"] = "Birthday cannot be in the future."
        if difference_in_years < 13:
            errors["age"] = "You must be at least 13 years old to register."
        return errors
    
    def login_validator(self, post_data):
        errors = {}

        user = User.objects.filter(email=post_data['email'])

        if user:
            [user] = user
            # check for password match
            password_match = bcrypt.checkpw(post_data['password'].encode('utf-8'), user.password.encode('utf-8'))

            if not password_match:
                errors["inc_password"] = "Password is incorrect."
        
        if not user:
            errors["not_exists"] = "User does not exist. Please register."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
