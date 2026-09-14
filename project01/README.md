# Introduction
In this project, we are parsing a Variant Call Format (VCF) file to identify and count rare diseases associated with a rare genetic variants, based on their ExAC alelle frequency. 

# Pseudocode

Put pseudocode in this box:

```

#!/usr/bin/env python
from pprint import pprint


# parse_line fucntion
FUNCTION  def parse_line(line: string) -> list of strings

columns = split line by tab character #.split("\t")

    info_field = columns[7]              
    info_items = split info_field by ";" #.split(";") 

    af_exac_value = NOT FOUND

FOR each item in info_items:
        IF item starts with "AF_EXAC=": #startswith("AF_EXAC")
            raw_value = part of item after "=" #raw_value= item.split("=")[1]
            IF raw_value contains ",":
                af_exac_value = float of (raw_value split by "," )[0]
            ELSE:
                af_exac_value = float(raw_value)
            (BREAK out of loop ) 

    IF af_exac_value == NOT FOUND:
        RETURN empty list

    IF af_exac_value >= 0.0001:
        RETURN empty list       
        
    disease_list = empty list

    FOR each item in info_items:
        IF item starts with "CLNDN=":
            raw_diseases = part of item after "="
            replace "|" with "," in raw_diseases
            disease_names = split raw_diseases by ","

            FOR each name in disease_names:
                trimmed_name = strip whitespace from name #trimmed_name=name.strip()
                IF trimmed_name is empty:
                    CONTINUE to next name
                IF trimmed_name == "not_specified" OR trimmed_name == "not_provided":
                    CONTINUE to next name
                ADD trimmed_name to disease_list
            BREAK out of loop  # found CLNDN, no need to keep searching

    RETURN disease_list

# -----------------------------------------------------
# read_file function
FUNCTION def read_file(filename: string) -> dictionary
  results = empty dictionary   #results = {}

    OPEN filename FOR READING as file #with open (filename , "r") as file:
        FOR each line in file :
            diseases = parse_line(line)

            FOR each disease in diseases:
                IF disease already a key in results:
                    results[disease] = results[disease] + 1 # results[disease] += 1
                ELSE:
                    results[disease] = 1
    CLOSE file

    RETURN results



if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
    




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
