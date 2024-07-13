'''
Madlibs is a simple game where you create a story template with "blanks" for words. You, or 
another player, then construct a list of words and place them into the story, creating an often 
silly or funny story as a result.

Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and 
injects them into a story that you create.
'''

noun = input("Noun: ") 
verb = input("Verb: ") 
adj = input("Adjective: ") 
adv = input("Adverb: ") 

print(f'The {noun} could {verb} down the stairs {adj} at an {adv} rate.') 

