#%%
def to_f(c):
    if c < -273.15:
        raise ValueError("Temperature Value is Below Absolute Zero")
    return ((9/5) * c) + 32

#%%
