# -*- coding: utf-8 -*-
"""
Modified lcs_with_stopwords.py to work as an import for datagen_par.py

@author: Vince Sing Choi
"""

# FindLCS takes in 2 arrays a, d which contain a: the acroynm -
# and d: the leaders of the possible candidates -
# it will also take in an index to choose from and the start and finish indices
# it will then compute and return a reconstruction matrix


def FindLCS(a, d, index, start, end):
    n = len(a[index]) + 1
    m = end - start + 1
    # print m
    # print n

    c = [[0 for i in range(m)] for j in range(n)]
    b = [["Nope" for i in range(m)] for j in range(n)]

    for i in range(n):
        c[i][0] = 0
    for j in range(m):
        c[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            #print ("comparing: ", a[index][i-1], " with :" , d[start+j-1])
            if a[index][i-1] == d[start+j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "Diag"				# 1 - Top left diagonal
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "Up" 		# 2 - Up
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "Left"			# 3 - Left

    # print c
    # print b
    #print ("Found LCS for: ", a[index])
    b.append(c[i][j])
    return b


# ParseBack takes in the reconstruction matrix and parses back to find the leaders acroynm definition
def ParseBack(b):
    directions = []
    done = False
    i = -1
    j = -1

    while not done:
        if b[i][j] == "Nope":
            done = True
        if b[i][j] == "Diag":
            directions.append(len(b[i]) + j)
            i = i - 1
            j = j - 1
        elif b[i][j] == "Up":
            i = i - 1
        elif b[i][j] == "Left":
            j = j-1
    return directions


def findacronym(stopwords, paragraph):
    # takes list of stopwords and a paragraph and outputs the acronyms found if any
    passage = paragraph

    # print (passage)
    # Here passage contains the input data file. passage[0][0] refers to the first line, first word

    # local variables for keeping track of leaders, acroynms and definitions
    # numlines, numwords, numletters keeps track of the size of each subarray
    leaders = []
    acronym = []
    wordindex = []
    definition = []
    tempdef = []
    tempdef2 = []
    isacronym = True
    numwords = 0
    numletters = 0
    wordcount = -1
    prelcs = 0
    postlcs = 0

    # loop to store leaders and find acronyms (consecutive capitals between 3-10)
    numwords = len(passage)
    #print (numwords, " words in line ", i)
    for i in range(numwords):
        numletters = len(passage[i])
        #print (numletters, " letters in word, ", passage[i][j])
        # special case for line feed
        if numletters == 0:
            leaders.extend(" ")
            isacronym = False

        for j in range(numletters):
            if (j == 0):
                wordcount = wordcount + 1
                if (not (passage[i] in stopwords)):
                    leaders.extend(passage[i][j].upper())
                else:
                    leaders.extend("*")

            if (numletters < 3 or numletters > 10):
                isacronym = False
                break

            if (passage[i][j].islower()):
                isacronym = False
                break

            if (passage[i][j].isdigit()):
                isacronym = False
                break

        if(isacronym and passage[i] not in acronym):
            print("new acronym: " + str(passage[i]) + " found")
            acronym.append(passage[i])
            wordindex.append(wordcount)
        isacronym = True

    # print leaders
    # print acronym
    # print wordindex

    # Booleans to determine whether or not the starting/ending index of a window is at the start or end
    si = False
    ei = False
    
    
    print ("acronym detected: " + str(len(wordindex)))
    if (len(wordindex) == 0):
        return definition 

    for k in range(len(wordindex)):
        # print leaders[wordindex[k]]
        # print passage[wordindex[k]]
        window = len(acronym[k]) * 2
        # special cases prewindow
        if wordindex[k] - window < 0:
            si = True
            temp = FindLCS(acronym, leaders, k, 0, wordindex[k])
        else:
            #print("prewindow is fine")
            si = False
            temp = FindLCS(acronym, leaders, k,
                           wordindex[k] - window, wordindex[k])

        # special cases post window
        # print numwords
        # print wordindex[k] + window
        if wordindex[k] + window >= numwords:
            ei = True
            temp2 = FindLCS(acronym, leaders, k, wordindex[k]+1, numwords)
        else:
            ei = False
            temp2 = FindLCS(acronym, leaders, k,
                            wordindex[k]+1, wordindex[k] + window + 1)

        # print temp
        # print temp2
        prelcs = temp[-1]
        del temp[-1]
        postlcs = temp2[-1]
        del temp2[-1]

        # compare pre and post windows for LCS
        if prelcs > postlcs:
            # print "use prewindow"
            #print ("acronym found at: " , wordindex[k])
            #print ("window is: ", window)
            temp3 = ParseBack(temp)
            #print ("temp3 = " , temp3 )
            # for i in range(len(temp3) -1, -1, -1):
            if si == True:
                #print ("temp3 at this time is: " , temp3[i])
                #print (passage[0 + temp3[i]-1])
                # print temp3[-1]
                # print temp3[0]
                for i in range(temp3[-1], temp3[0]+1):
                    somestring = passage[0 + i - 1]
                    tempdef.append(somestring)
            else:
                for i in range(temp3[-1], temp3[0] + 1):
                    somestring = passage[wordindex[k] - window + i - 1]
                    tempdef.append(somestring)

            tempdef2 = " ".join(map(str, tempdef))
            size = len(tempdef)
            j = 0
            while j != size:
                j = j+1
                del tempdef[0]
            print(" ".join((acronym[k], " - ", tempdef2)))
            definition.append(" ".join(acronym[k]))

        else:
            # print "use postwindow"
            temp3 = ParseBack(temp2)
            #print ("temp3 : ", temp3)
            if ei == True:
                for i in range(temp3[-1], temp3[0]+1):
                    somestring = passage[wordindex[k] + i]
                    tempdef.append(somestring)
            else:
            	for i in range(temp3[-1], temp3[0]+1):
            		somestring = passage[wordindex[k] + i]
            		tempdef.append(somestring)

            tempdef2 = " ".join(map(str, tempdef))
            size = len(tempdef)
            j = 0
            while j != size:
                j = j+1
                del tempdef[0]
            print(" ".join((acronym[k], " - ", tempdef2)))
            definition.append(" ".join(acronym[k]))
    return (definition)