# Variables, expressions and statements
A *variable* in Python is a name that we associate with a value. We do this by *assigning* the value to a name using the `=` operator.


```python
x = 17
room = "Cotton 110"
gravity = 9.8
```

Where did those values go? To retrieve, we just ask Python for the values back again.


```python
x
```


```python
room
```


```python
gravity
```

Using assignment, we have created a label that we can use to refer to the value we assigned to it. Kind of like the picture below

Name  | &nbsp;   | Value
----: | :------: | :-----
`x`| &rarr; | 17
`room` | &rarr; | "Cotton 110"
`gravity` | &rarr; | 9.8


If you have ever used a calculator with memory registers, it is a bit like that, but you can call things whatever you want. Generally speaking, in programming we use variable names that are meaningful in the context of the program, so that we know what's going on.

You can pretty much call a variable anything you want with a few restrictions, which will generally produce errors.

Variable names can't start with a number


```python
99redballoons = "weird song"
```

Variable names can't have any spaces


```python
my variable = 'twenty seven' 
```

Instead of spaces, it is common to use underscores


```python
this_works = 'twenty seven'
```

There are a bunch of 'reserved words' which we can't use. These are words that have a specific meaning in terms of the language. Generally they get coloured differently in any development environment so you will know if you are doing this. The reserved words are
```
False    class    finally  is       return
None     continue for      lambda   try
True     def      from     nonlocal while
and      del      global   not      with
as       elif     if       or       yield
assert   else     import   pass     break
except   in       raise
```
Try using one of these as a variable name in the cell below and see what happens


```python
## Add code below to assign a value to a forbidden variable name
```

You can use uppercase letters, but it is conventional in Python not to do so (there is a reason for this which we'll get to eventually).

## Expressions and statements
Anything that evaluates to a value is an *expression*. This means that values on their own


```python
53
```

variables that have been assigned a value


```python
x
```

and combinations of values, variables and operators (arithmetic or other kinds) are all expressions


```python
x + 4 == 21
```

A *statement* is a bit of code that cause something to happen. The two things we've seen so far that do this are assignment statements


```python
y = 19
```

and `print()` statements


```python
print('this is a statement')
```

Note that a statement doesn't necessarily produce an effect that you can see. The statement `y = 19` above assigned the value 19 to the variable `y`, but we can't tell that anything happened, unless we ask for the value of `y`


```python
y
```

### Order of evaluation in expressions
Like most programming languages, to avoid ambiguity Python has a priority order in which it evaluates operations in an expression.  Anything inside parentheses is evaluated first. Next comes any exponentiation (i.e., raising things to a power), then multiplication, division, addition and subtraction.

Based on this see if you can figure out, before running them, what the cell below will evaluate to.


```python
3 + 4 * 5 - 8 / 4
```

It's a lot less confusing to put parentheses in to make things clear


```python
3 + (4 * 5) - (8 / 4)
```

To change evaluation order, we can put parentheses in different places


```python
(3 + 4) * (5 - 8) / 4 
```


```python

```
