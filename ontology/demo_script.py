#!/usr/bin/python
import sys
import os

import search
import search_social as ss
import addEntries as ae
import recommendTags as rt


def start():

	drug_name = 'Majezik'
	print("Opening ontology...")
	print("Open formal ontology...")
	search.createOntology('.','drugs.owl')
	print("Open social populated ontology...")
	ss.createOntology('drugs_social.owl')
	ae.createOntology()
	print("Ontologies created...")


	input("")
	print("User Paul searches for adverse effects of "+drug_name+". Paul is 32 years old male with 180cm height and 70kg weight.")
	input("")
	print("Results from formal ontology...")
	formal_result = search.searchAdverseEffects(drug_name)
	for item in formal_result:
		print(item)
	print('\n')

	input("")
	print("Results from user populated ontology...")
	informal_result = ss.searchAdverseEffects(drug_name,32,'male',70,180)
	for item in informal_result:
		print(item)
	print('\n')


	input("")
	print("Paul also want to add an adverse effect for "+drug_name+". He did not see the effect he experienced in the search results.")
	print("Paul experiences shaking hands. So he wants to add it as an adverse effect.")
	input("")
	ae.addNewEntry(drug_name,'Hands shaking','10001','paul',32,'male',180,70)
	input("")
	result = search.searchAdverseEffectWithDescription('Hands shaking')
	count = 0
	for item in result:
		if count >4:
			break
		count = count + 1
		print(item)
	print('\n')
	input("")
	print('Tremor is given as a suggestion. Added new entry for '+drug_name+' as tremor. Now if we search again as Paul, tremor must be shown at front.')
	ae.addNewEntry(drug_name,'Tremor','10001','paul',32,'male',180,70)
	ss.updateOntology()

	print('\n')
	print("Results from user populated ontology...")
	informal_result = ss.searchAdverseEffects(drug_name,32,'male',70,180)
	for item in informal_result:
		print(item)
	print('\n')

	input("")
	print('\n')
	print("Let's say Paul written a blog about his experience with "+drug_name+" but didn't tag the post. We recommend him tags to add.")
	text = "This is such a horrible morning. I took "+drug_name+" for my hungover. Now my hands are shaking like crazy. I guess the term for the symptom was Tremor."
	print(text)
	input("")
	result_tag = rt.getTagRecommendations(text)
	count = 0
	for item in result_tag:
		if count >4:
			break
		count = count + 1
		print(item)
	print('\n')



	

if __name__ == '__main__':
	start()