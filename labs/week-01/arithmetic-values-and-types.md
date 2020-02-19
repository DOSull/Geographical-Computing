#### GISC 425 T1 2020
# Arithmetic, values, types and string operations
Here we look at some of the most basic aspects of how Python handles items of data.

## Hello world
We've already seen the traditional *hello world* program in Python.

As a reminder, here it is again, only more reserved this time.


```python
print('Hello world')
```

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

The two cells above also make use of *comments* which are denoted by the `#` symbol. The Python interpreter ignores anything after a `#` symbol. This might seem pointless, but it is really useful to add comments to code so that other human readers (most likely you 6 months later when you come back to the code) can understand what it is supposed to do.

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

Here three pieces of data which we as humans might be inclined to consider identical are actually considered different because they are different types, `int`, `float`, and `str`.

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

Make sure you understand how this is different from the first example of *hello world*.

## String operations
Numbers are manipulated using arithmetic operators such as `+`, `-`, `*` and so on, generally these don't make much sense for strings, although `+` and `*` still work.


```python
3 * 'spam'
```


```python
'spam' + 'ham'
```


```python

```
