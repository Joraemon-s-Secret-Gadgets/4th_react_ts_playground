from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import AnalysisRequestSerializer, AnalysisResponseSerializer

class AnalyzeAuraView(APIView):
    """
    [설계 전용] 이미지 기반 아우라 분석 엔드포인트
    
    프론트엔드에서 업로드한 이미지와 선택된 향기 노트를 받아,
    AI 분석을 거친 후 무드 키워드와 레이더 점수를 반환하는 핵심 엔드포인트입니다.
    """
    @extend_schema(
        request=AnalysisRequestSerializer,
        responses={200: AnalysisResponseSerializer},
        summary="이미지 분석 및 향수 추천 데이터 생성",
        description="Base64 이미지와 3개의 선택 노트를 입력받아 분석 결과를 리턴합니다."
    )
    def post(self, request):
        serializer = AnalysisRequestSerializer(data=request.data)
        if serializer.is_valid():
            # 실제 ML 로직 연동 시 아래 응답 데이터 규격을 준수해야 합니다.
            mock_response = {
                "personalMood": "#현대적 #시크",
                "perfumeKeywords": ["#우디", "#머스크", "#차가운 공기"],
                "fashionStyle": "미니멀리즘 비즈니스 캐주얼",
                "radarScores": {
                    "플로랄": 0.2, "우디": 0.85, "오리엔탈": 0.45, "프레시": 0.65, "구르망": 0.1
                }
            }
            return Response(mock_response, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
