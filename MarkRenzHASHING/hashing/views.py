from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import hashlib
import json

def home_view(request):
    return render(request, 'home.html')


def md5_hash(message):
    md5_object = hashlib.md5()
    md5_object.update(message.encode('utf-8'))
    return md5_object.hexdigest()

@csrf_exempt
def hash_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')
        hash_value = md5_hash(message)
        return JsonResponse({'hash': hash_value})
    return JsonResponse({'error': 'Invalid request'}, status=400)
