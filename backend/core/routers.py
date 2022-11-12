from rest_framework.routers import DefaultRouter
from nomination.views import NominationViewSet
from competition.views import CompetitionViewSet
from participant.views import ParticipantViewSet
from vote.views import VoteViewSet
from comp_winner.views import CompWinnerViewSet
from authentication.views import UserViewSet

router = DefaultRouter()

router.register('nomination', NominationViewSet)
router.register('competition', CompetitionViewSet)
router.register('participant', ParticipantViewSet)
router.register('vote', VoteViewSet)
router.register('comp_winner', CompWinnerViewSet)
router.register('auth', UserViewSet)