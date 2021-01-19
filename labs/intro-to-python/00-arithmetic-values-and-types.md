#### GISC 420 T1 2021
# Arithmetic, values, types and string operations
Here we look at some of the most basic aspects of how Python handles items of data.

## Hello world
It's traditional when learning to program to first learn how to get the computer to 'say' "Hello world". Here's what that program looks like in Python:

```python
print('Hello world')
```
Type that in the IDLE console and see what happens.

## Python arithmetic
Try running the code snippets below and see what happens.
```python
40 + 2
```

```python
43 - 1
```

```python
6 * 7
```

```python
84 / 2
```
So... we can use Python as a not-so-simple calculator! Hurrah! Just what the world needs, another calculator. One of the other basic arithmetic *operators* is `**` which is used for 'raise to the power of'
```python
# Close enough
6.48 ** 2
```

```python
# What about this
42 ** 0.5
```

In the two lines above I've used *comments* which denoted by the `#` symbol. The Python interpreter ignores anything after a `#` symbol. Working interactively in IDLE, you can simply ignore these - they are there for your benefit as a human, and are irrelevant to the Python interpreter. This might seem pointless, but it is really useful to add comments to working code (i.e. scripts and programs) so that other human readers (most likely you 6 months later when you come back to the code) can understand what it is supposed to do.

## Values and types
Every item of data in Python has a *value* and a *type*. The value is the content of the data, like the numeric content **42** or the text content **Hello World!**. But these two values are of different types, one is a number, the other is some text. Python has some specific types which it is important to know about.
```python
type(42)
```

```python
type(42.0)
```

```python
type('42')
```
Here three pieces of data which humans might be inclined to consider identical are actually considered different because they are different types, `int`, `float`, and `str`.

+ an `int` is an *integer*, i.e., a numeric value with no decimal part
+ a `float` is a *floating point number*, i.e., a numeric value that has a decimal part
+ a `str` is a *string* denoting a sequence of characters

Strings are distinguished from numeric types by using quote marks. It is worth noting that we can use either single `''` or double `""` quote marks. As far as Python is concerned `'spam'` and `"spam"` are the same value:
```python
"spam" == 'spam'
```

We'll get to `==` in a bit. The fact that we can mix quote marks means that we can include them in a string, which is useful, so for example we can do
```python
print("'Hello, World!'")
```

How is this different from the first example of *hello world* at the start of these instructions?

## String operations
Numbers are manipulated using arithmetic operators such as `+`, `-`, `*` and so on, generally these don't make much sense for strings, although `+` and `*` still work.
```python
3 * 'spam'
```

```python
'spam' + 'ham'
```
