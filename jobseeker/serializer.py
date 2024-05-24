from django.http import JsonResponse
from django.core.serializers import serialize
import json


class SerializerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the response is a Django queryset
        if hasattr(response, 'data'):
            # Serialize the response data using Django's serialize function
            serialized_data = serialize('json', response.data)
            # Convert serialized data to JSON
            json_data = json.loads(serialized_data)
            # Create a JSON response with the serialized data
            response = JsonResponse(json_data, safe=False)

        return response
