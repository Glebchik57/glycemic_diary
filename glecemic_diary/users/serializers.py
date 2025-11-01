from rest_framework import serializers

from diary.serializers import DiarySerializer
from .models import Patient, Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = (
            'name',
            'surname',
            'email',
            'patients'
        )


class PatientSerializer(serializers.ModelSerializer):
    diary = DiarySerializer()
    guests = GuestSerializer(many=True)
    class Meta:
        model = Patient
        fields = (
            'name',
            'surname',
            'email',
            'insulin',
            'diary',
            'guests'
        )
