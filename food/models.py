from django.db import models
from django.db.models.signals import post_delete
# Create your models here.

class Skills(models.Model):
    skill_name = models.CharField(max_length=20, primary_key=True)
    another = models.CharField(max_length=20)

    def __str__(self):
        return self.skill_name
    

class Profile(models.Model):
    name = models.CharField(max_length=30)
    skill_name = models.OneToOneField(Skills, on_delete=models.CASCADE)

    @property
    def skill_count(self):
        return self.skill_name.count

def delete_parent(sender, instance, **kwargs):
    if instance.skill_name:
        instance.skill_name.delete()

post_delete.connect(delete_parent, sender=Profile)