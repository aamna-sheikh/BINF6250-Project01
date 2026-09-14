
#!/usr/bin/env python
from pprint import pprint


# parse_line function
def parse_line(line: string):

# look into switching to the other command 
	if line startswith("#"):
			continue

	columns = line.split("\t")

		info_field = columns[7]              
		info_items = info_field.split(";") 


	for each item in info_items:
			if item startswith("AF_EXAC="): 
			# Split INFO by semicolons to get key-value fields
				raw_value = item.split("=")[1]
				af_exac_value = float(raw_value)
			    

		if af_exac_value is None:
			return []

		if af_exac_value >= 0.0001:
			return []      
			
		disease_list = []

		for item in info_items:
			if item startswith("CLNDN="):
				raw_diseases = item.split("=")[1]
				disease_names = raw_diseases.split("|") 

				for name in disease_names:
					trimmed_name = name.strip()
					if trimmed_name is None:
						continue
					if trimmed_name == "not_specified" or trimmed_name == "not_provided":
						continue
					disease_list.append(trimmed_name)
				break

		return disease_list

# -----------------------------------------------------
# read_file function
def read_file(filename: string):
  disease_counts = {}

    with open (filename , "r") as file:
        for each line in file:
            diseases = parse_line(line)

# do we have to add key value pair
            for disease in diseases:
                if disease in disease_counts:
                    disease_counts[disease] += 1 
                else:
                    disease_counts[disease] = 1 

    return disease_counts


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
	
    