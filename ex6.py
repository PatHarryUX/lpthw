# The integer 10 is put where the %d is
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Two strings are being formatted into the longer string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Concatination
print w + e
