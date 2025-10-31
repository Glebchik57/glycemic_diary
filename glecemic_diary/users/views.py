from rest_framework import viewsets

from glecemic_diary.users.models import Patient, Guest
from glecemic_diary.users.serializers import PatientSerializer, GuestSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
