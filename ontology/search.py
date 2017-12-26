#!/usr/bin/python
import sys
import os

import owlready2 as owl
import ontologyHandler as ontHandlerModule

global ontologyHandler

def createOntology(directory,filename):
	ontologyDirectory = os.path.join('/Users/i339336/drug-side-effect/ontology')
	ontologyName = os.path.join(ontologyDirectory, 'drugs.owl')
	#ontologyName = "http://semanticweb.org/teamO/drug-effects"
	global ontologyHandler
	ontologyHandler = ontHandlerModule.OntologyHandler(directory,filename)
	
def searchAdverseEffects(drugName):
	return ontologyHandler.getInstancesWithProperty("causedBy",drugName,False)

def searchDrugsWithAdverseEffect(adverseEffect):
	return ontologyHandler.getInstancesWithProperty("hasEffect",adverseEffect,False)

def searchDrugsWithActiveIngredient(activeIngredient):
	return ontologyHandler.getInstancesWithProperty("hasActiveIngredient",activeIngredient,False)

def searchActiveIngredientsWithDrug(drugName):
	return ontologyHandler.getInstancesWithProperty("containedIn",drugName,False)

def searchActiveIngredientsWithAdverseEffect(adverseEffect):
	drugList = searchDrugsWithAdverseEffect(adverseEffect,False)
	activeIngredientSet = set()
	for drug in drugList:
		activeIngredientSet.update(searchActiveIngredientsWithDrug(drug))
		
def searchBodyPartsForAdverseEffect(adverseEffect):
	return ontologyHandler.getInstancesWithProperty("affectedBy",adverseEffect,False)

def searchAdverseEffectWithDescription(description):
	adverseEffects = ontologyHandler.getInstancesForClass("AdverseEffect")
	desc_list = [item.hasDescription for item in adverseEffects]
	similarity_dict = {}
	description = description.lower()
	tokenized_desc = description.split()
	for desc in desc_list:
		adverseEffectName = adverseEffects[desc_list.index(desc)]
		adverseEffectName = adverseEffectName.name
		if match(adverseEffectName,description):
			score = len(tokenized_desc) + 1
		else:
			score = find_similarity(desc[0],tokenized_desc)
		if score in similarity_dict:
			temp_list = similarity_dict[score]
			temp_list.append(adverseEffectName)
			similarity_dict[score] = temp_list
		else:
			temp_list = []
			temp_list.append(adverseEffectName)
			similarity_dict[score] = temp_list
	result_list = []
	for key in sorted(similarity_dict):
		result_list.extend(similarity_dict[key])

	result_list = list(reversed(result_list))
	return result_list


def find_similarity(desc,tokenized_search_desc):
	desc = desc.lower()
	tokenized_ontology_desc = desc.split()
	intersect = set(tokenized_ontology_desc).intersection(set(tokenized_search_desc))
	return len(intersect)
    
def match(adverseEffectName,description):
	adverseEffectName = adverseEffectName.lower()
	description = description.lower()
	if(adverseEffectName == description):
		return True

	description = description.replace(" ", "")
	if(adverseEffectName == description):
		return True

	return False





if __name__ == '__main__':
	createOntology()