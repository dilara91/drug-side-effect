from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from main.models import User, Drug
from django.views.generic import ListView
from django.views.generic.base import TemplateView
import sys
sys.path.insert(0, '/Users/i339336/drug-side-effect/ontology')
import addEntries 
import search_social as ss
import ontologyHandler as oh
import search as ae

import os
from urllib.request import urlopen


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        
        filename = os.path.join('/Users/i339336/drug-side-effect/ontology','drugs.owl')
        f = open(filename)
        ae.createOntology('/Users/i339336/drug-side-effect/ontology',filename)
        x = ae.searchAdverseEffects('Aspirin')
        for item in x:
            print(item)

        context = super().get_context_data(**kwargs)
        context['drugs'] = x
        return context




''' 
def home(request):
    d = Drug(drugID = 3, drugname = "Buscopan")
    d.save()

    d2 = Drug(drugID = 3, drugname = "Aspirin")
    d2.save()
    drug_list = Drug.objects.all()

    return render(request, template_name="home.html", {'drugs': drug_list}) '''




