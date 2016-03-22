

# Parse shows files

def split_show_views(line):
	"""
	splits and parses each line of the dataset
	"""
    # <INSERT_CODE_HERE>
    return (show, views)

# Then you can use this function to transform the input RDD:
# show_views = show_views_file.<INSERT_CODE_HERE>(split_show_views)

# Parse channel files
def split_show_channel(line):
    # <INSERT_CODE_HERE>
    return (show, channel)

# Use it to parse the channel files:
# show_channel = show_channel_file.<INSERT_CODE_HERE>


# joined_dataset = <INSERT_CODE_HERE>


def extract_channel_views(show_views_channel): 
    # <INSERT_CODE_HERE>
    return (channel, views)

# channel_views = joined_dataset.<INSERT_CODE_HERE>(extract_channel_views)

def some_function(a, b):
    # <INSERT_CODE_HERE>
    return some_result

# channel_views.<INSERT_CODE_HERE>(some_function).collect()
