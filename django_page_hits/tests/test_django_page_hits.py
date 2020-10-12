#!/usr/bin/env python

"""Tests for `django_page_hits` package."""
from django.test import TransactionTestCase
from django.utils import timezone

from .MockRequest import MockRequest
from django_page_hits.models import PageHit
from django_page_hits.middleware import PageHitsMiddleware

HOME_ADDR = '/'
SUB_ADDR = '/sub'


class TestAuthenticatedVisit(TransactionTestCase):

    def setUp(self):
        self.home_request = MockRequest(HOME_ADDR, True)
        self.sub_path = MockRequest(SUB_ADDR, True)

    def test_middleware(self):
        today = timezone.datetime.today()
        PageHitsMiddleware.process_page_hits(self.home_request)
        PageHitsMiddleware.process_page_hits(self.home_request)
        PageHitsMiddleware.process_page_hits(self.sub_path)
        home_request = PageHit.objects.get(visit_date=today, url=HOME_ADDR)
        sub_request = PageHit.objects.get(visit_date=today, url=SUB_ADDR)
        self.assertEqual(sub_request.registered_hits, 1)
        self.assertEqual(home_request.registered_hits, 2)


class TestUnAuthenticatedVisit(TransactionTestCase):

    def setUp(self):
        self.home_request = MockRequest(HOME_ADDR, False)
        self.sub_path = MockRequest(SUB_ADDR, False)

    def test_middleware(self):
        today = timezone.datetime.today()
        PageHitsMiddleware.process_page_hits(self.home_request)
        PageHitsMiddleware.process_page_hits(self.home_request)
        PageHitsMiddleware.process_page_hits(self.sub_path)
        home_request = PageHit.objects.get(visit_date=today, url=HOME_ADDR)
        sub_request = PageHit.objects.get(visit_date=today, url=SUB_ADDR)
        self.assertEqual(sub_request.anonymous_hits, 1)
        self.assertEqual(home_request.anonymous_hits, 2)
