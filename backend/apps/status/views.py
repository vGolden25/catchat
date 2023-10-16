from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StatusSerializer


@extend_schema(
    responses={
        200: StatusSerializer,
    },
)
@api_view()
def status(request):
    serializer = StatusSerializer(data={"status": "ok"})

    serializer.is_valid(raise_exception=True)

    return Response(serializer.data)
