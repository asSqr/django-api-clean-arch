from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


class CreateBookAPIView(APIView):
    @swagger_auto_schema()
    def post(self, request):
        return {f'{self}': f'{request}'}
