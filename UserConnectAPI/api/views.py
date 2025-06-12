from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

# Public endpoint
class PublicAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Hello, this is a public endpoint!"})


# Protected endpoint
class ProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({"message": f"Welcome {user.username}, this is a protected endpoint!"})
