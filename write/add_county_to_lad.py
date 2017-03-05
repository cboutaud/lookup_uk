import csv

# First file to which we want to add county data
inputfile_lad = open("../pc_to_oa_lsoa_msoa_lad.csv")
lad_reader = csv.reader(inputfile_lad)
header = next(lad_reader) # skip and save headers so we can write the new header from it

# Second file from which we get county data
inputfile_county = open("../lad_to_county.csv")
county_reader = csv.reader(inputfile_county)
next(county_reader) #skip headers

# We are gonna write a new file rather than overwrite the first file
outputfile = open("../pc_to_oa_lsoa_msoa_lad_county.csv", "wb")
csv_writer = csv.writer(outputfile)
new_header = header[0:10] + [ "county", "county_name"] + [header[10]]
csv_writer.writerow(new_header)

# We're goona write a list with the lad for which we have county data
lad_from_county = []
for row in county_reader:
	lad_name = row[1]
	if lad_name not in lad_from_county:
		lad_from_county.append(lad_name)
inputfile_county.seek(0)

# Now we are ready to start looping through lad and get county data for each one... if available (see if/else loop)
for index, row in enumerate(lad_reader):
	# if index >= 100:
	# 	break
	lad = row[8]
	data = row[0:10]
	is_split = row[10]

	# With the list we wrote in the first part we can sort and say
	# If we have county data for that lad do this / else do that 
	if lad in lad_from_county:
		for row in county_reader:
			lad_name = row[1]
			county_data = row [2:4]
			if lad == lad_name:
				data.extend(county_data)
				data.append(is_split)
				csv_writer.writerow(data)
				break
		inputfile_county.seek(0)
	else:
		county_data = ["",""]
		data.extend(county_data)
		data.append(is_split)
		csv_writer.writerow(data)

# ---------------------------

# code used during testing

# To make if every lad are spelled the same way in the two files (wales and ua excluded)
# lad_from_county = []
# for row in county_reader:
# 	lad_name = row[1]
# 	if lad_name not in lad_from_county:
# 		lad_from_county.append(lad_name)
# lad_not_in_county = []
# for row in lad_reader:
# 	lad = row[8]
# 	if lad not in lad_from_county:
# 		if lad not in lad_not_in_county:
# 			lad_not_in_county.append(lad)
# print lad_not_in_county
