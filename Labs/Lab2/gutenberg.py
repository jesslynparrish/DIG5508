#%%
#A big problem I had with both parts of Lab 2 is that the Jupyter notebooks wouldn't show me any results - it would give me error messages, but not if anything happened or not. I don't know if this is because I didn't have a command to print results or if there was another problem.
# [2-1] ON YOUR OWN:

# Choose a text that was not previously analyzed above from Project Gutenberg.
# 1. Write code that retrieves and writes the text to a file in the current projeect.ZeroDivisionError

#Okay, for this problem, I thought it was fairly similar to the code that was laid out in the beginning of this jupyter notebook and the main thing that needed to be changed was the path to the new text file.
import gutenberg
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob

text = strip_headers(load_etext(2701)).strip()
blob = TextBlob(text)
source = open('Labs/Lab2/frankenstein.txt','w',encoding="utf-16",newline='\n')
source.write(text)
source.close()
#%%
# 2. Write code that retrieves the text (if downloaded) 

source = open('Labs/Lab2/frankenstein.txt','w',encoding="utf-16",newline='\n')

#I copied code from earlier in this notebook file and changed the path to the new text file
#%%
# 3. Create a TextBlob from the string that was retrieved either by API or the that contains only the contents of the text. This may involve locating the end of the header. Save the resulting TextBlob for use in the following cells in the variable "gut_text"

text = strip_headers(load_etext(2701)).strip()
blob = TextBlob(text)
#I don't really understand how TextBlob works, this was purely guesswork.
#%%
# [2-2] ON YOUR OWN:
from operator import itemgetter
# Write code that finds the top 5 longest sentences in the work. 

#My logic here is that by changing the max, it should increase the amount of sentences given for the output
blob = ("This is the longest. No this is. Nope, I am. No. Yes.") #Why do we need the blob?
list = []
list.append(0)
list.append(4)
list.append(100)
list.append(40)
list
[0,4,100,40]
sorted(list)
#tuple is a 2-dimensional array
#we're using a tuple because it has a set/unchangeable value
#a splice is a subset of a list
    # example of splice code: list[-5:] - this command would give the last 5 items in a list
#the index refers to the point before the item
#you're sorting the list in a tuple, with the tuple - i do not understand how you get the 5 sentences. I understand that once you have the 5 sentences you can put them in a tuple, but how do we modify the function to get the 5 longest sentences and not just the one longest sentence?!?!
from textblob import TextBlob
mylist = []
max = 0
index = 0
for key, sentence in enumerate(blob.sentences):
    mylist.append((sentence,len(sentence.words)))
    if(len(sentence.words) < max):
        #mytuple = (sentence,len)
        max = len(sentence.words)
        index = key
        print(result)

sorted(mylist,key=itemgetter(2))

#%%
# [2-3] ON YOUR OWN:

# Using the code above for figures, create a new table that lists the top 10 most frequent words and how many times they occur in that text.

import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(header=dict(values=['Word', 'Frequency']),
                 cells=dict(values=[[_, _, _, _, _, _, _, _, _, _, ], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))
                     ])

#I thought that the main items I needed to adjust here was to change the values to 'word' and 'frequency' and put in placeholders for where the values would go to correspond with 1st-10th greatest frequency. I didn't get as far as figuring out how to get it to work.

#I also had trouble installing 'conda install -c plotly' to do the table. I received an error message in Terminal when I tried