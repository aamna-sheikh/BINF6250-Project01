# Introduction
In this project, we are parsing a Variant Call Format (VCF) file to identify and count rare diseases associated with a rare genetic variants, based on their ExAC alelle frequency. 

# Pseudocode

Put pseudocode in this box:

```
FUNCTION parse_line(line):

	IF line starts with #: 
		return empty list

	Split line by tabs
	Get INFO column

	Split INFO by semicolon to get key-value pairs

	Search INFO fields for AF_EXAC

	IF AF_EXAC is not present:
		RETURN empty list
	ELSE: 
		Get AF_EXAC value after '=' and store as AF_EXAC 
		Convert AF_EXAC to a float

		IF AF_EXAC >= 0.0001:
			RETURN empty list

		ELSE: 
			Search INFO fields for CLNDN
			Get CLNDN value after '='
			Split by | and store as disease_list

			Remove 'not_specified' and 'not_provided' from disease_list

			RETURN disease_list


FUNCTION read_file(file_name):

	Create empty dictionary disease_counts
	Open file file_name

	FOR each line in the file: 
		pass through parse_line function
		store value as diseases

		FOR each disease in diseases:
			IF disease is already a key in disease_counts:
				increase value by 1
			ELSE:
				add disease as key with value=1

	RETURN disease count dict


Call read_file with "clinvar_20190923_short.vcf"

Print results from read_file

```

# Successes
Description of the team's learning points

# Struggles
Description of the stumbling blocks the team experienced

# Personal Reflections
## Group Leader
Group leader's reflection on the project

## Other member
Other members' reflections on the project

# Generative AI Appendix
As per the syllabus
