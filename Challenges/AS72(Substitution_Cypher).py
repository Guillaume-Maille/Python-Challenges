########################################################################################################################

# https://docs.google.com/forms/d/e/1FAIpQLSfR1DK0HBOTJ_wcTUHqivIi-MGhELTTblj-jxC7NYRyeiUESw/viewform?entry.761381367=AS72&entry.408774996
# Can you create a substitution cipher which uses a random generated sequenced alphabet to encrypt a custom message?
########################################################################################################################

import random

from random import shuffle

a = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

########################################################################################################################

x = input()

shuffle(a)

print(a)
