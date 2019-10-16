#%%
#Traveling abroad can be an exciting experience, though preparing can become stressful.
#One of the more prominent causes of stress is ensuring that you have the correct money for the trip, and one decision that each traveler must make is where is the best place to convert currency for their trip? For example, should you convert your currency before leaving at a currency exchange spot? Should they visit a currency exchange kiosk upon arriving at the airport of their final destination? Or is it better to visit a local bank after checking into your hotel (which is what a lot of my fellow travelers did on a trip to Morocco)? There is also the tried and true ATM. 

#In this currency converter, the user has a few options:
#-Convert dollars to euros 
#-Convert dollars to dirhams
#-Convert euros to dollars 

#To test this converter, complete these conversions:

#Convert 30 dollars to euros using the function to_euro

#Convert 100 euros to dollars using the function to_dollar

#Convert 50 dollars to dirham using the function to_dirham
#%%
def to_euro(d):
    return d * (0.91)


#%%
def to_dollar(e):
    return e * (1.1)

#%%
def to_dirham(c):
    return c / (0.27)

#%%
