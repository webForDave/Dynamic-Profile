from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MySerializer
from rest_framework import status
import requests
import datetime

@api_view(["GET"])
def my_information(request):

    my_data = {
        "email": "dakinola54@gmail.com",
        "name": "Akinola David",
        "stack": "Python/Django"
    }

    def get_cat_fact():
        response = requests.get("https://catfact.ninja/fact")

        if response.status_code == 200:
            return response.json()
        else:
            return "Error fetching cat fact"
    
    serializer = MySerializer(instance=my_data)
    cat_fact = get_cat_fact()["fact"]
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"

    return Response(data={
        "status": "success", 
        "user": serializer.data, 
        "timestamp": timestamp, 
        "fact": cat_fact
        }, status=status.HTTP_200_OK)