''' Configuration View Module
'''
from django.views import View
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from plc_monitor.core.plc import set_plcs
from json.decoder import JSONDecodeError
import json

class ConfigureView(View):
    ''' Configuration View'''

    def get(self, request):
        ''' Get Request'''
        t = get_template('configure.html')
        html = t.render()
        return HttpResponse(html)

    def post(self, request):
        ''' Post request'''
        try:
            data = request.POST
            set_plcs((data['name'], data['ip']))
        except :
            import traceback
            traceback.print_exc()
            return HttpResponse('Error')
        return HttpResponseRedirect('/list')
