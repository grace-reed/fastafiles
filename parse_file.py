#!/usr/bin/env python
#parse_file.py

#to use regular expressions import re
import re

#set the file path to genome of interest
genome_path='/path/to/file'

#initialize the counter 
line_count = 0

#initialize a sequence variable
seq = ''

with open(genome_path) as genome:
    for line in genome:
        #increment line count by one
        line_count +1
        #if the line count is less than five
        if line_count < 5:
        #check to see if the line is a header line (starts with >)
            if re.match('^>', line):
                #print the header
                print(line)
      else:
        #this is a sequence line so append to seq
        seq+=line
tbc ... 
