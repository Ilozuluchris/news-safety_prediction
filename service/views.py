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
from django.http import HttpResponseRedirect,HttpResponse
class index(View):
  def get(self, request, *args, **kwargs):
      countries_list = ['a','b']
      context = {
                'countries_list': countries_list
      }
      return render(request,'index.html', context)

class web(View):
    def get(self, request, *args, **kwargs):
        print(request)
        country = self.kwargs.get('country')
        # context = {
        #  'name': country,
        # 'news':  get_news_for_country(country),
        # 'safety': get_country_safety_stats(country)
        #
        # }
        context = {
  "name": "nigeria",
  "news": [
    {
      "urlToNewsArticle": "https://independent.ng/nde-trains-2500-idps-skill-acquisition-adamawa/",
      "title": "NDE Trains 2500 IDPs On Skill Acquisition In Adamawa",
      "description": "No fewer than 2,500 Internally Displaced Person (IDPs) in Adamawa state has been penciled down to commence training on skill acquisition by the National Directorate of Employment (NDE).",
      "image": "https://independent.ng/wp-content/uploads/2018/02/IDPs-1.jpg"
    },
    {
      "urlToNewsArticle": "https://theeagleonline.com.ng/saraki-obaseki-stakeholders-vow-action-to-end-human-trafficking/",
      "title": "Saraki, Obaseki, stakeholders vow action to end human trafficking",
      "description": "The stakeholders included the Minister of Interior, Abduraman Dambazzau; the European Union; United Kingdom; International Organization on Migration; the National Agency for the Prohibition on Trafficking in Persons; and Civil Society Organizations.",
      "image": "https://theeagleonline.com.ng/wp-content/uploads/2017/06/Bukola-Saraki1-e1498207935309.jpg"
    },
    {
      "urlToNewsArticle": "https://www.vanguardngr.com/2018/02/investigate-dapchi-girls-abduction-now-pdp-tasks-national-assembly/",
      "title": "Investigate Dapchi girls' abduction now, PDP tasks National Assembly",
      "description": "-The Peoples Democratic Party (PDP) Monday urged the National Assembly to as a matter of urgent national importance, open a full scale investigation into the circumstances leading to and surrounding the unfortunate abduction of 110 school girls in Dapchi, Yob…",
      "image": "https://cdn.vanguardngr.com/wp-content/uploads/2018/02/000_10W31H.jpg"
    },
    {
      "urlToNewsArticle": "https://www.vanguardngr.com/2018/02/groups-urge-fg-immortalise-nwobodo-mbakwe-obi/",
      "title": "Groups urge FG to immortalise Nwobodo, Mbakwe, Obi",
      "description": "IN line with promoting quality leadership and good governance in the Southeast zone of Nigeria, some groups have requested  that the trio of Chief Jim Nwobodo, governor of old Anambra State; late Chief Sam Mbakwe, governor of Imo State and Chief Peter Obi, fo…",
      "image": "https://cdn.vanguardngr.com/wp-content/uploads/2017/11/mighty-igbo.jpg"
    },
    {
      "urlToNewsArticle": "https://www.vanguardngr.com/2018/02/women-group-seeks-promotion-igbo-language-culture/",
      "title": "Women group seeks promotion of Igbo language, culture",
      "description": "UMUADA IGBO Nigeria and  Diaspora, an Igbo gender socio-cultural group has sworn that they will never allow Igbo language and culture go into extinction.",
      "image": "https://cdn.vanguardngr.com/wp-content/uploads/2018/02/Enugu1.png"
    },
    {
      "urlToNewsArticle": "https://www.vanguardngr.com/2018/02/islamic-cleric-docked-alleged-defamation-inciting-disturbance/",
      "title": "Islamic cleric docked for alleged defamation, inciting disturbance",
      "description": "An Ilorin-based Islamic cleric, Wasiu Jaguma, was on Monday arraigned in an Ilorin Magistrates’ Court on a two-count charge of defamation of character and inciting disturbance.",
      "image": "https://cdn.vanguardngr.com/wp-content/uploads/2017/12/Muslim-faithful1c.jpg"
    },
    {
      "urlToNewsArticle": "https://theeagleonline.com.ng/tricycle-riders-burn-frsc-vehicle-injure-six-in-jos/",
      "title": "Tricycle riders burn FRSC vehicle, injure six in Jos",
      "description": "Andrew Bala, the command’s Public Education Officer, confirmed the incident to the News Agency of Nigeria in Jos.",
      "image": "https://theeagleonline.com.ng/wp-content/uploads/2018/02/FRSC-LOGO-2.jpg"
    },
    {
      "urlToNewsArticle": "http://saharareporters.com/2018/02/26/n19bn-money-laundering-suit-efcc-tells-court-not-unfreeze-shagayas-account",
      "title": "N1.9bn Money Laundering Suit: EFCC Tells Court Not To Unfreeze Shagaya's Account",
      "description": "The Economic and Financial Crimes Commission on Monday urged a Federal High Court sitting in Lagos not to unfreeze a Unity Bank account with a balance of N1,902,673,399.93 belonging to socialite and businesswoman, Hajiya Bola Shagaya. The anti-graft agency cl…"
    },
    {
      "urlToNewsArticle": "https://www.businessdayonline.com/fg-announce-new-national-minimum-wage-end-q3-ngige/",
      "title": "FG to announce new national minimum wage before end of Q3 -Ngige",
      "description": "Federal Government has assured Nigerian workers of its resolve to conclude negotiations on the new national minimum wage before the end of the third quarter of 2018. Chris Ngige, Minister of Labour and Employment, gave the assurance in Abuja, during the openi…",
      "image": "https://www.businessdayonline.com/wp-content/uploads/2018/02/Chris-Ngige-2.jpg"
    },
    {
      "urlToNewsArticle": "https://www.vanguardngr.com/2018/02/will-continue-defend-buhari-abdullahi-adamu/",
      "title": "I will continue to defend Buhari – Abdullahi Adamu",
      "description": "The Senator representing Nasarawa West in the National Assembly, Senator Abdullahi Adamu has said that he would always continue to defend President Muhammadu Buhari and his administration.",
      "image": "https://cdn.vanguardngr.com/wp-content/uploads/2018/02/Abdullahi-Adamu.jpg"
    },
    {
      "urlToNewsArticle": "https://www.vanguardngr.com/2018/02/breaking-ex-briafan-solder-col-joseph-achuzie-hannibal-dies-90/",
      "title": "Breaking: Ex-Briafan solder, Col. Joseph Achuzie '' Hannibal '' dies at 90",
      "description": "Breaking: Ex-Briafan solder, Col. Joseph  Achuzie ‘’ Hannibal ‘’  dies at 90",
      "image": "https://cdn.vanguardngr.com/wp-content/uploads/2011/11/Achuzie.jpg"
    },
    {
      "urlToNewsArticle": "https://www.thecable.ng/buhari-chair-apc-nec-meeting-party-prepares-first-convention-since-2014",
      "title": "Buhari to chair APC NEC meeting as party prepares for first convention since 2014",
      "description": "President Muhammadu Buhari is expected to chair the All Progressives Congress (APC) national executive committee (NEC) meeting coming up on Tuesday ahead of the party’s national convention slated for Abuja. Governors",
      "image": "https://www.thecable.ng/wp-content/uploads/2017/11/PRESIDENT-BUHARI-PRESENTS-BOOK-BY-PRESIDENTIAL-MEDIA-TEAM-000.jpg"
    },
    {
      "urlToNewsArticle": "https://independent.ng/okowa-promises-n5m-donation-uvwie-monarchs-scholarship-programme/",
      "title": "Okowa Promises N5m Donation For Uvwie Monarch's Scholarship Programme",
      "description": "Governor Okowa, who made this known during the 10th year Anniversary celebration of the Ovie of Uvwie Kingdom, congratulated the people of the kingdom for the 10th year anniversary of the king.",
      "image": "https://independent.ng/wp-content/uploads/2017/09/EmmaOkowaPost.jpg"
    },
    {
      "urlToNewsArticle": "https://theeagleonline.com.ng/nans-condemns-abduction-of-dapchi-school-girls/",
      "title": "NANS condemns abduction of Dapchi school girls",
      "description": "NANS’s President, Chinonso Obasi, in a statement on Monday in Abuja, urged the relevant authorities to ensure the immediate rescue of the girls.",
      "image": "https://theeagleonline.com.ng/wp-content/uploads/2018/02/NANS.jpg"
    },
    {
      "urlToNewsArticle": "https://punchng.com/despite-military-presence-over-a-million-cows-have-flooded-benue-ortom-laments/",
      "title": "Despite military presence, over a million cows have flooded Benue, Ortom laments",
      "description": "John Charles, Makurdi\r\n\r\nBenue State Governor, Samuel Ortom, on Monday raised fresh concerns of possible herdsmen attacks in the state.\r\n\r\nThe governor dropped this hint when he led the senior past...",
      "image": "http://cdn.punchng.com/wp-content/uploads/2017/04/25101751/cows.jpg"
    },
    {
      "urlToNewsArticle": "http://punchng.com/tambuwal-appoints-special-adviser-on-poultry-four-others/",
      "title": "Tambuwal appoints special adviser on Poultry, four others",
      "description": "Governor Aminu Tambuwal of Sokoto State, on Monday, announced the appointment of five new special advisers and deployment of some Permanent Secretaries.\r\n\r\nA statement issued in Sokoto by Tambuwal’...",
      "image": "http://cdn.punchng.com/wp-content/uploads/2016/03/29104639/Sokoto-State-Governor-Aminu-Tambuwal-.jpg"
    },
    {
      "urlToNewsArticle": "http://www.tv360nigeria.com/lagos-governor-signs-2018-budget-into-law/",
      "title": "Lagos Governor signs 2018 budget into law",
      "image": "http://www.tv360nigeria.com/wp-content/uploads/PIX-5056-660x330.jpg"
    },
    {
      "urlToNewsArticle": "http://dailypost.ng/2018/02/26/2019-dino-melaye-two-senators-float-save-kogi-group/",
      "title": "2019: Dino Melaye, two other senators float 'Save Kogi Group'",
      "description": "Senators from the three senatorial districts of Kogi state on Monday inaugurated a Save Kogi Group, ahead of the 2019 general elections. Senator Dino Melay",
      "image": "http://dailypost.ng/wp-content/uploads/2017/06/Dino-Melaye-.jpg"
    },
    {
      "urlToNewsArticle": "https://www.vanguardngr.com/2018/02/oloyede-expresses-satisfaction-211000-utme-candidates-write-mock-exam/",
      "title": "Oloyede expresses satisfaction as 211000 UTME candidates write mock exam",
      "description": "ABUJA- AHEAD of the 2018 Unified Tertiary Matriculation Examination,UTME,billed to commence on March 6,the Registrar of Joint Admissions and Matriculation Board,JAMB,Prof. Ishaq Oloyede,has expressed hope that the exercise would experience significant improve…",
      "image": "https://cdn.vanguardngr.com/wp-content/uploads/2018/01/Prof-Ishaq-Oloyede.jpg"
    },
    {
      "urlToNewsArticle": "https://www.vanguardngr.com/2018/02/police-begins-illegal-arms-mop/",
      "title": "Police begins illegal arms mop up",
      "description": "ENUGU- THE Nigeria Police Force has commenced mop up of illegal firearms across states in the country.",
      "image": "https://cdn.vanguardngr.com/wp-content/uploads/2018/01/boko-arms.jpg"
    }
  ],
  "safety": {
    "human_attack_safety": {
      "index": "84",
      "status": "Slightly Safe"
    },
    "natural_disaster_safety": {
      "status_colour": "OrangeRed",
      "status_text": "Slightly Dangerous",
      "index": "81"
    },
    "name": "Bosnia and Herzegovina"
  }
}
        return render(request, "post_list.html", context)


if __name__ == "__main__":
    """
    nigeria ="nigeria"
    print(timeit.timeit("country_info(nigeria)", number=2, globals=globals()))
    print(timeit.timeit("country_ju(nigeria)", number=2, globals=globals()))
    """
    print(country_info('Bosnia and Herzegovina'))
