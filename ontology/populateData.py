
import sys
import os
import addEntries as ade


def populate_data():

	common_separator = ';'
	drug_separator = ';'
	adverse_separator = ','
	drug_adverse_separator = '->'

	ade.createOntology()
	data_file = open('data_son.csv', encoding="utf-8")
	data_lines = data_file.readlines()
	#username|userid|age|sex|height|weight|credibility|drug|adverseeffect|drugusage
	for item in data_lines:
		item_list = item.split('"')
		if len(item_list) < 2:
			continue
		first_part = item_list[0]
		second_part =  item_list[1]
		split_item = first_part.split(common_separator)
		username = split_item[0]
		userid = split_item[1]
		age = split_item[2]
		sex = split_item[3]
		height = split_item[4]
		weight = split_item[5]
		credibility = split_item[6]
		#drug = split_item[7]
		#adverseeffect = split_item[8]
		drugusage = second_part.strip()
		#drug-> ae,ae ; drug->ae; ...
		drugList = drugusage.split(drug_separator)
		if len(drugList) == 0:
			continue

		for d in drugList:
			drug_adverse_list = d.split(drug_adverse_separator)
			if len(drug_adverse_list) < 2:
				continue

			drug = drug_adverse_list[0]
			drug = drug.strip()
			
			adverseeffectList = drug_adverse_list[1].split(adverse_separator)
			for adverse in adverseeffectList:
				adverse = adverse.strip()
				ade.addNewEntry(drug,adverse,int(userid),username,int(age),sex,int(height),int(weight))



if __name__ == '__main__':
	populate_data()