

# Parse shows files
# <TV show, views>
# e.g Almost_News,25

def split_show_views(line):
	# 	splits and parses each line of the dataset
    line  = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    show     = key_value[0]   #key is first item in list
    views   = int(key_value[1])   #value is 2nd item 
    return (show, views)

# show_views_file = sc.textFile("input_a2join/join2_gennum*.txt")

# Then you can use this function to transform the input RDD:
# show_views = show_views_file.map(split_show_views)

# Parse channel files
# <TV show, channel>
# e.g Hourly_Sports,DEF

def split_show_channel(line):
    line   = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line, into key and value, returns a list
    show     = key_value[0]   #key is first item in list
    channel   = key_value[1]   #value is 2nd item 	
    return (show, channel)

# show_channel_file = sc.textFile("input_a2join/join2_genchan*.txt")

# Use it to parse the channel files:
# show_channel = show_channel_file.map(split_show_channel)

# use the join transformation to join the 2 dataset using the show name as the key.
# <TV show, (views, channel) >
# joined_dataset = show_channel.join(show_views)


# Extract channel as key

# <TV show, (views, channel) >
def extract_channel_views(show_views_channel): 
    views = int(show_views_channel[1][0])
    channel   = show_views_channel[1][1] #value is 2nd item 	
    return (channel, views)

# Now you can apply this function to the joined dataset to create an RDD of channel and views:
# channel_views = joined_dataset.map(extract_channel_views)

# Finally, we need to sum all of the viewers for each channel:
def sum_across_channels(a, b):
    # <INSERT_CODE_HERE>
    return a + b

# channel_views.reduceByKey(sum_across_channels).collect()


# test
line = "Almost_News,25"
print split_show_views(line)

line = "Hourly_Sports,DEF"
print split_show_channel(line)


