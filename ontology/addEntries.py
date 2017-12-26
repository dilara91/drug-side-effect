#!/usr/bin/python
import sys
import os
import time
import owlready2 as owl

def createOntology():
	ontologyDirectory = os.path.join('Users/i339336/drug-side-effect/ontology')
	ontologyName = os.path.join('drugs_social.owl')
	global ontology
	owl.onto_path.append(ontologyDirectory)
	ontology = owl.get_ontology(ontologyName).load()

def addNewEntry(drugName,adverseEffect,userid,username,userAge,userGender,userHeight,userWeight):
	key = str(time.time())
	key = key.replace('.',"")
	adverse_onto = getAdverseEffect(adverseEffect)
	if adverse_onto is None:
		print("The adverse effect is not on the ontology. Cannot add entry.")
		return
	if not drugExists(drugName):
		print("The drug is not on the ontology. Cannot add entry.")
		return

	userGender = normalizeUserGender(userGender)
	if userGender == 'Unknown':
		print("The gender is unknown. Cannot add entry.")
		return

	new_drug =  ontology.Drug("drug_"+key, namespace = ontology, hasEffect = [adverse_onto], hasName = [drugName])

	user_id_onto = "user_"+str(userid)
	if existingUser(user_id_onto):
		user = ontology[user_id_onto]
	else:
		user = ontology.User(user_id_onto, namespace = ontology, hasName = [username], hasAge = [userAge], hasGender = [userGender], hasHeight = [userHeight], hasWeight = [userWeight])

	user.showsSymptoms.append(adverse_onto)
	user.uses.append(new_drug)
	ontology.save()

def getAdverseEffect(adverseEffect):
	return ontology[adverseEffect]

def drugExists(drugName):
	drug = ontology[drugName]
	if drug is None:
		return False
	else:
		return True

def existingUser(userid):
	userid = ontology[userid]
	if userid is None:
		return False
	else:
		return True

def normalizeUserGender(userGender):
	userGender = userGender.lower()
	if userGender == 'female' or userGender == 'male':
		return userGender
	else:
		return 'Unknown'


if __name__ == '__main__':
	createOntology()