# Write your function, here.
def big_words(tup):
    # return tuple(filter(lambda word: len(word) > 8, tup))
    return tuple([x for x in tup if len(x) > 8])


print(big_words(('earth', 'jupiter', 'mars', 'neptune'))) #> ()
print(big_words(('wakanda', 'melbourne', 'london', 'france'))) #> ('melbourne',)
print(big_words(('app', 'academy', 'app academy', 'xylophone'))) #> ('app academy', 'xylophone')