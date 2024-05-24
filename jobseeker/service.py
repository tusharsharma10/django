# yourapp/views.py

from django.http import JsonResponse

from .decorators import validateResId, validateFolderId, validateUserType
from .exceptions import BadRequestException

validUserTypes = ['R', 'J']


def validateUserTypes(userType, *args, **kwargs):
    if userType is None or not userType in validUserTypes:
        raise BadRequestException('User type should be either R, J')


class JobeekerService(object):
    def __init__(self, dependency=None):
        self.dependency = dependency

    @staticmethod
    @validateResId
    @validateFolderId
    @validateUserType
    def getCount(request):
        daysOld = JobeekerService.daysOld(request.GET)
        resId = request.GET.get('resId')
        userType = request.GET.get('userType')
        folderId = request.GET.get('folderId')
        print()
        distinctCountList = JobeekerService.getDistinctCountByLabels(resId,userType,folderId,daysOld)
        return JsonResponse(data={'countList':distinctCountList},status=200)

    @staticmethod
    def daysOld(param):
        if param.get('daysOld') is not None:
            return param.get('daysOld')
        else:
            return 200

    @staticmethod
    def getDistinctCountByLabels(resId,userType,folderId,daysOld):
        return []