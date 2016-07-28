
# Introduction to Functions

You may recall from your math classes that a __function__ is a mapping from one set to another where every input maps to exactly one output. Perhaps my language seems odd to you; your experience with functions may be limited to the $y(x)$ variety. If this is the case, don't panic - there are two good (I hope) reasons I've chosen to be a bit more inclusive here.

- In your upper-level math classes you'll find this definition of function is a much more useful scaffold upon which to build your intuition.
- Most of the functions you'll write in Python have nothing to do with math!

You've already seen a few of Python's built-in functions in action -- namely `print()` and `type()`. Python has a ton of [built-in functionality](https://docs.python.org/3/), but what if you want something that Python doesn't already offer?

### Anatomy of a Function

It turns out defining our own functions is relatively straightforward. Below you'll find a function that takes two numbers as input and adds their squares:


```python
def add_squares(a, b):  
    return a**2 + b**2
```

Let's look at this piece by piece:


- the `def` keyword tells Python to __def__ine a new function called `add_squares` 


- `add_squares`, the function's name, describes what the function does. This isn't necessary for the code to function, but it makes it much more readable. In Python, it's conventional to name functions descriptively using lowercase letters, with underscores separating multiple words.


- the function has two _positional_ __parameters__, `a` and `b`. This means `a` and `b` are assigned _in order_. It may help to think of parameters as placeholders for values that are taken as input when the function is called. 


- a colon `:` and a newline take us to the body of the function. Notice after the newline we have an indented block. This block defines the _internal_ workings of the function, and effectively acts as a lockbox, preventing anything outside the function from seeing the data.


- there's another keyword, `return` that tells Python what information to pass outside of the code block. `return` passes the information on to whichever process called the function. So for example if we run: `type(add_squares(1,2))`, the interpreter will first evaluate `add_squares(1,2)` and then pass that answer along to the `type()` function, which should spit out `int`. 

So why doesn't the cell spit anything out when we run it? It's because all that code does is __define__ the function; it only tells Python what `add_squares` means. 

If we want to actually use the function, we need to _call_ it. When you call a function, you have to give it an __argument__ for every required __parameter__ - in this case, the values of `a` and `b`.

An example function call is shown below:


```python
#Passing the positional arguments 3 and 4 to add_squares(a, b).
#Since the function looks for a, b...
#INSIDE the function, a=3 and b=4. 
add_squares(3, 4) 
```




    25



Not so bad, right? Just a few more notes:

Unless you specify otherwise, what happens in the function stays in the function! You might be thinking that somewhere along the line, Python learned that a = 3 and b = 4, but if you ask the interpreter about those values, you'll see it has no idea what you're talking about.


```python
#Don't fall into the trap!
print(a)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-dd6275ab97fd> in <module>()
          1 #Don't fall into the trap!
    ----> 2 print(a)
    

    NameError: name 'a' is not defined


Finally you may be (but probably aren't) wondering why our function printed out the results without having called the `print()` function. 

In an interactive shell, a function will `return` its value to stdout (the terminal window) unless it's assigned elsewhere. In a non-interactive environment, the value disappears into the void unless something else captures it. _i.e._ if you were to run the program above from the command line, you'd see nothing happen.


```python
#Example that stores the return value
c_squared = add_squares(5, 12)
```


```python
print(c_squared)
```
