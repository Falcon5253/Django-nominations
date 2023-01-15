from rest_framework.renderers import BrowsableAPIRenderer

class myApiRenderer(BrowsableAPIRenderer):
    template =  'api.html'