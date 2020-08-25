################################################################################################################################

# UNIVERSAL RISE CODING TEST

##############



##### TEST CODE BELOW

# Python code will loop through list of strings. Those strings whose lengths exceed a threshold 
# are appended to a list called long_names. The remainder are appended to a list called 
# short_names. The number of elements in each list is then printed.
# NB remember this is Python so indexing starts at 0.
import numpy as np
# set up empty list to append to, and define threshold string length
long_names = ()
short_names = []
threshold = 4
# list of strings
names = [‘dog’ , ‘cat’, ‘mouse’, ‘horse’, ‘cow’, ‘elephant’]
# loop through list of strings, check length and append to relevant list
for i in np.arange(1,len(names),1):    
              if len(names[i]) > threshold:
                             long_list.append(names[i])
              elseif:
                             short_list.append(names[i])
print(“length of long_names = , long_names”)
print(“length of short names = ”, len(short_names))




##### CORRECTED CODE BELOW

import numpy as np
# set up empty list to append to, and define threshold string length

long_names = []
short_names = []
threshold = 4

# list of strings
names = ['dog' , 'cat', 'mouse', 'horse', 'cow', 'elephant']

#  loop through list of strings, check length and append to relevant list
for i in np.arange(0,len(names),1):    
  if len(names[i]) > threshold:
    long_names.append(names[i])
  else:
    short_names.append(names[i])

print("length of long names = ", len(long_names))
print("length of short names = ", len(short_names))
