#%%
def plusOne (value1):
    return value1 + 1

#%%
puppy = 121
kitten = 212
stingray = 42
snake = 81
sloth = 253
#%%
x = 5
plusOne(x)
x = 6
plusOne():

#%%
plusOne(x)
x = plusOne(x)
print(x)

#%%
# a, b
#5, 2
sum = 0
secondSum = 0
for x in range(100):
    sum = sum + x
    secondSum = secondSum + x * x 

#%%
def double(input):
    for x in input:
        print(x*2)

#%%
def exponent(x, y):
    z = x
    for n in range(1, y):
        z = z * x
    return z
    

#%%