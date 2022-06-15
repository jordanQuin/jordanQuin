def erase_efficace(cc):
    tabStr = cc.split()
    
    if len(tabStr) > 0:
        nbSB = 0
        nbSA = 0

        while cc[nbSB] == ' ':
            nbSB += 1

        if cc[len(cc) - 1] == ' ' and cc[len(cc) - 2] == ' ':
            nbSA = len(cc) - 2
            while cc[nbSA] == ' ':
                nbSA -= 1

            nbSA = len(cc) - nbSA - 1 

        newStr = tabStr[0]
        i = nbSB

        for j in range (0, len(tabStr) - 1):
            i += len(tabStr[j])

            if cc[i + 1] == ' ':
                while cc[i + 1] == ' ':
                    newStr += ' '
                    i += 1

                newStr += ' '
                i += 1

            else:
                i += 1

            newStr += tabStr[j + 1]

        newStr = ' '*nbSB + newStr + ' '*nbSA
    else:
        newStr = ''


    return newStr

print(erase_efficace('  Cou cou   J M  B  '))
               