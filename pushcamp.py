import sys
from camping import SUCCESS_EMOJI
from pushbullet import Pushbullet
import numpy as np
import sys

#Make sure your API key is specified in sys.argv[1] position
pb = Pushbullet(sys.argv[1])

available_site_strings = []
old_available_site_strings = []

for line in sys.stdin:
    line = line.strip()
    if "There are campsites" in line:
    	first_line = line
    	# available_site_strings.append("\n" + first_line + ":")
    	print()
    	new_line = first_line.split('from ')
    	# print(new_line[1])
    	# print(first_line)

    if SUCCESS_EMOJI in line:
        name = " ".join(line.split(":")[0].split(" ")[1:])
        available = line.split(":")[1][1].split(" ")[0]
        s = "{}: {} site(s) available in {} ".format(new_line[1], available, name)
        available_site_strings.append(s)
        print("%s %s" % (SUCCESS_EMOJI, s))
        joined_string = "\n".join(available_site_strings)
        # print(joined_string)


with open('old_available.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]

        # add item to the list
        old_available_site_strings.append(current_place)



# old_available_site_strings = ['2020-07-24 (None) to 2020-07-27 (None): 7 site(s) available in INDIAN COVE CAMPGROUND (232472) ', '2020-07-31 (None) to 2020-08-03 (None): 6 site(s) available in INDIAN COVE CAMPGROUND (232472) ', '2020-08-07 (None) to 2020-08-10 (None): 7 site(s) available in INDIAN COVE CAMPGROUND (232472) ']
npdiff_list = np.setdiff1d(available_site_strings, old_available_site_strings, )
npdiff_list2 = npdiff_list.tolist()
npdiff_list3 = ("\n \n".join(npdiff_list2))
print(npdiff_list3)

if not npdiff_list3:
	pass
else:
	push = pb.push_note("Campground Availability Update", "%s" % npdiff_list3)

	with open('old_available.txt', 'w') as filehandle:
	    for listitem in available_site_strings:
	        filehandle.write('%s\n' % listitem)

	with open("old_available.txt", "rb") as txt:
	    file_data = pb.upload_file(txt, "Master_Availability.txt")

	push = pb.push_file(**file_data)
