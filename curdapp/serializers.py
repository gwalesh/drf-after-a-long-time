from django.contrib.auth.models import User, Group
from .models import Test, Question, Option
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test 
        fields = ['title', 'slug']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'slug', 'thumbnail', 'test_id']

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ['option', 'question_id']