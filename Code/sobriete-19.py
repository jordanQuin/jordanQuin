import string

def erase(message: string):

    '''
        Author       : xxx Anonymized by JMB xxx
        Version      : 1.1
        Date         : 08-06-2022
        
        Description  : Takes a string parameter and remove simple spaces, not double, inside of it.
        
        Return       : String
    '''

    # Reflexion 
        # A String is an array of char type variables in its primary form.
        # 
        # Adept and fascinated of recursive algorithms, I've made one for this project !
        # 
        # The reasonning is purely primitive but very efficient because it doesn't include a lot of comparisons.
        # It's based on array accesses.
        #
        # I will train to through the algorithm to explain his functionning with a little game.
        #
        # In this game you are a char, the first one of the queue, and you don't know who are behind you.
        # If you are a space char, you are in love with another space char, every moment of your life should be lived together...
        # Be sure to never lose your partner of life ! 
        
        #   Who am I ?
    if message == "": # Am I even real ? No...
        return message # So I just return myself : the void
    
        #   So I know that I'm not the void, am I space ?
    if message[0] != ' ': # Surely not, you are discussing to the wrong person
        return message[0] + erase(message[1:]) # I enter the Valallah and the purge continues !

        #   Yeah it's me ! The famous and beautiful space char ;)
    else:
        if len(message) > 1: # *you look behind* Am I the last one standing ?

                    # Hehe somebody is behind, that's nice
                if message[1] == ' ': # IT'S IT ! MY SPACE LOVER
                    return '  ' + erase(message[2:]) # WE ENTER THE VALHALLA TOGETHER ! And the purge continues (next episode)...
                else: # Oh no, I've lost my space love ...
                    return erase(message[1:]) # I cannot enter, i'll find it before ! Do not wait me ! And let the purge continue without me !

        else: # Oh no, I've lost my space love ... Nobody is behind me ...
            return '' # I cannot enter, i'll find it before ! Do not wait me !