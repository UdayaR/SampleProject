''' List View module'''
from django.views import View
from django.http.response import HttpResponse
from django.template.loader import get_template
from plc_monitor.core.plc import get_plcs

class ListView(View):
    ''' List View'''

    def get(self, request):
        ''' Get Request'''
        t = get_template('list.html')
        html = t.render({'plcs': get_plcs()})
        return HttpResponse(html)
