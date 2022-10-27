from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(["GET"])
def home(request, *args, **kwargs):
  data = {
    "slackUsername":"Nageri.Cedric",
    "backend":true,
    "age": 25,
    "bio":"Backend developer, ready to change the world of data, by providing seamless solutions"
  }
  return JsonResponse(data)