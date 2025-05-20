from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from .models import InterviewVideo
from rest_framework.generics import ListAPIView
from .serializers import InterviewVideoSerializer
from rest_framework.decorators import api_view

class InterviewUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        video_file = request.FILES.get('video')
        email = request.data.get('email')

        if not video_file:
            return Response({"error": "No video provided"}, status=400)

        # Save video and email
        interview = InterviewVideo.objects.create(video=video_file, email=email)

        # Convert to mp4 and analyze (includes face + emotion analysis)
        converted_path = interview.convert_webm_to_mp4()
        if converted_path:
            interview.analyze_video()

        return Response({
            "message": "Video uploaded and analyzed",
            "total_frames": interview.total_frames,
            "face_frames": interview.face_frames,
            "score": interview.score
        })


@api_view(['GET'])
def check_analysis_status(request, video_id):
    try:
        video = InterviewVideo.objects.get(pk=video_id)
        return Response({
            "analyzed": video.analyzed,
            "total_frames": video.total_frames,
            "face_frames": video.face_frames
        })
    except InterviewVideo.DoesNotExist:
        return Response({"error": "Video not found"}, status=404)


class InterviewReportListView(ListAPIView):
    queryset = InterviewVideo.objects.filter(analyzed=True).order_by('-id')
    serializer_class = InterviewVideoSerializer
