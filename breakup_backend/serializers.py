
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import MoodTrackerEntry, User

# class MoodTrackerEntrySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = MoodTrackerEntry
#         fields = ['user_id', 'date', 'mood_status', 'days_on_streak', 'last_reset']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['auth_id', 'name', 'email', 'password', 'streak_max', 'streak_starts']

class MoodTrackerEntrySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date = serializers.DateField()
    mood_status = serializers.IntegerField()
    days_on_streak = serializers.IntegerField()
    last_reset = serializers.CharField()

    def create(self, validated_data):
        return MoodTrackerEntry.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.date = validated_data.get('date', instance.date)
        instance.mood_status = validated_data.get('mood_status', instance.mood_status)
        instance.days_on_streak = validated_data.get('days_on_streak', instance.days_on_streak)
        instance.last_reset = validated_data.get('last_reset', instance.last_reset)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

    def read(self, instance):
        instance.read()