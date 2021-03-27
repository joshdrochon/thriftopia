from django.db import models
from login_register.models import User

class Class(models.Model):
    name = models.CharField(max_length=55)
    character = models.CharField(max_length=55, default="")
    intelligence = models.IntegerField()
    luck = models.IntegerField()
    cunning = models.IntegerField()
    desc = models.TextField(default="")
    img_path = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    rarity = models.CharField(max_length=15)
    worth = models.IntegerField()
    condition = models.CharField(max_length=55, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Player(models.Model):
    p_class = models.ForeignKey(Class, related_name="players", on_delete=models.CASCADE)
    wealth = models.IntegerField(default=0)
    morale = models.IntegerField(default=50)
    energy = models.IntegerField(default=100)
    experience = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    user = models.ForeignKey(User, related_name="players", on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

rarity = ["trivial", "common", "rare" "extraordinary", "legendary"]
conditions = ["poor", "fair", "good", "gently-used", "like-new",]






