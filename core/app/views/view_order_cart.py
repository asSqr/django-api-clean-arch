from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from drf_yasg.utils import swagger_auto_schema


from ..serializers.serializer_order_cart import CreateOrderCartSerializer
from ...domain.use_cases.order_cart import CreateOrderCartUseCase


class CreateOrderCartAPIView(APIView):
    """ Olá """
    @swagger_auto_schema(request_body=CreateOrderCartSerializer)
    def post(self, request):
        use_case = CreateOrderCartUseCase()
        response = use_case.execute()


class GetListOrderCartAPIView(ListAPIView):
    """Ola """
    def get(self, request):
        pass
