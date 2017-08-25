# This line imports the argv class from the sys module
from sys import argv

# This line unpacks the arguments
script, filename = argv

# This line assigns the contents of the sample file to the variable txt
txt = open(filename)

# This line prints out a sentence with the filename formatted in
print "Here's your file %r:" % filename
# This line prints the contents of the sample file
print txt.read()
txt.close()

# These two lines ask a question and then take the sample filename in as input
print "Type the filename again:"
file_again = raw_input("> ")

# This line opens the sample file and saves its contents as txt_again
txt_again = open(file_again)

# This line prints the contents of the sample file
print txt_again.read()
txt_again.close()
