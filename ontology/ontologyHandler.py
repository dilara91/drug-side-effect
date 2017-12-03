#!/usr/bin/python
import sys

import owlready2 as owl

class OntologyHandler:
   
   def __init__(self, ontologyDirectory, ontologyIRI):
      self.ontologyDirectory = ontologyDirectory
      self.ontologyIRI = ontologyIRI
      owl.onto_path.append(self.ontologyDirectory)
      self.ontology = owl.get_ontology(self.ontologyIRI).load()
   
   def getOntology(self):
      return self.ontology

   def getInstance(self,instanceID):
      return self.ontology[instanceID]

   def getInstancesForClass(self,className):
      return self.ontology.search(type = self.ontology[className])

   def getInstancesWithProperty(self,propertyName,propertyValue,reasoner):

      if reasoner:
         owl.sync_reasoner()

      resultList = []

      if propertyName == "hasEffect":
          resultList = self.ontology.search(hasEffect = self.ontology[propertyValue])
      elif propertyName == "hasEffectOn":
         resultList = self.ontology.search(hasEffectOn = self.ontology[propertyValue])
      elif propertyName == "hasActiveIngredient":
         resultList = self.ontology.search(hasActiveIngredient = self.ontology[propertyValue])
      elif propertyName == "containedIn":
         resultList = self.ontology.search(containedIn = self.ontology[propertyValue])
      elif propertyName == "affectedBy":
         resultList = self.ontology.search(affectedBy = self.ontology[propertyValue])
      elif propertyName == "causedBy":
         resultList = self.ontology.search(causedBy = self.ontology[propertyValue])

      return [item.name for item in resultList]
     

