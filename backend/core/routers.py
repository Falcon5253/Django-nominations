from rest_framework.routers import DefaultRouter
from competition.views import CompetitionViewSet, NominationViewSet, WinnerViewSet, ParticipantViewSet, VoteViewSet
from authentication.views import UserViewSet

router = DefaultRouter()

router.register('nomination', NominationViewSet)
router.register('competition', CompetitionViewSet)
router.register('participant', ParticipantViewSet)
router.register('vote', VoteViewSet)
router.register('winner', WinnerViewSet)
router.register('auth', UserViewSet)