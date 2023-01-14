from rest_framework.routers import DefaultRouter
from competition.views import CompetitionViewSet, NominationViewSet, WinnerViewSet, ParticipantViewSet, VoteViewSet
from authentication.views import ProfileViewSet
from django.contrib.auth import views as AuthViews
from django.urls import path

router = DefaultRouter()

router.register('nomination', NominationViewSet)
router.register('competition', CompetitionViewSet)
router.register('participant', ParticipantViewSet)
router.register('vote', VoteViewSet)
router.register('winner', WinnerViewSet)
router.register('auth', ProfileViewSet)

app_name = 'rest_framework'
urlpatterns = [
    path('auth/login/', AuthViews.LoginView.as_view(template_name='login.html'), name='login', ),
    path('auth/logout/', AuthViews.LogoutView.as_view(), name='logout'),
]