#!/usr/bin/python
import sys
import os

import owlready2 as owl
import ontology.ontologyHandler as ontHandlerModule

# global ontologyHandler


# def createOntology():
class OntologySearch():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ontologyDirectory = os.path.join(path, "ontology/")
    ontologyName = 'drugs.owl'
    # global ontologyHandler
    ontologyHandler = ontHandlerModule.OntologyHandler(ontologyDirectory, ontologyName)

    def getAllDrugs(self):
        result_list = self.ontologyHandler.getInstancesForClass('Drug')
        return [item.name for item in result_list]

    def getAllAdverseEffects(self):
        result_list = self.ontologyHandler.getInstancesForClass('AdverseEffect')
        return [item.name for item in result_list]

    def searchAdverseEffects(self, drugName):
        return self.ontologyHandler.getInstancesWithProperty("causedBy", drugName, False)


    def searchDrugsWithAdverseEffect(self, adverseEffect):
        return self.ontologyHandler.getInstancesWithProperty("hasEffect", adverseEffect, False)


    def searchDrugsWithActiveIngredient(self, activeIngredient):
        return self.ontologyHandler.getInstancesWithProperty("hasActiveIngredient", activeIngredient, False)


    def searchActiveIngredientsWithDrug(self, drugName):
        return self.ontologyHandler.getInstancesWithProperty("containedIn", drugName, False)


    def searchActiveIngredientsWithAdverseEffect(self, adverseEffect):
        drugList = self.searchDrugsWithAdverseEffect(adverseEffect, False)
        activeIngredientSet = set()
        for drug in drugList:
            activeIngredientSet.update(self.searchActiveIngredientsWithDrug(drug))


    def searchBodyPartsForAdverseEffect(self, adverseEffect):
        return self.ontologyHandler.getInstancesWithProperty("affectedBy", adverseEffect, False)


    def searchAdverseEffectWithDescription(self, description):
        adverseEffects = self.ontologyHandler.getInstancesForClass("AdverseEffect")
        desc_list = [item.hasDescription for item in adverseEffects]
        similarity_dict = {}
        description = description.lower()
        tokenized_desc = description.split()
        for desc in desc_list:
            adverseEffectName = adverseEffects[desc_list.index(desc)]
            adverseEffectName = adverseEffectName.name
            if self.match(adverseEffectName, description):
                score = len(tokenized_desc) + 1
            else:
                score = self.find_similarity(desc[0], tokenized_desc)
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

    def find_similarity(self, desc, tokenized_search_desc):
        desc = desc.lower()
        tokenized_ontology_desc = desc.split()
        intersect = set(tokenized_ontology_desc).intersection(set(tokenized_search_desc))
        return len(intersect)

    def match(self, adverseEffectName, description):
        adverseEffectName = adverseEffectName.lower()
        description = description.lower()
        if (adverseEffectName == description):
            return True

        description = description.replace(" ", "")
        if (adverseEffectName == description):
            return True

        return False


# if __name__ == '__main__':
#     createOntology()
