# NUL Challenge  

### Task 1: extend the english grammar
 
[JSGF text file](https://github.com/TianaQ/nlu-challenge/blob/master/JSGF_en_ext.txt), [test script in Python](https://github.com/TianaQ/nlu-challenge/blob/master/test.py)  

##### Examples:  
```
we 'd like to listen to electro
i 'd like to hear pop please
i would like to hear rumours by cake please
would you please put on cake please
can you put on let it be
could you please put on some reggue please
could you put on bat out of hell please
could you please play thriller by radio head
would you put on thriller by radio head please
```
##### Questions: 

1. Extend the above grammar to cover the following kind of utterances:
```
[i want to listen to]<unk> [jazz]<genre> [music]<unk>`
[play me]<unk> [ummagumma]<album> [by]<unk> [pink floyd]<artist>
```
###### Examples:  
```
we 'd like to listen to electro
i 'd like to hear pop please
i would like to hear rumours by cake please
would you please put on cake please
can you put on let it be
could you please put on some reggue please
could you put on bat out of hell please
could you please play thriller by radio head
would you put on thriller by radio head please
```
[JSGF text file](https://github.com/NILodio/nl-challenge/blob/master/base_us_ext_JSGF.txt), [test script in Python](https://github.com/NILodio/nl-challenge/blob/master/solution.py)  

2. Do you see any limitations on how the above grammar could scale up, as you keep adding entities to
provide coverage for building the final statistical models?
Shortly report them if any, and share some ideas to possibly overcome them.

* Adding a bunch of rules may lead to accidentally generating utterances that won't be expected, this will alter the accuracy of the model. This could be avoided using wishes sentences( sentences that are preselected by the model  or creating grammar for different cases that would improve the model before training )

* Also, there are a bulk of slags in all languages which could drive us to 
high algorithmic complexity, some of them could be handled by a pre-trained selected grammar. However, we should be aware of this issue and consider different approaches of this bias 


### Task 2: ### Task 1: extend the english grammar

###### Examples:  
```
porfavor toca los bellacos porfavor
me quiero escuchar humano
pon some ballenato music porfavor
pon humano
me quiero escuchar los bellacos by radio head
pon pop
toca pink floyd
toca la liga porfavor
reproduce toca some gospel music
```
[JSGF text file](https://github.com/NILodio/nl-challenge/blob/master/base_es_ext_JSGF.txt), [test script in Python](https://github.com/NILodio/nl-challenge/blob/master/solution.py)  

* Grammarly Spanish is more complex than English, there are so many combinations and idioms to be aware of.

* In Spanish it also becomes necessary to build proper sequences of rules to handle word forms and idioms