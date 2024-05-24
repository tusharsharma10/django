from django.http import JsonResponse
from functools import wraps

from jobseeker.exceptions import BadRequestException


validUserTypes = ['R','J']
def validateResId(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        param = request.headers['resId']
        if not param:
            return JsonResponse({'error': 'resId is required'}, status=400)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def validateFolderId(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            param = request.query_params['folderId']
            if not param:
                return JsonResponse({'error': 'folderId is required'}, status=400)
        except Exception as ex:
             return JsonResponse({'error': 'folderId is required'}, status=400)
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def validateUserType(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):


        try:
            param = request.query_params['userType']
            if not param:
                return JsonResponse({'error': 'User type is required'}, status=400)
            if param not in validUserTypes:
                return JsonResponse({'error': 'User type should be either R, J'}, status=400)
        except Exception as ex:
            return JsonResponse({'error': 'User type is required'}, status=400)

        return view_func(request, *args, **kwargs)

    return _wrapped_view