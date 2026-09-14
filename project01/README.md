# Introduction
Description of the project

# Pseudocode
Put pseudocode in this box:

```
parse_line(line)
- take a string as an argument
- extract AF_EXAC
- if AF_EXAC is not present, skip the line
- if AF_EXAC < 0.0001:
    - get associated diseases from CLNDN
    - do not count not_specified
    - do not count not_provided
    - return list of diseases
- if variant is not rare:
    - return empty list


read_file(filename)
- take a string as an argument for the file
- open the file
- read the file line by line
- pass each line to parse_line
- use a dictionary to count how many times each disease is observed
- return the dictionary
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
