#%%
'hello'[0]

#%%
'hello'[1]


#%%
'hello'[2]


#%%
'hello'[3]


#%%
'hello'[4]


#%%
'hello'[5]
#error message makes sense since rather than going from 1-5, python counts 0-4

#%%
'hello world'[0:3]

#%%
'2112'[0:3]

#%%
''[0]
''[0:1]

#%%
'hello world'[0:500]

#%%
'hello world'[450:500]

#%%
'hello world'[1:]

#%%
greeting = 'hello world'

#%%
greeting[0].upper() + greeting[1:]

#%%
'abcdefgh'[0:9:2]

#%%
'abcdefg'[::2]

#%%
'hello world'[-1:]

#%%
'hello world'[-3]

#%%
'HELLO World'.lower()

#%%
original = 'Burma Shave'
lowercase = original.lower()
lowercase

#%%
orignal

#%%
wyatt = 'They flee from me that sometime did me seek / With naked foot, stalking in my chamber.'

#%%
wyatt = wyatt.lower()

#%%
wyatt

#%%
print(c)

#%%
for c in wyatt:
    print(c)

#%%
for i in range(len(wyatt)):
    print(wyatt[i])

#%%
for i in range(len(wyatt)):
    print(i, wyatt[i])

#%%
for i in range(len(wyatt)):
    print wyatt[i:i+2]

#%%
for i in range(len(wyatt)): 
    print wyatt[i:i+2]

#%%
pairs = 0
for i in range(len(wyatt)): 
    if wyatt[i:i+2] == 'ee':
        pairs = pairs + 1

#%%
pairs = 0
for i in range(len(wyatt)):
    if wyatt[i] == wyatt[i + i]:
        pairs = pairs + 1

#%%
pairs

#%%
wyatt[86]

#%%
pairs = 0
for i in range(len(wyatt)-1):
    if wyatt[i] == wyatt[i+1]:
        pairs = pairs + 1

#%%
#Paused on page 10/29 of chapter 8