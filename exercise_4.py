#!/usr/bin/env python
# coding: utf-8

# # Algorithmic Question

# You are given a string, s. Let's define a subsequence as the subset of characters that respects the order we find them in s. For instance, a subsequence of "DATAMINING" is "TMNN". Your goal is to define and implement an algorithm that finds the length of the longest possible subsequence that can be read in the same way forward and backwards. For example, given the string "DATAMININGSAPIENZA" the answer should be 7 (dAtamININgsapIenzA).

# # Algorithm

# ##Step 1 : Given a String "string" Find the length of it

# #Step 2 : Find whether the String is Palindrome or not by using string reverse.  If its palindrome return the original length of the string
# 

# ##Step 3: Find the Substrings of the length greater than or equal to 1 and lesser than length of the string.

# #for finding substring using combinations below, where order of the letters matters

# #Repeat the step from the length of the string decending till 1

# In[7]:


from itertools import combinations
#method to check reversibility of a given string
def palindrome(S):
    reverse = S[::-1]
    if S==reverse:
        return True
    else:
        return False
#Algorithm
def algorithm(string):
    #length of the string
    length = len(string)
    
    if palindrome(string):
        #can be stopped here if the given string itself a palindrome and the above condition satisfied
        print(length,"(",string.upper(),")")
    else:
        length -=1
        #making string into lower
        string=string.lower()
        #looping till its length 1
        while length>1:
            #getting substring by using combinations 
            sub_strings = list(combinations(list(string),length))
            #flag to stop the iteration when the maximum size of substring found
            found = False
            #loop through substrings of length n-1...so on till 1
            for i in sub_strings:
                #making sub_string from list
                S = "".join(i)
                #checking reverse of string
                if(palindrome(S)):
                    #if its reverse print only the pattern in capitalize using below
                    s = list(string.lower())
                    c = i
                    j=0
                    #printing the combination 
                    for k in c:
                        while j != len(s):
                            if(k==s[j]):
                                s[j]=s[j].upper()
                                j+=1
                                break  
                            j+=1
                    #printing and flag found true and continue to find other substrings of same length as there are chances for others
                    print(length,"(","".join(s),")")
                    found = True
                    continue
                else:
                    continue
            #if its found terminate the loop
            if found == True:
                break
            #else reduce the length and iterate
            else:
                length -=1
        #if none found return length as 1
        if found == False:
            print(length)


#
string = "DATAMININGSAPIENZA"
algorithm(string)


# In[24]:


The Above Greedy Alogrithm to find the reversive sub_string below


# Step 1 of 4 - Input and Check whether palindrome
# step1 : Getting Input of string "S" of Length 'N'
# step2 : Check whether the reverse of the string 'R'( S[::-1] ) is equal to the string 'S'
# step3 : If it is equal return the length 'N' as the maximum length of the substring
# step4 : Else proceed with further steps below.
# 
# Step 2 of 4 - Reduce Length and Find Substrings
# step1 : Reduce Length of the string 'N-1' if N-1 > 1 do the steps below
# step2 : Convert string into a list of characters of length N-1
# step3 : Find the Combinations of the given array of string length being R(N-1) out of N characters 
# step4 : The number of combinations is 'K' ((N)! / R! . (N-R)!)
# step5 : Convert list into string for example ['a','b','c'] into 'abc'
#     
# Step 3 of 4 - Find whether the substrings are palindrome
# step1 : For each "Si" in Sub_strings where 0<i<K where K is the number of sub_strings
# step2 : Check whether The Sub_string is palindrome or not
# step3 : If its palindrome return the length of the sub_string 'N-1' as the maximum length of substring
# step3 : else repeat the steps for other sub_strings
# 
# Step 4 of 4 - Repeat the steps
# step1 : Repeat the steps 2 and 3 until the length of substring N-1 > 1 
# step2 : If None found N-1 == 1 then return 1 as the maximum length of substring
# 
