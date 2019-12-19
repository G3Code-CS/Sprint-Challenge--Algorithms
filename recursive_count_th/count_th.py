import math


'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Initializing the counter value to be returned
    count = 0

    # If the length of the word is less than 2 then there is no possibility of finding 
    # the match and returns 0
    if len(word) <= 2:
        return 0
    
    # This is the recursive function which recurses once called
    def countVal(word, count, position):

        # Base criteria for recursion stop
        if (len(word) == position+1):
            return count
        
        # Checks if the letter and the next letter matches to 'th'
        if word[position] + word[position+1] == 'th':
            count = count + 1
        
        # Goes to the next position
        position = position + 1
        return countVal(word, count, position)
    
    # The first call to the recursion function
    return countVal(word, count, 0)

    

print(count_th("the king is the best thing"))

