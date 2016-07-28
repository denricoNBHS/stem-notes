
# Assignment and Comparison in Python:
### Not all equals are equal

Time for what might very well be the operator you use most frequently in Python, the assignment operator, `=`. 

You might be thinking, "Isn't that an equals sign?" You'd be wrong, and that's what you get for thinking. Okay, to be fair, it _is_ an equals sign, but the way it behaves in Python is subtly different from what you're used to.

In your iPython shell, when you enter something like:


```python
a = 3
```

you're saying that `a` and 3 are the same, but more importantly, you're taking the __variable__ `a` and __assigning__ it a value of 3. Now when we ask the interpreter about the value of `a`, we get 3.


```python
a
```




    3



We can also perform all of the same operations on `a` we could with the number 3. For all intents and purposes, `a` _is_ 3.


```python
a**2
```




    9




```python
a-1
```




    2




```python
a % 2
```




    1



This isn't just limited to `int` types. Variables in Python can store _any_ object type!


```python
three = "III"
```

... and they can be used in functions!


```python
type(three)
```




    str




```python
print(three)
```

    III


You can also reassign a variable after you've previously assigned it.


```python
three = 3
```


```python
three
```




    3



Python also supports _multiple assignment_. This can save space! For example:


```python
#Without multiple assignment
a = "Apple"
b = "Banana"
c = "Cherry"
```


```python
print(a, b, c)
```

    Apple Banana Cherry



```python
#Using multiple assignment
a, b, c = 1, 2, 3
```


```python
print(a, b, c)
```

    1 2 3


If you're looking to _check_ whether two things are equal, we use the __equivalence__ operator, `==`.


```python
a == 1 # Is a equal to 1?
```




    True



The previous line is equivalent to asking Python whether `a` and 1 are equivalent. In this case, Python responds with an emphatic "Yes!". Wait... we haven't seen this before. Let's get out our Pythondex and see what we have here.


```python
type(a==1)
```




    bool



`bool`! Boolean values are used to keep track of `True`/`False` values. Any type of conditional programming relies on these values to make decisions. For example, let's use modular arithmetic to evaluate whether or not a number is even:


```python
89 % 2 == 0
```




    False



This code is equivalent to asking, "Hey Python, is the remainder of 89 divided by 2 zero?"

Python's all, "You mean is 89 even? I got you fam -- no."

Here are some of the other comparison operators in action: 


```python
8 != 9 # Is 8 not equal to 9?
```




    True




```python
5 > 6 # Is 5 greater than 6?
```




    False




```python
5 < 6 # Is 5 less than 6?
```




    True




```python
9 >= 19 # Is 9 greater than or equal to 19?
```




    False




```python
9 <= 19 # Is 9 less than or equal to 19?
```




    True


