# Variables, expressions and statements
A *variable* in Python is a name that we associate with a value. We do this by *assigning* the value to a name using the `=` operator.

```python
>>> x = 17
>>> room = "Cotton 110"
>>> gravity = 9.8
```

Where did those values go? To retrieve them, we just ask Python for the values back again using their names.

```python
>>> x
```

```python
>>> room
```

```python
>>> gravity
```

Using assignment, we have created a label or name that we can use to refer to the value we assigned to it. Kind of like the picture below

Name | &nbsp; | Value
-:|:-:|:-
`x`| &rArr; | 17
`room` | &rArr; | "Cotton 110"
`gravity` | &rArr; | 9.8


If you have ever used a calculator with memory registers, this is a bit like that, but you can call things (more or less) whatever you want by giving it a name. Generally speaking, in programming we use variable names that are *meaningful in the context of the program*, so that we know what's going on. The variable names are another way that we make code readable and understandable by humans (the computer couldn't care less what you call things).

You can pretty much call a variable anything you want with a few restrictions, which will generally produce errors.

Variable names can't start with a number

```python
>>> 99redballoons = "weird song"
```

Variable names can't have any spaces

```python
>>> my variable = 'twenty seven'
```

So, instead of spaces, it is common in Python to use underscores

```python
>>> his_works = 'twenty seven'
```

There are also a bunch of 'reserved words' which we can't use. These are words that have a specific meaning in the Python programming language so calling a variable by them leads to confusion and errors. Generally they get coloured differently in any Python editing environment so you will know if you are doing this. Some reserved words are:

```python
False    class    finally  is       return
None     continue for      lambda   try
True     def      from     nonlocal while
and      del      global   not      with
as       elif     if       or       yield
assert   else     import   pass     break
except   in       raise
```

Try using one of these as a variable name and see what happens. For example:

```python
from = 'whence I came'
```

You can use uppercase letters, but it is conventional in Python not to do so (there is a reason for this which we'll get to eventually).

## Expressions and statements
Anything that evaluates to a value is an *expression*. This means that values on their own

```python
>>> 53
```

variables that have been assigned a value

```python
>>> x
```

and combinations of values, variables and operators (arithmetic or other kinds) are all expressions

```python
>>> x + 4 == 21
```

A *statement* is a bit of code that cause something to happen. The two things we've seen so far that do this are assignment statements

```python
>>> y = 19
```

and `print()` statements

```python
>>> print("this is a string, printed by a statement")
```

Note that a statement doesn't necessarily produce an effect that you can see. The statement `y = 19` above assigned the value 19 to the variable name `y`, but we can't tell that anything happened, unless we ask for the value of `y` back again.

### Order of evaluation in expressions
Like most programming languages, to avoid ambiguity Python has a priority order in which it evaluates operations in an expression.  Anything inside parentheses is evaluated first. Next comes any exponentiation (i.e., raising things to a power), then multiplication, division, addition and subtraction.

You may see this order referred to as **PEMDAS** for **P**arenetheses, **E**xponentiation, **M**ultiplication, **D**ivision, **A**ddition, **S**ubtraction, but this isn't particularly helpful to remember, as in other places it is called **BEDMAS** for **B**rackets, and the rest the same but slightly changed!

Based on this see if you can figure out, before running them, what the expression below will evaluate to.

```python
>>> 3 + 4 * 5 - 8 / 4
```

It's a lot less confusing to put parentheses in to make things clear

```python
>>> 3 + (4 * 5) - (8 / 4)
```

To change evaluation order, we can put parentheses in different places

```python
(3 + 4) * (5 - 8) / 4
```

Getting these rules wrong can lead to subtle errors in programs that are hard to find, so it makes sense to use brackets to guarantee things happen in the order you want!
