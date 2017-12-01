#!/usr/bin/python
import sys

import owlready2 as owl

class Ontology:
   
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
      return self.ontology.search(type = onto[className])

   def getInstancesWithProperty(self,propertyName,propertyValue,reasoner):

      if reasoner:
         owl.sync_reasoner()

      resultList = []

      if propertyName == "hasEffect":
          self.ontology.search(hasEffect = ontology[propertyValue])
      elif propertyName == "hasEffectOn":
         self.ontology.search(hasEffectOn = ontology[propertyValue])
      elif propertyName == "hasActiveIngredient":
         self.ontology.search(hasActiveIngredient = ontology[propertyValue])
      elif propertyName == "containedIn":
         self.ontology.search(containedIn = ontology[propertyValue])
      elif propertyName == "affectedBy":
         self.ontology.search(affectedBy = ontology[propertyValue])
      elif propertyName == "causedBy":
         self.ontology.search(causedBy = ontology[propertyValue])
      else:
         []

      return [item.name for item in resultList]
     

