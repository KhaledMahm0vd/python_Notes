Automate the boring stuff with python programming:

Al Sweigart

======================================

expression: evaluate to a single value:

ex: 2+2 = 4 5-3=2

calculations:

+ addition - subtraction

* multiplication / division

calculation occurs according to PEMDAS:

Parantheses > exponents > multiplication > division > addition > subtraction

  

# data types:

is a category of values

1 → integer “int” 1.0 → float “a” → string “str”

“alice” + “bob” → “alicebob” concatenation

“alice” * 3 → alice alice alice

# arguments = values passed to functions

- execution start at the top and moves down.

# comments are ignored in python.

len() takes a string value & returns an integer value of the string's length.

int() str() float() convert values' data type

  

Flow Control:

Comparison Operators:

== equal to != not equal < less than > greater than <= less than or equal to

>= greater than or equal to

42 == 42 → True 42 != 42 → false 4>3 → True

4<3 → False 42 == “42” → false 42.0 == 42 True

  

Boolean Operators:

AND OR NOT

True AND True → True True OR True → True

True AND False → False True OR False → True

False AND True → False False OR True → True

False AND False → False False OR False → False

  

True and False are boolean datatype

NOT True → False NOT False → True

  

If statement:

  

`name = "alice"`

`if name == "alice":`

`print("Hi, Alice")`

`print("Done")`

  

`password = '1234'`

`if password = '1234':`

`print("Access Granted")`

`else:`

`print("Wrong Password")`

`name = 'bob'`

`age = 3000`

`if name = 'alice':`

`print("Hi, Alice")`

`elif age < 12:`

`print("wrong person")`

`elif age > 2000:`

`print("Welcome, vampire")`

`elif age < 100:`

`print("not you")`

  

0 & 0.0 are considered False value while other numbers are considered True

bool(0) → False bool('') → False

bool(42) → True bool(“Hello”) → True

  

# While Loop:

`spam = 0`

`while spam < 5:`

`print('Hello, World')`

`spam = spam + 1`

  

name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you')

  

the above program only quits if “your name” string is provided as input

  

`spam = 0`

`while spam < 5:`

`spam = spam + 1`

`if spam == 3 :`

`continue`

`print("spam is" + str(spam))`

  

`the above program doesn't print number 3.`

  

`when the execution reaches the end of a while statement's block, it jumps back to the start to re-check the condition.`

`A break statement causes the execution to immediately leave the loop, without re-checking the condition.`

`A continue statement causes the execution to immediately jump back to the start of the loop and re-check the condition.`

  

`# For loops:`

`print('My name is')`

`for i in range (5):`

`print('jimmy five times' + str(i))`

  

`total = 0`

`for num in range(101):`

`total = total + num`

`print(total)`

  

`print('My name is')`

`i = 0`

`while i < 5:`

`print('jimmy five times' + str(i))`

`i = i + 1`

  

`# For loop syntax:`

`for i in range(start, stop, step):`

`action`

`print('My name is')`

`for i in range (5, -1, -1):`

`print('jimmy five times' + str(i))`

  

`for loops will loop for a specific number of times.`

`The range() function called with one, two, or three arguments.`

`Break and continue can be used in for loops.`

  

`# Python Built-in functions:`

`i``mport random`

`r = random.randint(1,10)`

`print(r)`

  

`from random import *`

`randint(1,10)`

  

`random, math, print are python built-in functions.`

`The modules that come with python are called the standard library, but you can also install third-party modules using the pip(pipx on some linux systems) tool.`

`sys.exit() function will immediately close your program.`

`# write your own functions:`

`def hello():`

`print(hello)`

`hello(arguments)`

  

`def → defines a function`

`code in global scope can't use only local variables.`

`code in local scope can access global variables.`

`Code in one function local scope can't use variables in another local scope.`

  

`Spam = 36 → global scope`

`def eggs():`

`Spam = 42 → local scope`

`print(spam)`

  

`def spam():`

`eggs = 99`

`spam()`

`print(eggs) # error since egg is local scope & can't be called by global`

  

`def spam():`

`eggs = 99` `#` `first one rules`

`bacon()`

`print(eggs)`

`def bacon():`

`ham = 101`

`eggs = 0`

`spam()` `#` `will print as eggs = 99`

  

`def spam():`

`print(eggs)`

`eggs = 42`

`spam()` `# will print 42`

  

`def spam():`

`eggs = 'Hello'`

`print(eggs)` `# Hello`

`eggs = 42`

`spam()`

`print(eggs)` `# 42`

  

  

`def spam():`

`global eggs`

`eggs = 'Hello' # since it is global, first one will be printed`

`print(eggs)`

`eggs = 42`

`spam()`

`print(eggs)`

  

`# Try/Except statement:`

`def divideby(divideBy):`

`try:`

`return 42 / divideBy`

`except ZeroDivisionError:`

`print('Error, you can not divide by zero')`

`print(divideby(2))`

`print(divideby(12))`

`print(divideby(0))`

`print(divideby(1))`

  

`print('How many cats do you have?')`

`numCats = input()`

`try:`

`if int(numCats) >= 1:`

`print('that is alot of cats')`

`else:`

`print('that is not many cats')`

`except ValueError:`

`print('you did not enter a number')`

  

`print('How many cats do you have?')`

`numCats = input()`

`try:`

`if int(numCats) >= 1:`

`print('that is alot of cats')`

`else:`

`print('that is not many cats')`

`except ValueError:`

`print('you did not enter a number')`

  

`# Guess the number game:`

`# This is a guess the number game.`

`import random`

`secretNumber = random.randint(1, 20)`

`print('I am thinking of a number between 1 and 20.')`

  

`# Ask the player to guess 6 times.`

`for guessesTaken in range(1, 7):`

`print('Take a guess.')`

`guess = int(input())`

  

`if guess < secretNumber:`

`print('Your guess is too low.')`

`elif guess > secretNumber:`

`print('Your guess is too high.')`

`else:`

`break # This condition is the correct guess!`

  

`if guess == secretNumber:`

`print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')`

`else:`

`print('Nope. The number I was thinking of was ' + str(secretNumber))`

  

`# Lists:`

`lists is composed of brackets containing elements seperated by comma.`

`Spam = ['cat', 'bat', 'rat']`

`list index start with 0`

`spam[0] → cat`

`* list of lists: a list containing lists inside it.`

`s``pam = [['cat', 'bat'],[10,20,30,40]]`

  

`spam[0] → ['cat', 'bat']`

`spam[1][0] → 10`

  

`spam = ['cat', 'bat', 'rat', 'elephant']`

`spam[-1]`

`→` `elephant`

  

`spam = ['cat', 'bat','rat', 'elephant']`

`print(spam[-1])`

`print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')`

  

`we can use index to assign new value to list.`

`test = [10,20,30]`

`test[1] →` `'``Hello``'`

`test → [10,` `'``Hello``',` `30]`

`list[start:end] where start is inclusive and end is exclusive`

`to delete a list item:`

`del list[index]`

`len(list) → list items count (length)`

  

`there are similarities between lists and strings such as slicing and indexing.`

`list(“hello”)`

`→` `[‘h’, ‘e’, ‘l’, ‘l’, ‘o’]`

`name(‘zophie’)`

`name[0]`

`→` `z`

`name[1:3]`

`→ ‘``op’`

`you can’t assign a letter in a string.`

`name_2 = 'zophie a cat'`

`newName = name_2[0:7] + 'the' + name_2[8:12]`

`print(newName)`

  

`#` `mutable list` `references:`

`# change in first list does not change a copy`

`# but changing a copy does change the original`

`# since the copy and the original refers to same place in memory.`

`print('does not change the copy\n')`

`#spam refers to a reference of the list not the actual list.`

`spam = 42`

`cheese = spam`

`spam = 100`

`print(spam)`

`print(cheese)`

`print('does change the copy\n')`

`listx = [0,1,2,3,4]`

`choice = listx`

`choice[1] = 'hello!'`

`print(choice)`

`print(listx)`

  

`*` `immutable values don’t have this problem because they can’t be modified “in place”. They can only be replaced by new values.`

  

`“``copy” module in python have deepcopy function in it.`

`Shallow copy: two different objects refering to same list in memory.`

`spam = 42`

`cheese = spam`

`cheese → 42`

`spam → 42`

`this is shallow copy.`

  

`Deep Copy: copy first list to another list so two different variables/objects refer to different lists.`

`# deepcopy does not change the original list`

`import copy`

`spam = ['a', 'b', 'c', 'd']`

`cheese = copy.deepcopy(spam)`

`cheese[1] = 42`

`print(cheese)`

`print(spam)`

  

`recap:`

`- strings can do a lot of the same things lists can do except strings are mutable.`

`- immutable values like strings and tuples can’t be modified “in place”.`

`- mutable values like lists can be modified in place`

`- variables don’t contain lists, they contain references to the lists.`

`- when passing a list argument to a function, you are actually passing a list reference.`

`- changes made to a list in a function will affect the list outside the function.`

`- the \ line continuation character can be used to stretch python instructions across multiple lines.`

`Look at [https://youtu.be/_AEJHKGk9ns](https://youtu.be/_AEJHKGk9ns)`

`Section 7 : Dictionaries:`

`you can check for presence of keys in a dictionary using “in & not in”`

`‘``name’ in eggs`

`‘``color’ not in eggs`

  

`# dict[key] --> value`

`# dictionaries are unordered.`

`# order matters for lists but it does not for dictionaries.`

`myCat = {'size':'fat', 'color':'gray', 'voice':'loud'}`

`print(myCat['size'])`

`print('my cat has '+myCat['color']+' fur')`

`# list order:`

`print([1,2,3] == [3,2,1])`

`# dictionary order:`

`eggs = {'count':4, "color":"red", "age":1}`

`ham = {"age":1, "count":4, "color":"red"}`

`print(eggs == ham)`

`print('name' in eggs)`

`print('color' in ham)`

`print('count' not in eggs)`

  

`dictionary methods are keys(), values(), items()`

`list(eggs.keys()) → returns a list`

`list(ham.values()) → returns a list`

`list(eggs.items()) → returns a list of tuples.`

`[{,},{,},{,}] → list of tuples.`

  

`Note:`

`list(eggs.keys()) → returns a list`

`eggs.keys() → returns “dict_keys([‘name’, ’species’, ‘age’])”`

  

`using` `dictionary methods with For loop:`

`for k in eggs.keys():`

`print(k)`

  

`for v in eggs.values():`

`print(v)`

  

`for k,v in eggs.items():`

`print(k,v)`

  

`to check for key in a dictionary without raising an error, we can use if statement.`

`If ‘color’ in eggs:`

`print(eggs[‘color’])`

  

`but this process is tedious.`

`Python has .get method for getting a value while providing default value if not found.`

`# default Get method for finding a key in dict without raising an error and providing default value if not found.`

`eggs = {'count':4, "color":"red", "age":17}`

`print(eggs.get('age',0))`

`# return an empty string if not found.`

`print(eggs.get('health', ""))`

`picnicItems = {'apples':5, 'cups':2}`

`print("I am bringing "+str(picnicItems.get('napkins', 0))+" napkins to the party")`

  

`the opposite of get method is set method.`

`if "health" not in eggs:`

`eggs['health'] = 'good'`

  

`print(eggs)`

`# the alterantive for above if statement is setdefault method`

`ham = {'count':4, "age":17}`

`ham.setdefault('color','black')`

`print(ham)`

  

`# setting new default does not change the default value, it will be set once.`

  

`message = 'it was a bright cold day in April, and the clock was thirteen'`

`count = {}`

`for character in message.upper():`

`count.setdefault(character, 0)`

`count[character] = count[character] + 1`

`print(count)`

  

`notes:`

`1. to apply a string method apply it on provided string like message not on character.`

`2. setdefault sets the value to 0 above if not found.`

`3. to escape a lot of commas in a long text, we use trible quotes ''' '''.`

`4. to clean the display and print neatly we use pprint module.`

`Recap:`

`* dictionaries contain key-value pairs. Keys are like a list’s indexes.`

`* dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.`

`* dictionaries are unordered. There is no “first” key-value pair in a dictionary.`

`* the keys(), values(), and items() methods will return list-like values of a dictionary’s keys, values, and both keys and values, respectively.`

`* the get() method can return a default value if a key doesn’t exist.`

`* the setdefault() method can set a value if a key doesn’t exist.`

`* the pprint module’s pprint “pretty print” function display a dictionary value cleanly. The pformat() function returns a string value of this output.`