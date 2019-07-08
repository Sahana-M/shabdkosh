# Kannada Stemmer -
This is the implementation of Kannada stemmer. It is a light weight Kannada stemmer based on removing suffixes from a Kannada word. Given a suffixed form of a word its returns its base form.

The language used for implementation of this stemmer is Python (Python 3.5)

The data used for framing the rules were from the 
- fasttext.cc (a free open source library for natural language processing tasks) which consists of word vectors for 150+ langugages. Specifically Kannada words data set were from both commoncrawl.org and wikipedia data set.
- commoncrawl data set https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.kn.300.vec.gz
- wikipedia data set https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.kn.vec


# INTRODUCTION

Kannada is both agglunative and morphologically rich langugage. Out of 38 basic characters, 330 conjucts are formed by various combination of vowels and consonants. There are more than 10,000 basic root words and about a million morphed variants are formed due to more than 5000 distinct character variants.

Example -
1) **ಓದಿಸಿನೋಡುತ್ತಾನೆ  (OdisinoDuttane**) which can be split into meaningful parts :
	ಓದು   + ಇಸಿ   + ನೋಡು + ಉತ್ತಾ  + ಆನೆ  = ಓದಿಸಿನೋಡುತ್ತಾನೆ 
	Oodu + isi + noDu   + ntt  + Ane = OdisinoDuttane

Since the variants are huge the rules needed for implementation are also large in number. The total number of rule categories are 74, with each rule conisting of arbitrary number of suffixes, hence the total number of rules are 416. The number of rules will keep on increasing depending on the encounter of new variants. 

# INSTALLATION
Our stemmer is light weight and requires only Python 3 (or any version of python 3, even python 2 will work)
Installation

```sh
$ sudo apt-get update
$ sudo apt-get install python3.5
```


# IMPLEMENTATION 

The commoncrawl data set consists of 14,74,573 words and wiki data set consists of 1,63,265 words which contain some special characters as well as words from other langugages. 
After filtering this data set using a simple unicode filter code the resulting number of words were,


| Data set  | Before filtering | After filtering| 
| ------ | ------ | ------ |
| common crawl |14,74,573|12,53,814|
|wikipedia |1,63,265|1,49,677|


This gave us two fully filtered data set, which now can be used for our stemmer.

The python implementation Kannada_stemmer.py has been implemented in **python 3.5.** 

**The code contains the python dictionary complex_suffixes which consists of 73 categories of rules.** 
Rule number :
- **1 to 40** contain the categories of suffixes belonging to different forms of tenses.
- **41 to 73** consists of rules which donot belong to tenses category, many belonging to the same category of meaning and some random suffixes.

Example - 
**Rule 48 :**

| Kannada  | English translation|
| ------ | ------ |
| ದಲ್ಲೇ |There only (referring place)|
| ನಲ್ಲೇ |In him/her/there only (referring a person) |
| ನಲ್ಲಿ |In him/her/there |
| ವಲ್ಲಿ |-ing form |
| ದಲ್ಲಿ |In it (referring thing) |
| ದಲ್ಲೂ | In 		  it only (referring thing) |
| ಯಲ್ಲಿ | In him/her |
| ರಲ್ಲಿ |In them 
| ಗಳಲ್ಲಿ |In those |
| ಳಲ್ಲಿ |In her |
| ಯಲ್ಲಿನ | In there ||

As we can see in the english translation of these suffixes, that all of the translations are similar to each other, denoting a similar meaning.These kind of suffixes are grouped together to form a single rule. 

### Rule types
Our implementation has been concentrating on 4 different types of stemming, they are,

- Suffixes where  left half of suffix be retained and right half be discarded

    
    | Rule   | Before stemming | After stemming| 
    | ------ | ------ | ------ |
    | 72 |ರದ|ರ
    |example|ಮರದ|ಮರ
    |   |tree's|tree|


- Suffixes where left half of suffix be retained and right half be modified


    | Rule   | Before stemming | After stemming| 
    | ------ | ------ | ------ |
    |73|ಡಲು|ಡು|
    |example|ಮಾಡಲು|ಮಾಡು|
    ||to do|do|
    

- Suffixes which must be completely removed


    | Rule   | Before stemming | After stemming| 
    | ------ | ------ | ------ |
    |41|ಯಾದರೆ||
    |example|ಪ್ರೆಶ್ನೆ ಯಾದರೆ|ಪ್ರೆಶ್ನೆ |
    ||if it's a question|question|
  
  
- Suffixes which are single characters and are risky to remove, hence this is the last kind of suffix to be checked


    | Rule   | Before stemming | After stemming| 
    | ------ | ------ | ------ |
    |71|ದ||
    |example|ಬರೆದ|ಬರೆ|
    ||he wrote/ wrote|write|
        

This is a brief overview of all the rules framed.
The code implemented here is taking a file input of our wikipedia or commoncrawl dataset and giving out a file of base words after stemming.

