#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# <TV show, count>
# e.g Almost_News, 25
# a possible pseudo code example of how to implement this join using tv-show as the key:

# join2_mapper:

# read lines, and split lines into key & value

# if value is ABC or if value is a digit print it out
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------



for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 


    if value_in == "ABC" or value_in.isdigit() :

        print('%s\t%s' % (key_in, value_in))


#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value