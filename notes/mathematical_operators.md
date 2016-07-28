
# Mathematical Operators in Python

You've gotten your feet wet with ['Hello World'](python_intro.ipynb), but surely Python does more, right? Let's explore some of the things Python can do with numbers. Enter the following expression into your iPython prompt:


```python
1+2
```




    3



_Positively mind-blowing_. Okay, I get that this isn't the most profound example, but there's more going on here than meets the eye. Let's use our `type()` function from before to see what's happening under the hood:


```python
type(1+2) #Yes, a function can accept an expression as an argument!
```




    int



We see that Python is telling us about a different `type` of object here -- an `int`(eger)! It's telling us that the expression 1+2 yields an integer result. I wonder what other operations work here?


```python
2-1
```




    1




```python
3*4
```




    12




```python
4/3
```




    1.3333333333333333



Here we see the other typical mathematical operations in action -- subtraction, multiplication, and division. But what's going on with that last result? Surely _that_ can't be an `int`, can it?


```python
type(4/3)
```




    float



Ah, a new object type! Gotta catch 'em all! It turns out that 4/3 yields a `float` - a floating-point decimal.

Do exponents work too?


```python
3^2
```




    1



Um... certainly not what we expected. Don't make this mistake! In Python, we use the `**` operator to exponentiate. 

__Note__: If you're curious what the `^` did up there, it's an operation called bitwise XOR. It takes the binary representations of the two numbers, in this case 11 and 10, and 'adds' them digit by digit according to the following rule: return 1 if the digits are different, and 0 if they are the same. In this case, that gives you 01, which is the binary representation of the number 1. If you're still reading this, I love you.


```python
3**2
```




    9



Much better. Roots work this way as well (remember rational exponents?)


```python
9**(1/2)
```




    3.0




```python
type(9**(1/2))
```




    float



Note that this operation turns our `int` into a `float`. It'll be important to have a solid understanding of object types as your programs get more complex. 

One other operator worth learning is the `%`, or modulo operator. The expression `a % b` returns the remainder when `a` is divided by `b`.

For example:


```python
49 % 5
```




    4



Perhaps the most familiar application of modular arithmetic is determing whether a number is even or odd. We define even numbers as numbers that are divisible by two. Another way of saying that is numbers that are _congruent to zero mod 2_. Sounds fancy, but you already know what's up:


```python
28 % 2  
```




    0




```python
33 % 2
```




    1



Since 28 _mod_ 2 is 0, we know 28 is even. Since 33 _mod_ 2 is not 0, we know 33 is not even. Simple.

In some cases, mathematical operators are defined for some non-mathematical data types. For example:


```python
'Pika'*2 + 'Pi'
```




    'PikaPikaPi'



But in general, doing this blindly results in disappointment.


```python
'beer'**(1/2)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-15-965f23c1540b> in <module>()
    ----> 1 'beer'**(1/2)
    

    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'


Python doesn't get that the proper response would have been `'root beer'`. I'll see myself out...

Next: [Assignment](assignment.ipynb)
