from textblob import TextBlob
gravity = TextBlob('A screaming comes across the sky.')
gravity.words
TextBlob('A screaming comes across the sky.').words
len(gravity.words)
gravity.words[:3]
sorted(gravity.words)
gravity.tokens
TextBlob("Can't touch this.").tokens

pride = TextBlob('It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.')
pride.tags

count = 0
def adjs():
    for (word, tag) in pride.tags:
    if tag == 'JJ':
        count = count + 1


