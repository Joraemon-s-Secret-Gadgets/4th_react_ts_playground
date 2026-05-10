from django.urls import path
from .views import AnalyzeAuraView

urlpatterns = [
    path('analyze/', AnalyzeAuraView.as_view(), name='analyze-aura'),
]
