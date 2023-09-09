from django.core.cache import cache
from django.shortcuts import render
import logging
from rest_framework.views import APIView
import requests

logger = logging.getLogger(__name__) #playground.views

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('Httpbin is offline')
        return render(request, 'hello.html', {'name': 'Mosh'})