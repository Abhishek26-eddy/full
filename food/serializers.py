from rest_framework import serializers
from .validators import is_present
from .models import Skills, Profile


class ProfileSerializer(serializers.ModelSerializer):
    # skill_name = serializers.CharField(source='skill_name.skill_name')
    # skill_count = serializers.CharField(required=True, read_only=False)
    class Meta:
        model = Profile
        fields = ('name', 'skill_name', 'skill_count')

        extra_kwargs = {
            'skill_count':{'required':True}
        }

    # def get_skill_count(self, obj):
    #     return obj.Skills.count()


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = '__all__'
