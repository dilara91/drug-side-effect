#!/usr/bin/python
import sys
import os
import time
import owlready2 as owl


class CreateOntology():

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    ontologyDirectory = os.path.join(path, "ontology/")

    ontologyName = 'drugs_social.owl'
    # global ontology
    owl.onto_path.append(ontologyDirectory)
    ontology = owl.get_ontology(ontologyName).load()

    def addNewEntry(self, drugName, adverseEffect, userid, username, userAge, userGender, userHeight, userWeight):
        key = str(time.time())
        key = key.replace('.', "")
        adverse_onto = self.getAdverseEffect(adverseEffect)
        if adverse_onto is None:
            print("The adverse effect is not on the ontology. Cannot add entry.")
            return "The adverse effect is not on the ontology. Cannot add entry."
        if not self.drugExists(drugName):
            print("The drug is not on the ontology. Cannot add entry.")
            return "The drug is not on the ontology. Cannot add entry."

        userGender = self.normalizeUserGender(userGender)
        if userGender == 'Unknown':
            print("The gender is unknown. Cannot add entry.")
            return "The gender is unknown. Cannot add entry."

        new_drug = self.ontology.Drug("drug_" + key, namespace=self.ontology, hasEffect=[adverse_onto], hasName=[drugName])

        user_id_onto = "user_" + str(userid)
        if self.existingUser(user_id_onto):
            user = self.ontology[user_id_onto]
        else:
            user = self.ontology.User(user_id_onto, namespace=self.ontology, hasName=[username], hasAge=[userAge], hasGender=[userGender], hasHeight=[userHeight], hasWeight=[userWeight])

        user.showsSymptoms.append(adverse_onto)
        user.uses.append(new_drug)
        self.ontology.save()
        return "Successfully Saved"

    def getAdverseEffect(self, adverseEffect):
        return self.ontology[adverseEffect]

    def drugExists(self, drugName):
        drug = self.ontology[drugName]
        if drug is None:
            return False
        else:
            return True

    def existingUser(self, userid):
        userid = self.ontology[userid]
        if userid is None:
            return False
        else:
            return True

    def normalizeUserGender(self, userGender):
        userGender = userGender.lower()
        if userGender == 'female' or userGender == 'male':
            return userGender
        else:
            return 'Unknown'

# if __name__ == '__main__':
#     createOntology()
