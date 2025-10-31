from rest_framework import serializers
from models import Diary, Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'date',
            'glycemic_level',
            'insulin_injection_count',
            'comment'
        )


class DiarySerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Diary
        fields = (
            'patient',
            'date',
            'notes'
        )
