# backend/interview/serializers.py
from rest_framework import serializers
from .models import InterviewVideo

class InterviewVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewVideo
        fields = '__all__'
        #fields = ['id', 'video', 'converted_video', 'total_frames', 'face_frames', 'score', 'analyzed', 'email']
