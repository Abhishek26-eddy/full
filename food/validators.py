

from rest_framework.validators import ValidationError
from .models import Skills

def is_present(value):
    skills = Skills.objects.all()

    if value in skills:
        pass
    else:
        raise ValidationError('You cannot add this skill!')
