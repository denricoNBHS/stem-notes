
# Introduction to Python

Let's dive right into what Python can do! First, fire up the interactive Python interpreter from your command prompt (PowerShell for Windows or Terminal for OS X). 

__Note for clarity__: Your prompt depends on your username, directory, and a host of other variables I couldn't possibly anticipate. I've tried to generalize below, but to be clear, the only command you're entering at the prompt is `python`

### _Windows_:

`C:\[directory\username]> python`

### _Mac OS X_:

`[your username]$ python`

Once you've started the iPython (interactive Python) shell, your prompt will look like this:

`>>>`

and it will accept Python commands. Let's test it out:


```python
print('Hello world!')
```

    Hello world!


In this (stale yet traditional) example, we've called the __function__ `print` with the __argument__ `'Hello world!'`. As you've no doubt figured out, the `print()` function prints its argument to the screen. In this case, we've passed it the __string__ `'Hello world!'` In Python, and programming in general, a string is simply text for display or manipulation.

In Python, strings are surrounded in quotes, like `'Hey, hey!'` or `"My, my!"`. At any point, you can check an object's __type__ by using the `type()` function, as shown below.


```python
type('Rock and Roll will never die.')
```




    str



You can see that the function returns the value `str`, which is short for _string_. Let's see what else the interpreter can do...

Next: [Mathematical Operators](mathematical_operators.ipynb)


```python
# Note: throughout the guide, you'll see comments like this throughout the code
# Python ignores anything on a line after the '#' symbol.
# Getting into the habit of commenting your code will help you and your readers
# once your code starts getting more complex.
```
