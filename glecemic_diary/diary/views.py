from django.shortcuts import render
from rest_framework import viewsets

from .models import Diary, Note
from .serializers import DiarySerializer, NoteSerializer


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
