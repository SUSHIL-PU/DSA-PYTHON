#   KMP Search algorithm for pattern search in a text string.
#       TIME COMPLEXITY : O(N) 
# 
#  given two string a text and a pattern.. Have to find out the indexes of the pattern that can be found in text.
#    

def preprocess(pat):
    lps = [0]* len(pat)    # lps is a list of size len(pat) having all element as 0.
    i = 0                  # lps store the Longest Prefix Sufix for the pat
    j = 1
    while j < len(pat):
        if pat[i] == pat[j]:
            i += 1
            lps[j] = i
            j += 1
        else:     # when pat[i] != pat[j]
            if i == 0:     
                lps[j] = 0
                j += 1
            else:
                ind = i - 1
                i = lps[ind]

    return lps



def kmpSearch(text, pat):
    lps =  preprocess(pat)   # to find out the longest prefix-suffix as a integer list
    # print(lps)
    indText = 0
    indPat = 0
    while indText < len(text):
        if text[indText] == pat[indPat]:
            indText += 1
            indPat += 1
        if indPat == len(pat):
            print("Found at index", indText-len(pat))
            indPat = lps[indPat - 1]
        elif indText < len(text) and text[indText] != pat[indPat]:
            if indPat == 0:
                indText += 1
            else:
                indPat = lps[indPat - 1]


# ----------------------------------------------------------------------------------------
#           Brute force approach
#       TIME COMPLEXITY  :   O(N * M)
# 
# 
# def searchPat(text, pat):
#     i = 0 # index of text
#     j = 0 # index of pat

#     while i < len(text):
#         if text[i] == pat[j]:
#             i += 1
#             j += 1
#         if j == len(pat):
#             print('Found at index ', i - len(pat))
#             break
#         if i < len(text) and j < len(pat) and text[i] != pat[j]:
#             j = 0
#             i += 1
# ---------------------------------------------------------------------------------------        
        

text = input('Enter the full text : ')
pattern = input('Enter the pattern to be search : ')
# searchPat(text, pattern)
kmpSearch(text, pattern)


# --------------------------------------------------------------------------------------------
#                  OUTPUT
# Input :
#       Enter the full text : Hello sushil this is sushil
#       Enter the pattern to be search : sushil
#  Output :
#       Found at index 6
#       Found at index 21