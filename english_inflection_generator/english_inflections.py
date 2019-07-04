from pattern.en import conjugate,PRESENT,PAST,INFINITIVE,SG,PL,INDICATIVE,IMPERATIVE,PROGRESSIVE
from nltk.stem import PorterStemmer


ps =PorterStemmer()
word = 'reading'
rootWord=ps.stem(word)
print("\n Root word ", rootWord)

#INDICATIVE ------------------------------------------
print("\n\nINDICATIVE")
#1st Person Singular I - present, past , future
print("\n1st Person Singular I ")
print ("Present -    I ",conjugate(verb=word, tense=PRESENT, person = 1, number = SG, mood= INDICATIVE),
       "\nPast -       I ", conjugate(verb=word, tense=PAST, person = 1, number = SG, mood= INDICATIVE),
       "\nFuture -     I will",conjugate(verb=word, tense=INFINITIVE, person = 1, number = SG, mood= INDICATIVE))


#1st Person Plural WE - present, past, future
print("\n1st Person Plural WE")
print ("Present -    We ",conjugate(verb=word, tense=PRESENT, person = 1, number = PL, mood= INDICATIVE),
       "\nPast -       We ",conjugate(verb=word, tense=PAST, person = 1, number = PL, mood= INDICATIVE),
       "\nFuture -     We will ",conjugate(verb=word, tense=INFINITIVE, person = 1, number = PL, mood= INDICATIVE))

#2nd Person YOU- present, past, future
print("\n2nd Person Plural")
print ("Present -    You ",conjugate(verb=word, tense=PRESENT, person = 2, number = SG, mood= INDICATIVE),
       "\nPast -       You ",conjugate(verb=word, tense=PAST, person = 2, number = SG, mood= INDICATIVE),
       "\nFuture -     You will ",conjugate(verb=word, tense=INFINITIVE, person = 2, number = SG, mood= INDICATIVE))

#3rd Person Singular HE/SHE/IT- present, past, future
print("\n3rd person singular")
print ("Present -    he/she/it ",conjugate(verb=word, tense=PRESENT, person = 3, number = SG, mood= INDICATIVE),
       "\nPast -       he/she/it ",conjugate(verb=word, tense=PAST, person = 3, number = SG, mood= INDICATIVE),
       "\nFuture -     he/she/it will", conjugate(verb=word, tense=INFINITIVE, person = 3, number = SG, mood= INDICATIVE))

#3rd Person Plurals THEY- present, past, future
print("\n3rd person plural ")
print ("Present -    they ",conjugate(verb=word, tense=PRESENT, person = 3, number = PL, mood= INDICATIVE),
       "\nPast -       they ",conjugate(verb=word, tense=PAST, person = 3, number = PL, mood= INDICATIVE),
       "\nFuture -     they will",conjugate(verb=word, tense=INFINITIVE, person = 3, number = PL, mood= INDICATIVE))



#PERFECT ------------------------------------------

print("\n\nPERFECT -")
#1st Person Singular I - present, past , future
print("\n1st Person Singular I ")
print ("Present -    I have",conjugate(verb=word, tense = PAST, person = 1, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nPast -       I had", conjugate(verb=word, tense= PAST, person = 1, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nFuture -     I will have",conjugate(verb=word, tense= PAST, person = 1, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE))


#1st Person Plural WE - present, past, future
print("\n1st Person Plural WE")
print ("Present -    We have",conjugate(verb=word, tense=PAST, person = 1, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nPast -       We had",conjugate(verb=word, tense=PAST, person = 1, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nFuture -     We will have",conjugate(verb=word, tense=PAST, person = 1, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE))

#2nd Person YOU- present, past, future
print("\n2nd Person Plural")
print ("Present -    You have",conjugate(verb=word, tense=PAST, person = 2, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nPast -       You had",conjugate(verb=word, tense=PAST, person = 2, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nFuture -     You will have",conjugate(verb=word, tense=PAST, person = 2, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE))

#3rd Person Singular HE/SHE/IT- present, past, future
print("\n3rd person singular")
print ("Present -    he/she/it has",conjugate(verb=word, tense=PAST, person = 3, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nPast -       he/she/it had",conjugate(verb=word, tense=PAST, person = 3, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nFuture -     he/she/it will have", conjugate(verb=word, tense=PAST, person = 3, number = SG, mood = INDICATIVE, aspect = PROGRESSIVE))

#3rd Person Plurals THEY- present, past, future
print("\n3rd person plural ")
print ("Present -    they have",conjugate(verb=word, tense=PAST, person = 3, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nPast -       they had",conjugate(verb=word, tense=PAST, person = 3, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE),
       "\nFuture -     they will have",conjugate(verb=word, tense=PAST, person = 3, number = PL, mood = INDICATIVE, aspect = PROGRESSIVE))


#CONTINUOUS --------------------------------------

print("\n\nCONTINUOUS -")

#1st Person Singular I - present, past , future
print("\n1st Person Singular I ")
print ("Present -    I am",conjugate(verb=word, person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE),
       "\nPast -       I was", conjugate(verb=word,  person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE),
       "\nFuture -     I will be",conjugate(verb=word,  person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE))


#1st Person Plural WE - present, past, future
print("\n1st Person Plural WE")
print ("Present -    We are",conjugate(verb=word, person = 1, number = PL, aspect= PROGRESSIVE),
       "\nPast -       We were",conjugate(verb=word,  person = 1, number = PL, aspect= PROGRESSIVE),
       "\nFuture -     We will be",conjugate(verb=word, person = 1, number = PL, aspect= PROGRESSIVE))

#2nd Person YOU- present, past, future
print("\n2nd Person Plural")
print ("Present -    You are",conjugate(verb=word,  person = 2, number = SG, aspect= PROGRESSIVE),
       "\nPast -       You were",conjugate(verb=word,  person = 2, number = SG, aspect= PROGRESSIVE),
       "\nFuture -     You will be",conjugate(verb=word, person = 2, number = SG, aspect= PROGRESSIVE))

#3rd Person Singular HE/SHE/IT- present, past, future
print("\n3rd person singular")
print ("Present -    he/she/it is",conjugate(verb=word,  person = 3, number = SG, aspect= PROGRESSIVE),
       "\nPast -       he/she/it was",conjugate(verb=word, person = 3, number = SG, aspect= PROGRESSIVE),
       "\nFuture -     he/she/it will be", conjugate(verb=word,  person = 3, number = SG, aspect= PROGRESSIVE))

#3rd Person Plurals THEY- present, past, future
print("\n3rd person plural ")
print ("Present -    they are",conjugate(verb=word,  person = 3, number = PL, aspect= PROGRESSIVE),
       "\nPast -       they were",conjugate(verb=word,  person = 3, number = PL, aspect= PROGRESSIVE),
       "\nFuture -     they will be",conjugate(verb=word, person = 3, number = PL, aspect= PROGRESSIVE))



#PERFECT CONTINUOUS --------------------------------------

print("\n\nPERFECT CONTINUOUS -")

#1st Person Singular I - present, past , future
print("\n1st Person Singular I ")
print ("Present -    I have been",conjugate(verb=word, person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE),
       "\nPast -       I had been", conjugate(verb=word,  person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE),
       "\nFuture -     I will have been",conjugate(verb=word,  person = 1, number = SG, aspect= PROGRESSIVE, mood= INDICATIVE))


#1st Person Plural WE - present, past, future
print("\n1st Person Plural WE")
print ("Present -    We have been",conjugate(verb=word, person = 1, number = PL, aspect= PROGRESSIVE),
       "\nPast -       We had been",conjugate(verb=word,  person = 1, number = PL, aspect= PROGRESSIVE),
       "\nFuture -     We will have been",conjugate(verb=word, person = 1, number = PL, aspect= PROGRESSIVE))

#2nd Person YOU- present, past, future
print("\n2nd Person Plural")
print ("Present -    You have been",conjugate(verb=word,  person = 2, number = SG, aspect= PROGRESSIVE),
       "\nPast -       You had been",conjugate(verb=word,  person = 2, number = SG, aspect= PROGRESSIVE),
       "\nFuture -     You will have been",conjugate(verb=word, person = 2, number = SG, aspect= PROGRESSIVE))

#3rd Person Singular HE/SHE/IT- present, past, future
print("\n3rd person singular")
print ("Present -    he/she/it has been",conjugate(verb=word,  person = 3, number = SG, aspect= PROGRESSIVE),
       "\nPast -       he/she/it had been",conjugate(verb=word, person = 3, number = SG, aspect= PROGRESSIVE),
       "\nFuture -     he/she/it will have been", conjugate(verb=word,  person = 3, number = SG, aspect= PROGRESSIVE))

#3rd Person Plurals THEY- present, past, future
print("\n3rd person plural ")
print ("Present -    they have been",conjugate(verb=word,  person = 3, number = PL, aspect= PROGRESSIVE),
       "\nPast -       they had been",conjugate(verb=word,  person = 3, number = PL, aspect= PROGRESSIVE),
       "\nFuture -     they will have been",conjugate(verb=word, person = 3, number = PL, aspect= PROGRESSIVE))


























