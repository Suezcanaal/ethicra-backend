from django.urls import path
from .views import InterviewUploadView, check_analysis_status, InterviewReportListView

urlpatterns = [
    path("upload/", InterviewUploadView.as_view(), name="upload"),
    path("status/<int:video_id>/", check_analysis_status, name="status"),
    path("reports/", InterviewReportListView.as_view(), name="reports"),  # This is what was missing
]
