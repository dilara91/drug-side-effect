#!/usr/bin/python
import sys
import os

import owlready2 as owl
import ontologyHandler as ontHandlerModule

global ontologyHandler

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

import search as ss

def createOntology(directory,filename):
	global ontologyHandler
	ontologyHandler = ontHandlerModule.OntologyHandler(directory,filename)
	ss.createOntology(directory,filename)
	
def getTagRecommendations(blog_text):
	blog_text = blog_text.lower()
	words = word_tokenize(blog_text)
	for item in words:
		print(item)

	adverse_effect = ss.getAllAdverseEffects()
	drugs = ss.getAllDrugs()
	for item in drugs:
		print(item)

	for item in adverse_effect:
		print(item)

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


if __name__ == '__main__':
	createOntology()