''' Configuration View Module
'''
from django.views import View

class ConfigureView(View):
    ''' Configuration View'''
    def get(self):
        ''' Get Request'''
        return '<b>Sample project</b>'