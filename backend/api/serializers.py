from rest_framework import serializers

class AnalysisRequestSerializer(serializers.Serializer):
    image = serializers.CharField(help_text="이미지 Base64 문자열")
    selectedNotes = serializers.ListField(
        child=serializers.CharField(),
        help_text="사용자가 선택한 향기 노트 리스트"
    )

class AnalysisResponseSerializer(serializers.Serializer):
    personalMood = serializers.CharField()
    perfumeKeywords = serializers.ListField(child=serializers.CharField())
    fashionStyle = serializers.CharField()
    radarScores = serializers.DictField(child=serializers.FloatField())
