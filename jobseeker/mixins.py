
from django.http import JsonResponse

class ValidateQueryParamsMixin:
    def dispatch(self, request, *args, **kwargs):
        param = request.GET.get('param')
        if not param:
            return JsonResponse({'error': 'The "param" query parameter is required.'}, status=400)
        if not param.isdigit():
            return JsonResponse({'error': 'The "param" query parameter must be a number.'}, status=400)
        return super().dispatch(request, *args, **kwargs)



# # yourapp/views.py
#
# from django.views import View
# from .mixins import ValidateQueryParamsMixin
#
# class MyView(ValidateQueryParamsMixin, View):
#     def get(self, request, *args, **kwargs):
#         param = request.GET.get('param')
#         return JsonResponse({'message': f'Valid param: {param}'})
