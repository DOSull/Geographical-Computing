#### GISC 425 T1 2020
# It's turtles all the way down
Right. So the API documentation for `turtle` is available [here](https://docs.python.org/3/library/turtle.html). That is where you should look for information on things that are unclear.

For now, I am going to provide a supplement to Chapter 4 in [_Think Python_](https://greenteapress.com/wp/think-python-2e/).

## The `turtle` module
To 'fire it up' we make a turtle. We'll call ours something more local.


```python
aroha = turtle.Turtle()
```

You should see a blank window appear with a little black triangle at its centre. This is `aroha` our first `Turtle` to whom we can issue commands using function calls that will cause her (?!) to draw things in the window. The `fd(x)` function causes the `Turtle` object asked to execute it to move `x` units forward. There is also a `bk(x)` command to cause a `Turtle` to move backwards.


```python
aroha.fd(100)
```

We can also ask a `Turtle` to change direction with the `right(x)` or `left(x)` function which causes the turtle to turn in the appropriate direction through an angle of `x` degrees. These functions can also be abbreviated as `rt(x)` or `lt(x)`.


```python
aroha.right(90)
```

Now if we issue a forward command, the line will get drawn at an angle to the previous one.


```python
aroha.fd(100)
```

That's enough to get the general idea. It is also useful, before continuing to be able to reset the screen and send `aroha` back to her start location.


```python
aroha.reset()
```

## Simple repetition
So... in the cell below right some code to make `aroha` draw a square.


```python
# Write code below to make aroha draw a square
# You will need the Turtle(), fd(), and rt() functions
# Take another look at the cells above if you are unsure what to do


```

The book tells you what you most likely wrote. It probably involved some repetition, which even allowing for copy and paste is pretty tedious to deal with.

Thankfully, much of programming is all about repetition, so we have a construct in Python that allows us to repeat actions many times. For example


```python
# Simple repetition
for i in range(4):
    print("Here we go again")
```

With that in mind, rewrite your square drawing code to use a `for` loop.


```python
# Write code here using a for loop to make aroha draw a square

```

## Exercises from section 4.3
These are taken directly from _Think Python_. In each case write the code in the cell below the instructions.

1. Write a function called `square` that takes a parameter named `t`, which is a turtle. It should use the turtle to draw a square.

   Write a function call that passes bob as an argument to square, and then run the program again.


```python
## I'll give you the function definition code to get you started

def square(t):
    print("Replace this print statement with code to draw a square")


## and here's a line of code to run the function
square(aroha)
```

2. Add another parameter, named `length`, to `square`. Modify the body so length of the
sides is `length`, and then modify the function call to provide a second argument. Run
the program again. Test your program with a range of values for length.


```python
## Again here's a function header

def square(t, length):
    print("You know what to do")
```

3. Make a copy of the `square` function code and change the name to `polygon`. Add another parameter
named `n` and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees.


```python
## No clues this time
```

### The next two are optional for now

4. Write a function called circle that takes a turtle, t , and radius, r , as parameters and
that draws an approximate circle by calling polygon with an appropriate length and
number of sides. Test your function with a range of values of r .
Hint: figure out the circumference of the circle and make sure that length * n =
circumference .


```python

```

5. Make a more general version of circle called arc that takes an additional parameter
angle , which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360 , arc should draw a complete circle.

## Read the book!
The book spells out nicely how to complete these tasks in sections 4.4 to 4.7 and I suggest that you work through those while working on this notebook.

## Clean up
I haven't quite figured out how to clean up after the `turtle` module. The cell below should work, but may still require you to 'X' out of the graphics window.


```python
turtle.done()
```


```python

```
