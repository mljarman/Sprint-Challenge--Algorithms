'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # checking for 2 characters, 'th' so base case would be 1 character or less:
    if len(word) <= 1:
        return 0
    # look at first 2 characters in string, if it's 'th' and is lower case:
    if word[:2] == 'th' and word[:2].islower():
        # add 1 to the count and make recursive call to go through rest of word,
        # starting from first index.
        return 1 + count_th(word[1:])
    else:
        # if first 2 characters aren't 'th', make recursive call to go through
        # rest of word.
        return count_th(word[1:])
