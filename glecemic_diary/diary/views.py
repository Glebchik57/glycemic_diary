from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Diary, Note
from .serializers import DiarySerializer, NoteSerializer


class DiaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

    def get_queryset(self):
        return Diary.objects.filter(patient=self.request.user)

    @action(methods=['get'], detail=False)
    def read_all_patient_diary_by_guest(self):
        diaries = Diary.objects.filter(patient__in=self.request.user.patients)
        serializer = DiarySerializer(diaries, many=True)
        return Response(serializer.data)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
