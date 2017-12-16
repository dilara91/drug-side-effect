#!/usr/bin/python
import sys
import os

import owlready2 as owl

def createOntology():
	ontologyDirectory = os.path.join('.')
	ontologyName = os.path.join('.', 'drugs_users.owl')
	global ontology
	owl.onto_path.append(ontologyDirectory)
    ontology = owl.get_ontology(ontologyName).load()



def addNewEntry(drugName,adverseEffect,userid,userAge,userGender,userHeight,userWeight):
	key = str(time.time())
	key.replace('.',"")
	adverse_onto = getAdverseEffect(adverseEffect)
	new_drug =  Drug(str("drug_",key), namespace = ontology, hasEffect = adverse_onto, hasName = drugName)
	if existingUser(userid):
		user = ontology[userid]
	else:
		user = User(userid, namespace = ontology, hasAge = userAge, hasGender = userGender, hasHeight = userHeight, hasWeight = userWeight)

	user.showsSymptoms.append(adverse_onto)
	user.uses.append(new_drug)
	ontology.save()

	


if __name__ == '__main__':
	createOntology()