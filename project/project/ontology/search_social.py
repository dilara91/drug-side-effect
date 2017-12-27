#!/usr/bin/python
import sys
import os

import rdflib
from rdflib import Namespace


def createOntology():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ontologyPath = os.path.join(os.path.join(path, "ontology/"), 'drugs_social.owl')
    global g
    g = rdflib.Graph()
    g.load(ontologyPath, format='xml')


def searchAdverseEffects(drugName, userAge, userGender, userWeight, userHeight):
    result_list = []
    # We are aiming to show related effects higher
    # relation is determined by the closeness of the profiles of users.
    # if every category matches then it appears on front
    namespace = dict(ont=Namespace("http://www.semanticweb.org/teamO/drug-effects#"))

    query = """SELECT ?effect
		WHERE { 	
			?user a ont:User;
			ont:uses ?drug;
			ont:hasAge ?age;
			ont:hasGender ?gender;
			ont:hasWeight ?weight;
			ont:hasHeight ?height.
			?drug ont:hasName ?drugname;
			ont:hasEffect ?effect.
		FILTER (?age > """ + str(userAge - 5) + """ && ?age < """ + str(userAge + 5) + """
				&& ?weight > """ + str(userWeight - 10) + """ && ?weight < """ + str(userWeight + 10) + """
				&& ?height > """ + str(userHeight - 10) + """ && ?height < """ + str(userHeight + 10) + """
				&& ?drugname = '""" + drugName + """'
			    && ?gender = '""" + normalizeUserGender(userGender) + """') }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        effect = item[0].n3().split('#')[1].split('>')[0]  # extract the side effect name
        if effect not in result_list:
            result_list.append(effect)

    # matches everything but gender

    query = """SELECT ?effect
		WHERE { 	
			?subject a ont:User;
			ont:uses ?drug;
			ont:hasAge ?age;
			ont:hasWeight ?weight;
			ont:hasHeight ?height.
			?drug ont:hasName ?drugname;
			ont:hasEffect ?effect.
		FILTER (?age > """ + str(userAge - 5) + """ && ?age < """ + str(userAge + 5) + """
				&& ?weight > """ + str(userWeight - 10) + """ && ?weight < """ + str(userWeight + 10) + """
				&& ?height > """ + str(userHeight - 10) + """ && ?height < """ + str(userHeight + 10) + """
				&& ?drugname = '""" + drugName + """') }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        effect = item[0].n3().split('#')[1].split('>')[0]  # extract the side effect name
        if effect not in result_list:
            result_list.append(effect)

    # matches age and weight
    query = """SELECT ?effect
		WHERE { 	
			?subject a ont:User;
			ont:uses ?drug;
			ont:hasAge ?age;
			ont:hasWeight ?weight.
			?drug ont:hasName ?drugname;
			ont:hasEffect ?effect.
		FILTER (?age > """ + str(userAge - 5) + """ && ?age < """ + str(userAge + 5) + """
				&& ?weight > """ + str(userWeight - 10) + """ && ?weight < """ + str(userWeight + 10) + """
				&& ?drugname = '""" + drugName + """') }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        effect = item[0].n3().split('#')[1].split('>')[0]  # extract the side effect name
        if effect not in result_list:
            result_list.append(effect)

    # matches age
    query = """SELECT ?effect
		WHERE { 	
			?subject a ont:User;
			ont:uses ?drug;
			ont:hasAge ?age.
			?drug ont:hasName ?drugname;
			ont:hasEffect ?effect.
		FILTER (?age > """ + str(userAge - 5) + """ && ?age < """ + str(userAge + 5) + """
				&& ?drugname = '""" + drugName + """') }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        effect = item[0].n3().split('#')[1].split('>')[0]  # extract the side effect name
        if effect not in result_list:
            result_list.append(effect)

    # no similarity only uses this drug
    query = """SELECT ?effect
		WHERE { 	
			?subject a ont:User;
			ont:uses ?drug.
			?drug ont:hasName ?drugname;
			ont:hasEffect ?effect.			
		FILTER (?drugname = '""" + drugName + """') }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        effect = item[0].n3().split('#')[1].split('>')[0]  # extract the side effect name
        if effect not in result_list:
            result_list.append(effect)

    return result_list


def searchDrugsWithAdverseEffect(adverseEffect, userAge, userGender, userWeight, userHeight):
    result_list = []
    # We are aiming to show related effects higher
    # relation is determined by the closeness of the profiles of users.
    # if every category matches then it appears on front
    namespace = dict(ont=Namespace("http://www.semanticweb.org/teamO/drug-effects#"))

    query = """SELECT ?drugName
		WHERE { 	
			?user a ont:User;
			ont:uses ?drug;
			ont:hasAge ?age;
			ont:hasGender ?gender;
			ont:hasWeight ?weight;
			ont:hasHeight ?height.
			?drug ont:hasName ?drugname;
			ont:hasEffect ont:""" + adverseEffect + """.
		FILTER (?age > """ + str(userAge - 5) + """ && ?age < """ + str(userAge + 5) + """
				&& ?weight > """ + str(userWeight - 10) + """ && ?weight < """ + str(userWeight + 10) + """
				&& ?height > """ + str(userHeight - 10) + """ && ?height < """ + str(userHeight + 10) + """
				&& ?gender = '""" + normalizeUserGender(userGender) + """') }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        drug = item[0].n3().split('"')[1]  # extract the side drug name
        if drug not in result_list:
            result_list.append(drug)

    # matches everything but gender

    query = """SELECT ?drugName
		WHERE { 	
			?user a ont:User;
			ont:uses ?drug;
			ont:hasAge ?age;
			ont:hasWeight ?weight;
			ont:hasHeight ?height.
			?drug ont:hasName ?drugname;
			ont:hasEffect ont:""" + adverseEffect + """.
		FILTER (?age > """ + str(userAge - 5) + """ && ?age < """ + str(userAge + 5) + """
				&& ?weight > """ + str(userWeight - 10) + """ && ?weight < """ + str(userWeight + 10) + """
				&& ?height > """ + str(userHeight - 10) + """ && ?height < """ + str(userHeight + 10) + """) }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        drug = item[0].n3().split('"')[1]  # extract the side drug name
        if drug not in result_list:
            result_list.append(drug)

    # matches age and weight
    query = """SELECT ?drugname
		WHERE { 	
			?user a ont:User;
			ont:uses ?drug;
			ont:hasAge ?age;
			ont:hasWeight ?weight.
			?drug ont:hasName ?drugname;
			ont:hasEffect ont:""" + adverseEffect + """.
		FILTER (?age > """ + str(userAge - 5) + """ && ?age < """ + str(userAge + 5) + """
				&& ?weight > """ + str(userWeight - 10) + """ && ?weight < """ + str(userWeight + 10) + """) }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        drug = item[0].n3().split('"')[1]  # extract the side drug name
        if drug not in result_list:
            result_list.append(drug)

    # matches age
    query = """SELECT ?drugname
		WHERE { 	
			?subject a ont:User;
			ont:uses ?drug;
			ont:hasAge ?age.
			?drug ont:hasName ?drugname;
			ont:hasEffect ont:""" + adverseEffect + """.
		FILTER (?age > """ + str(userAge - 5) + """ && ?age < """ + str(userAge + 5) + """) }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        drug = item[0].n3().split('"')[1]  # extract the side drug name
        if drug not in result_list:
            result_list.append(drug)

    # no similarity only uses this drug
    query = """SELECT ?drugname
		WHERE { 	
			?subject a ont:User;
			ont:uses ?drug.
			?drug ont:hasName ?drugname;
			ont:hasEffect ont:""" + adverseEffect + """. }	"""

    qres = g.query(query, initNs=namespace)

    for item in qres.result:
        drug = item[0].n3().split('"')[1]  # extract the side drug name
        if drug not in result_list:
            result_list.append(drug)

    return result_list


def normalizeUserGender(userGender):
    userGender = userGender.lower()
    if userGender == 'female' or userGender == 'male':
        return userGender
    else:
        return 'Unknown'


if __name__ == '__main__':
    createOntology()
