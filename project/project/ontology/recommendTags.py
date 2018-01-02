#!/usr/bin/python
import sys
import os

import owlready2 as owl
import ontology.ontologyHandler as ontHandlerModule

global ontologyHandler

import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

import search as ss

class recommendTags():

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ontologyDirectory = os.path.join(path, "ontology/")
    ontologyName = 'drugs.owl'
    # global ontologyHandler
    ontologyHandler = ontHandlerModule.OntologyHandler(ontologyDirectory, ontologyName)


    def getTagRecommendations(blog_text):
        blog_text = blog_text.lower()
        words = word_tokenize(blog_text)

        adverse_effect = ss.getAllAdverseEffects()
        drugs = ss.getAllDrugs()

        tags = []

        for item in adverse_effect:
            item = item.lower()
            if item in words:
                tags.append(item)

        for item in drugs:
            item = item.lower()
            item = item.split('/')[0]
            if item in words:
                tags.append(item)

        return tags