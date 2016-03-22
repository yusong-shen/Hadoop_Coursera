
# Mapper for fileA


def split_fileA(line):
    # split the input line in word and count on the comma
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    # turn the count to an integer  
    word     = key_value[0]   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 
    count =  int(value_in)
    return (word, count)



# Mapper for fileB

def split_fileB(line):
    # split the input line into word, date and count_string
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    key_in     = key_value[0].split(" ")   #key is first item in list
    value_in   = key_value[1]   #value is 2nd item 
    word = key_in[1]
    date = key_in[0]
    count_string = value_in
    return (word, date + " " + count_string) 




# Test
# test_line = "able,991"
# print split_fileA(test_line)

test_line = "Dec-15 able,100"
print split_fileB(test_line)