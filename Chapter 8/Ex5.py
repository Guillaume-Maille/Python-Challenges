import string

def ex5(text):
    x_no_punct = ''
    ecount = 0
    wcount = 0
    for letter in text:
        if letter not in string.punctuation:
            x_no_punct += letter
    for i in text:
        if i == 'e':
            ecount += 1
        else:
            wcount += 1
    eper = ecount/wcount*100
    print(wcount)
    print(ecount)
    print("Your text contains {0} words, of which {1} ({2:.1f}%) contain an 'e'.".format(wcount, ecount, eper))

x = "The killer whale or orca (Orcinus orca) is a toothed whale belonging to the oceanic dolphin family, of which it is the largest member. Killer whales have a diverse diet, although individual populations often specialize in particular types of prey. Some feed exclusively on fish, while others hunt marine mammals such as seals and other species of dolphin. They have been known to attack baleen whale calves, and even adult whales. Killer whales are apex predators, as no animal preys on them. A cosmopolitan species, they can be found in each of the world's oceans in a variety of marine environments, from Arctic and Antarctic regions to tropical seas, absent only from the Baltic and Black seas, and some areas of the Arctic Ocean."

ex5(x)
