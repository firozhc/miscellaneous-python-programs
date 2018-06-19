import re
import filechanger as fc


def main():

	file_name = "UniversalFileHeader.txt"

	va_file_name = "va.csv"

	new_va_file_name = "VA.txt"

#	fha_file_name = "FHA.csv"

#	new_fha_file_name = "FHA.txt"

	fha_file_name = "fha-9.csv"

	new_fha_file_name = "fha-9.txt"

	#file_name = "va.csv"

	pattern = r'\[(.*?)\]'

	header_file= []
	va_file = []
	fha_file = []

	with open(file_name, 'rU') as f:
		for line in f:
			match = re.findall(pattern, line)
			if match:
				header_file.append((match[0].lower()))
	f.close()


	try:
		fc.major_lazer(va_file_name, new_va_file_name)  ### Create the VA txt File
		#print('Congratulations! "'+new_va_file_name+'" File Succesfully Created')

	except:
		print("IO Error, Could not create File- "+new_va_file_name)


	try:
		fc.major_lazer(fha_file_name, new_fha_file_name)  ### Create the FHA txt File
		#print('Congratulations! "'+new_fha_file_name+'" File Succesfully Created')
		
	except:
		print("IO Error, Could not create File- "+new_fha_file_name)
		#print(Error)


	with open(new_va_file_name,'r') as va:
		for item in va:
			va_file += item.split(',')
	va.close()

	with open(new_fha_file_name,'r') as fha:
		for item in fha:
			fha_file += item.split(',')
	fha.close()
	"""
	print("Header File Contents:->")
	print(header_file)

	print("VA File Contents:->")
	print(va_file)

	print("FHA File Contents:->")
	print(fha_file)

	"""
	solution_header = {}

	l = []

	for item in header_file:
		if item in va_file:
			l.append("VA")
		if item in fha_file:
			l.append("FHA")
		solution_header[item] = l
		l = []
		output_string = ""

	for key in solution_header:
		if len(solution_header[key]) != 0:
			#print(key, solution_header[key])
			output_string = output_string + " " + key + "," + str(solution_header[key]) + '\n'

	
	with open("output_file.csv",'w') as f:
		f.write(output_string)

		f.close()




if __name__=='__main__':
	main()








