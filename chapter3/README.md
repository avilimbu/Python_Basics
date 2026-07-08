# Chapter 3 | STRINGS

Stirng is a data type in python.

Strings are immutable which means that we cannot change them by running functions on them.

string is a sequence of characters enclosed in quotes.

We can primarily write a string in three ways.
* a = 'python' `single quoted string`
* name = "ram" `double quoted string`
* poem = '''Every bug is just a lesson to explore,
            Every line of code unlocks a little more.
            With Python as my guide, I'll learn and grow each day,
            One program at a time, I'll build my own way.''' `triple quoted string`


### String Slicing

A string in python can be sliced for getting a part of a string.

The index in a string starts for "0" to length(-1) in Python. In order to slice a string we use 
`sstring_name[start: stop]`.

Negative indexes can also be used in string, where `-1 = length(-1)`, `-2 = length(-2)` and `so on`.

>>Slicing with skip value

We can also provide skip value as a part of our slice like `string_name[start: stop: step]`. Default value for `step = 1` meaning it moves one step in teh left to right direction. 


### string Functions

Some of the most commonly used functions to perform operations or manipulate strings are:

1. len() functions:

This function returns length of the string | `len("avhi")` gives `4`

2. string.endswith("arr"):

This function tells whether a variable string end with the string given or not. 

3. string.count("c"):

This functions counts the total no of occurance of any given chaaracter.

4. string.capitallize()

This function capitalize the first character of a given string.

5. string.find(word)

This function finds a word and returns the index of first occurance of that word.

`sentence = "wow, i like reading"` `print(sentence.find("like"))` Gives '7'

6. replace(old_word, new_word):

This function replace the old word with the new word.

### Escape Sequence Characters

Sequence of characters after "\" -`Escape Sequence Character`

* \n = new line
* \t = tab
* \'..\' = singlequote
* \\ = backslash
*\"...\" = double quote


