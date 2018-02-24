# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View

from .utils.news import get_news_for_country
from .utils.safety import get_country_safety_stats


def country_info(country):
    #todo index news and safety on separate threads
    country_info = {}
    country_info['name'] = country
    country_info['news'] = get_news_for_country(country)
    country_info['safety'] = get_country_safety_stats(country)
    return country_info


class api(View):
    def get(self, request,*args, **kwargs):
        country = self.kwargs.get('country')
        return JsonResponse(country_info(country))
