from rest_framework.views import APIView
from rest_framework.response import Response


class TracebackRequest(APIView):
    """ Трассировка GET запросов """
    def get(self, request):
        print(request.headers)
        with open('./dev/request.log', 'w') as file:
            file.write(str(request.headers))

        return Response('halloWelt')