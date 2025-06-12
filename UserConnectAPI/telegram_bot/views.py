from rest_framework.views import APIView
from rest_framework.response import Response
from .bot import handle_start_command

class TriggerBotView(APIView):
    def get(self, request):
        handle_start_command()
        return Response({"message": "Bot executed!"})
