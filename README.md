# Geographical Computing
These pages outline a one semester (36 contact hours) class in python programming for geospatial that was last taught at Victoria University of Wellington as GISC 420 in the first half of 2022.

I am still in the process of cleaning the materials up for potential conversion into training materials. For the time being the materials are provided _gratis_ with no warrant as to their accuracy as a guide to python programming for geospatial but you may still find them useful all the same!

## Link to video segments from zoom sessions
A consolidated list of the video material for this class is available on [this page](video-links.md). Note that some video content is from earlier years, but remains relevant.

## Lab and lecture timetable
Here's a 12 week schedule for the course.

Week | Lecture topic | [Lab materials](labs/README.md) | [Videos](video-links.md)
:-:|:-|:-|:-:
1 | Course overview; why python; variables and operators | [Introduction to Python code](labs/intro-to-python/README.md) | [Videos](video-links.md#week-1-introduction)
2 | [Programming 1](https://southosullivan.com/gisc420/functions-and-conditionals/) functions and conditionals | [**`geopandas`: working with spatial data using code**](labs/intro-to-geopandas/intro-to-geopandas.zip?raw=true) (5%) | [Videos](video-links.md#week-2-functions-and-conditionals)
3 | [Programming 2](https://southosullivan.com/gisc420/sequences-and-iteration/): Loops, strings, and lists | [**Loops and iteration**](labs/sequences-and-iteration/sequences-and-iteration.zip?raw=true) (10%) | [Videos](video-links.md#week-3-iteration-and-sequences)
4 | [Programming 3](labs/dictionaries/00-overview.ipynb): Dictionaries | [**Reclassify complex landuse data programmatically**](labs/dictionaries/dictionaries.zip?raw=true) (15%) | [Videos](video-links.md#week-4-dictionaries-and-data-decoding)
5 | [`geopandas` as a GIS](labs/geopandas-as-gis/00-overview.ipynb) | [**Perform basic GIS operations in `geopandas`**](labs/geopandas-as-gis/geopandas-as-gis.zip?raw=true) (15%) | [Videos](video-links.md#week-5-geopandas-as-a-gis)
6 | Programming 4: [Objects](labs/object-orientation/object-orientation.ipynb) [[right-click download](labs/object-orientation/object-orientation.ipynb?raw=true)] and APIs; thinking algorithmically | Introducing some potential project topics<br />[**Mini-programming project**](labs/mini-projects/) (30%) [Videos](video-links.md#week-6-object-orientation)
7 | [Random other stuff](labs/random-other-stuff/00-overview.ipynb) | [Random other stuff materials](labs/random-other-stuff/random-other-stuff.zip?raw=true)<br />Setting up working environments for the projects | [Videos](video-links.md#week-7-random-other-stuff-and-working-environments)
8 | [Web-scraping and the DOM](labs/web-scraping/web-scraping-in-python.ipynb) | [`BeautifulSoup`](labs/web-scraping/web-scraping-in-python.ipynb?download=true) | [Videos](video-links.md#week-8-web-scraping)
9 | [Automating QGIS](labs/pyqgis/Exploring%20the%20python%20QGIS%20API.ipynb) | the [materials](labs/pyqgis/pyqgis.zip?raw=true) | [Videos](video-links.md#week-9-automating-gis-with-python)
10 | [A glimpse of other languages: same only different](https://southosullivan.com/gisc420/other-languages/) | [`pydeck` - making JavaScript using Python](labs/deck/tereo-name-pydeck-example.ipynb) |
11 | Course review (ask me anything!) | Working on mini-projects
12 | **In-class 'e-test'** (25%) | Working on mini-projects

### Readings  
A really great introduction to Python is provided by this freely available PDF book (also available to purchase), from which readings will be assigned, especially in the first half of trimester.

+ Downey A. 2015. [*Think Python: How to Think Like a Computer Scientist*](https://greenteapress.com/thinkpython2/thinkpython2.pdf) 2nd edn. Green Tea Press, Needham, MA.

Other useful resources are generally found online and will be called out in lectures as we proceed or provided via Blackboard if needed.

### Software
Most of the lab assessments will be completed in [Jupyter Notebook](https://jupyter.org/) or similar [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) environments. These are good for incrementally becoming accustomed to code, then writing small amounts of code, building up to writing more extensive blocks of code.

For the mini-project assignment it will probably be more effective to work in an *Integrated Development Environment* (IDE) such as [VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) and use a version control tool such as [git](https://git-scm.com/).

All these tools are freely available (although there are a few wrinkles and variations between platforms). We will introduce these in class as needed. All are available on the lab machines, but you may prefer to work on your own computer.

