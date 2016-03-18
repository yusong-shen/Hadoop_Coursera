#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# join2_reducer:

# read lines and split lines into key & value

# if a key has changed (and it's not the first input)

# then check if ABC had been found and print out key and running total,

# if value is ABC then set some variable to mark that ABC was found (like abc_found = True)

# otherwise keep a running total of viewer counts


#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

last_key = None
running_total = 0
abc_found = False 

line_cnt           = 0  #count input lines

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     

    # e.g  (Almost_News, ABC)
    #       (Almost_News, 35)
    #note: for simple debugging use print statements, ie:  
    curr_key  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    # check if key has changed
    # if not, add value to running total
    if curr_key == last_key :
        # if value is ABC then set some variable to mark that ABC was found 
        if value_in == "ABC" :
            abc_found = True;
        else :
            running_total += int(value_in)
    else :
    # a key has changed (and it's not the first input) 

        # check if it's not the first input
        if line_cnt > 1:
            # check if ABC had been found
            if abc_found :
                # print out the last key and running total
                print( "{0}\t{1}".format(last_key, running_total) )
                # reset "ABC" to not found
                abc_found = False

        # reset values
        if value_in == "ABC" :
            abc_found = True;
        else :
            running_total = int(value_in)

        last_key = curr_key


# ---------------------------------------------------------------
#now write out the LAST join result
# ---------------------------------------------------------------

if last_key == curr_key and abc_found:
    print( "{0}\t{1}".format(last_key, running_total))
