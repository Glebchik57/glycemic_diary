from django.shortcuts import render
from rest_framework import viewsets

from glecemic_diary.diary.models import Diary, Note
from glecemic_diary.diary.serializers import DiarySerializer, NoteSerializer


class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
