from django.db.models import F
from django.utils import timezone
from .models import PageHit


class PageHitsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.process_page_hits(request)
        return response

    @staticmethod
    def process_page_hits(request):
        today = timezone.datetime.today()
        page_hit, created = PageHit.objects.get_or_create(
            url=request.path, visit_date=today
        )
        if request.user.is_authenticated:
            page_hit.registered_hits = F("registered_hits") + 1
        else:
            page_hit.anonymous_hits = F("anonymous_hits") + 1
        page_hit.save()
