
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import MoodTrackerEntry, User, Post, Comment

# class MoodTrackerEntrySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = MoodTrackerEntry
#         fields = ['user_id', 'date', 'mood_status', 'days_on_streak', 'last_reset']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['auth_id', 'name', 'email', 'password', 'streak_max', 'streak_starts', "support_info", "struggles_info", "tutorial_in_progres", "id"]

class MoodTrackerEntrySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date = serializers.DateField()
    content = serializers.CharField()
    mood_status = serializers.IntegerField()
    days_on_streak = serializers.IntegerField()
    last_reset = serializers.DateTimeField()

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

class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date = serializers.DateField()
    content = serializers.CharField()
    likes = serializers.IntegerField()
    comments = serializers.JSONField()
    tags = serializers.JSONField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.date = validated_data.get('date', instance.date)
        instance.content = validated_data.get('content', instance.content)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

    def read(self, instance):
        instance.read()

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    date = serializers.DateField()
    content = serializers.CharField()
    likes = serializers.IntegerField()
    tags = serializers.JSONField()

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.post_id = validated_data.get('post_id', instance.post_id)
        instance.date = validated_data.get('date', instance.date)
        instance.content = validated_data.get('content', instance.content)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

    def read(self, instance):
        instance.read()