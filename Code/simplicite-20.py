import string

def erase(message: string):
    
    '''
        Author       : xxx Anonymized by JMB xxx
        Version      : 2.0
        Date         : 08-06-2022
        
        Description  : Takes a string parameter and remove simple spaces, not double, inside of it.
        
        Parameter    : String (not empty)
        Raise        : ValueError if the length of the String is zero
        Return       : String
    '''
    
    # Conditions and raises
    if len(message) == 0:
        raise ValueError('Message vide')
    
    # Reflexion 
        # A String is an array of char type variables in its primary form.
        # I'm using this particularity to treat the problem as basic as it can be possibly imagined.
        #
        # The algorithm go through the message by acessing character by character.
        # It implements it in a list by comprehension following simple conditions :
        #   - Am I a character different of space ?                             ->      Added
        #   - I'm a space but the precedent or the next character is space too  ->      Added
        #   - I'm a space but none of my neighbours are spaces                  ->      Not Added
        #
        # By using this method, a physical problem can be raised on the first and the last char.
        # This is due, respectively, to the abscence of a predeccessor char and a successor char.
        # So I decided to not surchage the whole algorithm by using more conditions.
        # I manage to treat this particular cases after the completion of the list.
        #
        # Another problem could be an "insufficient" string, not sufficient in terms of chars.
        # So if the user uses a String with the length of 2 :
        # We do not have to enter the algorithm because if the first or second character is a space,
        # we just return the other one.
    
    # Algorithm and explanations
        # CASE : LENGTH OF 1
    if len(message) == 1 :
        if message == ' ':
            return ''
        else:
            return message
        
        # CASE : LENGTH OF 2
    if len(message) == 2 :
        if message == '  ':
            return message
        elif message[0] == ' ':
            return message[1]
        else:
            return message[0]
    
        # ALGORITHM
            # Construction of a list of the chars in the message by comprehension
            # The char is added if it fits the criterias mentionned in REASONNING part (lines 27-28-29)
            # We are in the range of 1 to -1 so from the second character to the second to the last
    messageErased = [message[i] for i in range(1, len(message)-1) if message[i] != ' ' or message[i+1] == ' ' or message[i-1] == ' ']
            # We add the last char    if this isn't space   or if the last and the second last chars forms a double space
    messageErased.append(message[-1]) if message[-1] != ' ' or message[-2] + message[-1]  == '  ' else None
            # And we insert in first position in the list the first char of the message if this isn't a simple space
    messageErased.insert(0, message[0])  if message[0]  != ' ' or message[1] == ' '  else None
            # return a new String composed of the list of chars
    return ''.join(messageErased) # join permits to add every char in order in the empty String