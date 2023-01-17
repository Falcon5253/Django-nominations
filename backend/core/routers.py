from rest_framework.routers import DefaultRouter, APIRootView
from competition.views import CompetitionViewSet, NominationViewSet, WinnerViewSet, ParticipantViewSet, VoteViewSet
from authentication.views import ProfileViewSet
from django.contrib.auth import views as AuthViews
from django.urls import path
from collections import OrderedDict
from django.urls import NoReverseMatch
from rest_framework.response import Response
from rest_framework.reverse import reverse


class listOfUrlsView(APIRootView):
    def get(self, request, *args, **kwargs):
        ret = OrderedDict()
        namespace = request.resolver_match.namespace
        for key, url_name in self.api_root_dict.items():
            if namespace:
                url_name = namespace + ':' + url_name
            try:
                ret[key] = reverse(
                    url_name,
                    args=args,
                    kwargs=kwargs,
                    request=request,
                    format=kwargs.get('format')
                )
            except NoReverseMatch:
                # Don't bail out if eg. no list routes exist, only detail routes.
                continue
            
        ret["myUrl"] = "http://httpbin.com"
        return Response(ret)
        
    
    

class myRouter(DefaultRouter):
    APIRootView = listOfUrlsView
    root_view_name = "list-of-urls"

router = myRouter()

router.register('nomination', NominationViewSet)
router.register('competition', CompetitionViewSet)
router.register('participant', ParticipantViewSet)
router.register('vote', VoteViewSet)
router.register('winner', WinnerViewSet)
router.register('auth', ProfileViewSet)

app_name = 'rest_framework'
urlpatterns = [
    path('auth/login/', AuthViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('auth/logout/', AuthViews.LogoutView.as_view(), name='logout'),
]