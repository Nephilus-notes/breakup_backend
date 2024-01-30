from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework.response import Response

from .serializers import MoodTrackerEntrySerializer, UserSerializer
from .models import MoodTrackerEntry, User

# Create your views here.

@api_view(['POST'])
def create_profile(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # double check that there are no other users with the same email, auth_id, pk, etc.
        serializer.save()
    return Response()

@api_view(['GET', 'POST', 'DELETE'])
def mood_tracker_entry(request, pk):
    try:
        entry = MoodTrackerEntry.objects.get(pk=pk)
    except MoodTrackerEntry.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = MoodTrackerEntrySerializer(entry)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MoodTrackerEntrySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=204)