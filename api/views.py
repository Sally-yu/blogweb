import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
# We're using `django_ajax.middleware.AJAXMiddleware` in settings
# so we don't need to use `@ajax` and `AJAXMixin` decorators


# JsonResponse without safe
from api.models import News


def CusResponse(data, safeOrNot=False):
    return JsonResponse(data, safe=safeOrNot)

# allnews
def allNews(request):
    if request.method == 'GET':
        datatable = News.objects.all().filter()
        jsonData = serializers.serialize('json', datatable)
        print('allnews')
        context = {
            'data': jsonData,
        }
        return CusResponse(context)
    else:
        return HttpResponse('Unsupport method,please use GET')


# news
def news(request, id):
    if request.method == 'GET':
        datatable = News.objects.all().filter()
        jsonData = serializers.serialize('json', datatable)
        print('id=', id)
        context = {
            'data': jsonData,
        }
        return CusResponse(context)
    else:
        return HttpResponse('Unsupport method,please use GET')


def postTest(request):
    if request.method == 'POST':
        print('POST')
        jsonData = json.loads(request.body)  # 获取post的json，dict类型
        print(jsonData)
        print(jsonData['username'])
        print(jsonData['password'])
        return HttpResponse('23d23')
    else:
        return HttpResponse('Unsupport method,please use POST')


def saveNews(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        print(jsonData)
