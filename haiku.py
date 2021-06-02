#!/usr/bin/env python3

import os
import tweepy as tw
import random as ran
import toml

config = toml.load("config.toml")
consumer_key = config['twitter']['consumer_key']
consumer_secret = config['twitter']['consumer_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
#define the words used in each parts of speech */
#FUTURE -> take into account the tense (past, present, future)
#FUTURE -> figure out how to leverage this api -> https://developer.oxforddictionaries.com/
articles = ['a','an','the']
#https://www.cbsnews.com/news/study-time-is-most-often-used-noun/
#FUTURE -> there are ten types of nouns
nouns = ['time','person','year','way','day','thing','man','world','life','hand','part','child','eye','woman','place','work','week','case','point','government','company','number','group','problem','fact']
#https://www.thefreedictionary.com/List-of-pronouns.htm
#FUTURE -> there are several types of pronouns
pronouns = ['all','another','any','anybody','anyone','anything','both','each','either','everybody','everyone','everything','few','many','most','neither','nobody','none','no one','nothing','one','other','others','several','some','somebody','someone','something','such']
#https://www.englishclub.com/vocabulary/common-verbs-25.htm
#FUTURE -> there are several types of verbs
#https://www.uvu.edu/writingcenter/docs/handouts/grammar/typesofverbs.pdf
verbs = ['be','have','do','say','get','make','go','know','take','see','come','think','look','want','give','use','find','tell','ask','work','seem','feel','try','leave','call']
#https://www.englishclub.com/vocabulary/common-adjectives-25.htm
adjectives = ['good','new','first','last','long','great','little','own','other','old','right','big','high','different','small','large','next','early','young','important','few','public','bad','same','able']
#https://www.englishclub.com/vocabulary/common-adverbs-25.htm
adverbs = ['up','so','out','just','now','how','then','more','also','here','well','only','very','even','back','there','down','still','in','as','too','when','never','really','most']
#https://www.englishclub.com/vocabulary/common-propositions-25.htm
#FUTURE look up types of prepositions
prepositions = ['of','in','to','for','with','on','at','from','by','about','as','into','like','through','after','over','between','out','against','during','without','before','under','around','among']
#https://www.englishclub.com/vocabulary/common-conjunctions-25.htm
#FUTURE look up types of conjunctions
conjunctions = ['and','that','but','or','as','if','when','than','because','while','where','after','so','though','since','until','whether','before','although','nor','like','once','unless','now','except']
#https://www.englishclub.com/vocabulary/common-interjections-25.htm
#FUTURE look up types of interjections
interjections = ['yes','oh','yeah','no','hey','hi','hello','hmm','ah','wow','Alas','Bingo','Bravo','Eureka','Crikey','Gee','Golly','Gosh','Holy cow','Aha','Huh','Duh','Ahh','Well','Yuck','Eww','Aww','Ouch','Oh','Ah','Ugh','Phew','Phooey','Rats','Yippee','Blah','Brr','Eek','Good grief','Shh','Please','Psst','Shoo','Hey','Oh','Yo','Here','Ahem','Encore','There','HushScat','No','Silence','Enough']
#sentence structure
#FUTURE -> make this more dynamic...
s_article = ran.choice(articles)
s_adjective = ran.choice(adjectives)
s_noun = ran.choice(nouns)
p_adverb = ran.choice(adverbs)
p_verb = ran.choice(verbs)
p_article = ran.choice(articles)
p_adjective = ran.choice(adjectives)
p_noun = ran.choice(nouns)
#accounting for the changes to articles when next word begins with a vowel
vowels = 'aeiou'
if s_adjective[0].lower() in vowels:
    while s_article == 'a':
        s_article = ran.choice(articles)
else:
    while s_article == 'an':
        s_article = ran.choice(articles)
if p_adjective[0].lower() in vowels:
    while p_article == 'a':
        p_article = ran.choice(articles)
else:
    while p_article == 'an':
        p_article = ran.choice(articles)
#counting syllables
s_article_vowels = [letter for letter in s_article if letter in vowels]
s_adjective_vowels = [letter for letter in s_adjective if letter in vowels]
s_noun_vowels = [letter for letter in s_noun if letter in vowels]

p_adverb_vowels = [letter for letter in p_adverb if letter in vowels]
p_verb_vowels = [letter for letter in p_verb if letter in vowels]
p_article_vowels = [letter for letter in p_article if letter in vowels]
p_adjective_vowels = [letter for letter in p_adjective if letter in vowels]
p_noun_vowels = [letter for letter in p_noun if letter in vowels]

vowels_in_each_word = [s_article_vowels, s_adjective_vowels, s_noun_vowels, p_adverb_vowels, p_adjective_vowels, p_article_vowels, p_adjective_vowels, p_noun_vowels]
print(vowels_in_each_word)

add_interjection = ran.randint(1,2)

make_subject_plural = ran.randint(0,1)
if make_subject_plural == 1:
    print("making the noun plural")
    print("checking the article")
    if (s_article == 'a') | (s_article == 'an'):
        print("article needs to be changed from a or an to the")
        s_article = 'the'
    if s_noun == 'person':
        s_noun = 'people'
    elif s_noun == 'woman':
        s_noun = 'women'
    elif s_noun == 'man':
        s_noun = 'men'
    elif s_noun == 'life':
        s_noun = 'lives'
    elif s_noun == 'child':
        s_noun = 'children'
    elif s_noun.endswith('s') | s_noun.endswith('x') | s_noun.endswith('z') | s_noun.endswith('ch') | s_noun.endswith('sh'):
        s_noun = s_noun + 'es'
        print("adding -es: " + s_noun)
    else:
        s_noun = s_noun + 's'
        print("adding -s: " + s_noun)
else:
    print("making the verb plural")
    if p_verb.endswith('s') | p_verb.endswith('x') | p_verb.endswith('z') | p_verb.endswith('ch') | p_verb.endswith('sh'):
        p_verb = p_verb + 'es'
        print("adding -es: " + p_verb)
    else:
        p_verb = p_verb + 's'
        print("adding -s: " + p_verb)

subject = s_article + ' ' + s_adjective + ' ' + s_noun

make_predicate_plural = ran.randint(0,1)
if make_predicate_plural == 1:
    print("making the noun plural")
    print("checking the article")
    if (p_article == 'a') | (p_article == 'an'):
        p_article = 'the'
    if p_noun == 'person':
        p_noun = 'people'
    if p_noun == 'woman':
        p_noun = 'women'
    if p_noun == 'man':
        p_noun = 'men'
    if p_noun == 'life':
        p_noun = 'lives'
    if p_noun == 'child':
        p_noun = 'children'
    if p_noun.endswith('s') | p_noun.endswith('x') | p_noun.endswith('z') | p_noun.endswith('ch') | p_noun.endswith('sh'):
        p_noun = p_noun + 'es'
        print("adding -es: " + p_noun)
    else:
        p_noun = p_noun + 's'
        print("adding -s: " + p_noun)
else:
    print("nothing else to do")
predicate = p_adverb + ' ' + p_verb + ' ' + p_article + ' ' + p_adjective + ' ' + p_noun

if add_interjection == 1:
	statement = ran.choice(interjections) + '!' + ' '
statement = subject + ' ' +  predicate
print(statement);
statement_vowel_count = len([letter for letter in statement if letter in vowels])
print(statement_vowel_count)

# Post a tweet from Python
api.update_status(statement)
# Your tweet has been posted!
