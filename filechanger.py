import re


def create_row_name(name):

	pattern = r'[a-z0-9]'

	match = re.findall(pattern, name)

	string =''

	for e in match:
		string += e

	return string


def major_lazer(file_name, new_file_name1):


#	file_name = "va.csv"

	with open(file_name,'r') as f:
		rows = f.read().split(',')
	

	f.close()

	#new_file_name1 ="VA.txt"

	with open(new_file_name1,'w') as fw:
		for row in rows:
			if row != '':
				fw.write(create_row_name(row.lower()) + ",")

	fw.close()





		