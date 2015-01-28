"""
    I recently took a web course through http://www.codecademy.com to brush up 
    on my Python skills. There was one exercise that asked the user to create a 
    function that would take two strings: the first is a text string, and second
    is a text string of a word to be censored out with asterisks. However, I 
    thought I would take the exercise a bit further replace parts of words that 
    matched the word to be censored. This is somewhat similar to the "replace" 
    method. 
"""

def censor(text, word):
    
    """
    This censor function searches the text string for the word string and 
    replaces matches with asterisks. We assume the input strings won't contain 
    punctuation or upper case letters.
    
    For example if I am censoring the word "hack" from a sentence consisting of 
    the word "hacking," it should be converted to "****ing."
    """
    
    if len(text) < len(word):
        
        # If length of text string is longer than length of word string,
        # word string cannot be in text string, so set result equal to
        # the original text string
        
        result = text
    
    else:  
        
        result = list(text)
        possible_locations = []
        
        for i in xrange(len(text)):
        
        # Check for locations in text string where the first letter
        # of the word string appears, and add the index of this 
        # location to possible locations 
           
            if text[i] == word[0]:
                possible_locations.append(i)
        
        # print possible_locations  # for testing only
        
        
        for i in possible_locations:
            
        # check for and remove locations where the word string 
        # cannot fit as its length at the possible index would 
        # exceed the length of the text string 
            
            if i + len(word) > len(text):
                possible_locations.remove(i)
        
        # print possible_locations # for testing only
        
        definite_locations = []

        for i in possible_locations:
            
            # iterate over the possible locations to
            # search for definite locations
            
            j, still_possible = 0, True
            while still_possible == True and j < len(word):
                if text[i+j] != word[j]:
                    still_possible = False
                j += 1
            if still_possible == True:
                definite_locations.append(i)
        
        # print definite_locations # for testing only
        
        for i in definite_locations:
            for j in xrange(len(word)):
                result[i+j] = "*"
                
        result = "".join(result)

    print result # for testing only     
    return result 
    
"""
Here are som examples to test:
     
censor("max is so maxy and m max ma","max")
censor("abc123","abc123")
censor("abc12","abc123")
censor("abc123","abc12")
censor("noah is not on noah's arc because no noah would know","noah")
"""