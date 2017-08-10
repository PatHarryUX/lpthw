print "I will now count my chickens:"

# 25 plus 5 is 30
print "Hens", 25 + 30 / 6
# Multipliplication and modulus has the same precedence
# so the one on the left gets evaluated first:
# 100 - (75 % 4)
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + 0 - 0 + 6
# 1 + 6
# 7
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

# 5 is not less than -2, so this is evaulated as False
print 3 + 2 < 5 - 7

# 5
print "What is 3 + 2?", 3 + 2
# -2
print "What is 5 - 7", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

# True
print "Is it greater?", 5 > -2
# True
print "Is it greater or equal?", 5 >= -2
# False
print "Is is less or equal?", 5 <= -2
