# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import threading
import timeit

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import View

#from .utils.news import get_news_for_country
#from .utils.safety import get_country_safety_stats
from service.utils.news import get_news_for_country
from service.utils.safety import get_country_safety_stats

def country_info(country):
    #todo index news and safety on separate threads
    country_info = {}
    country_info['name'] = country
    country_info['news'] = get_news_for_country(country)
    country_info['safety'] = get_country_safety_stats(country)
    return country_info


def country_ju(country):
    #todo index news and safety on separate threads

    country_info = {}
    country_info['name'] = country
    #todo threading still fails
    safety_thred = threading.Thread(target=get_country_safety_stats, args=(country))
    news_thread = threading.Thread(target=get_news_for_country, args=(country))
    country_info['news'] = news_thread.start()#get_news_for_country(country)
    country_info['safety'] =  safety_thred.start()#get_country_safety_stats(country)
    return country_info


class api(View):
    def get(self, request,*args, **kwargs):
        country = self.kwargs.get('country')
        return JsonResponse(country_info(country))


class web(View):
    def get(self, request, *args, **kwargs):
        country = self.kwargs.get('country')
        context = {
         'name': country,
        'news':  get_news_for_country(country),
        'safety': get_country_safety_stats(country)

        }
        return render(request, "post_list.html", context)


if __name__ == "__main__":
    nigeria ="nigeria"
    print(timeit.timeit("country_info(nigeria)", number=2, globals=globals()))
    print(timeit.timeit("country_ju(nigeria)", number=2, globals=globals()))