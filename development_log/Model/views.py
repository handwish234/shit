from django.core import serializers
from django.http import JsonResponse
from .models import LoginParams
import json

def get_LoginParams_data(request):
    LoginParams_data = LoginParams.objects.all()
    serialized_data = serializers.serialize('json', LoginParams_data)
    deserialized_data = json.loads(serialized_data)

    # 构建整齐的 JSON 数据格式
    data = []
    for item in deserialized_data:
        fields = item['fields']
        formatted_item = {
            'username': fields['username'],
            'password': fields['password'],
            'autoLogin': fields['autoLogin'],
            'type': fields['type'],
        }
        data.append(formatted_item)
    
    result1 = {
        'data': data,
        "success": True,
        "errorMessage":" ",
    }

    result2 = {
        'data': {},
        "success": False,
        "errorMessage":"Data error",
    }

    try:
        response = JsonResponse(result1, safe=False)
    except:
        response = JsonResponse(result2, safe=False)

    # 添加 CORS 头
    response["Access-Control-Allow-Origin"] = "*"

    return response