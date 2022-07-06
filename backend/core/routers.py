from rest_framework.routers import DefaultRouter
from nominations.views import NominationViewSet
from organizer.views import OrganizerViewSet
from competition.views import CompetitionViewSet
from participant.views import ParticipantViewSet
from votes.views import VotesViewSet
from winners.views import WinnerViewSet
from authentication.views import UserViewSet

router = DefaultRouter()

router.register('nominations', NominationViewSet)
router.register('organizer', OrganizerViewSet)
router.register('competition', CompetitionViewSet)
router.register('participant', ParticipantViewSet)
router.register('votes', VotesViewSet)
router.register('winners', WinnerViewSet)
router.register('auth', UserViewSet)