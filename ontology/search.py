#!/usr/bin/python
import sys
import os

import owlready2 as owl
import ontologyHandler as ontHandlerModule

global ontologyHandler

def createOntology():
	ontologyDirectory = os.path.join('.')
	ontologyName = os.path.join('.', 'drugs.owl')
	global ontologyHandler
	ontologyHandler = ontHandlerModule.OntologyHandler(ontologyDirectory,ontologyName)
	
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



if __name__ == '__main__':
	createOntology()