import re


# function needed to remove the quotations, in the form [.], from a string 
def remove_quotes(x):
    # using regex, finding all substrings contained between the characters '[' and ']'
    #'quotes' is a list with all those characters, we loop over all of them, and then delete them from 'x'
    quotes = re.findall(r'\[(.+?)\]', x)
    for i in range(len(quotes)):
        x = x.replace('[{}]'.format(quotes[i]), '')
    return (x)


# this function splits 2 words if they are attached and the second one starts with an uppercase. 
# this happens many times when there are more than 1 names in 'music', 'starring'...
def split_names(a):
    for i in range(1,len(a)):
        # when we encounter an upper case letter and the previous is not a tab, we split the word
        if (a[i].isupper() == True) & (a[i-1] != ' '):
            a = a[:i] + ' ' + a[i:]
    return a


# function neede to get the movie title from the wikipedia page title
def get_title(title):
    # titles can come in this format [...] - (1987 American film) - Wikipedia
    # we clean the title from the final word and everything in the brackets.
    bra = re.findall(r'\((.+?)\)', title)
    for i in range(len(bra)):
         title= title.replace(' ({})'.format(bra[i]), '')
    title = title[:-12]
    return title