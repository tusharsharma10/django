# yourapp/exceptions.py

from django.http import JsonResponse


class BadRequestException(Exception):
    pass


def customExceptionHandler(get_response):
    def middleware(request):
        try:
            response = get_response(request)
        except BadRequestException as ex:
            # Handle BadRequestException by returning a JSON response with status code 400
            return JsonResponse({'error': str(ex)}, status=400)
        except Exception as ex:
            # Handle other exceptions by returning a JSON response with status code 500
            return JsonResponse({'error': 'An unknown error occurred'}, status=500)

        return response

    return middleware
