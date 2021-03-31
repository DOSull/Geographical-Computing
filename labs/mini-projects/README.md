#### GISC 420 T1 2021
# The 'big' assignment: ideas and scope
## A list of topic ideas
Here are some topic ideas to consider and discuss. To begin, don't worry too much about *how* think more about how much you are interested (or not) in each one. Alternatively think up an [idea of your own](#your-idea-here) to work on.

### Isochrones
Have a look at [this website](https://mapnificent.net), which enables you to generate public transport isochrones for a chosen location in many major cities (including Wellington, although I don't know if it has tried using the buses lately...).  You could also read [my masters dissertation](http://southosullivan.com/msc/mastersThesis.pdf) or [this paper](https://dx.doi.org/10.1080/136588100240976) I wrote based on it.

An isochrone map shows lines of equal travel time from an origin location, based on a specified form of transport. In some respects transit isochrone maps are more interesting than car or bike or walking ones. For car/bike/walking isochrones, take a look at [this example](https://github.com/gboeing/osmnx-examples/blob/master/notebooks/13-isolines-isochrones.ipynb), using [OSMnx](https://github.com/gboeing/osmnx). For transit isochrones, [GTFS data](http://gtfs.org/) are likely to be of interest&mdash;and there are even [ESRI tools available](https://esri.github.io/public-transit-tools/).

### Multitype Voronoi
Voronoi (or Thiessen or Dirichlet or proximity) polygons are heavily used in GIS and spatial analysis. Usually they are associated with a set of points. Christopher Gold has proposed that Voronoi regions be associated not only with points, but with lines and polygons, and that these form natural neighbourhood areas of the points, lines and polygons. Below is a simple example.  An early paper about this is [here](http://link.springer.com/10.1007/3-540-55966-3_13).

<img src="voronoi-brooklyn.png" width=60%><br />

I made this example with a series of steps in QGIS. The idea of this project would be to make some scripts that can take a combination of input layers of various kinds, and make a single set of Voronoi polygons from them.

### Gerrymandering and/or the US electoral college
It's always US election season and there's a presidential one coming up in a few months. Recent US electoral traumas have brought the issue of gerrymandering to increased public attention. There are various spatial dimensions to the issue and this project would involve exploring the issue by writing code that could generate alternative redistricting maps. For inspiration take a look at [Random States of America](http://fakeisthenewreal.org/random-states-of-america/) and [Redraw the States](http://kevinhayeswilson.com/redraw/). I did some work on this a while back and you can see code for that [here](https://github.com/data-8/geography-88/blob/master/session4/ASSIGNMENT-2-MAUP.ipynb).

### (Related) zone design for New Zealand
In the 2018 census, for the first time Statistics New Zealand introduced a level between meshblocks (80-100 people) and previously defined area units (3-5,000 people). The latter are now referred to as SA2 (Statistical Area 2) and the new intermediate level is called SA1. That innovation has made the original idea of this topic redundant.
However, more recent developments, specifically COVID19 have increased interest in 'regions' appropriate for managing a crisis such as this one. Given the health dimension, [District Health Boards](https://koordinates.com/layer/4324-nz-district-health-boards-2012/) seem the obvious unit, but for many purposes these are just too large. Perhaps [Territorial Authorities](https://koordinates.com/from/datafinder.stats.govt.nz/layer/25735/) are a better fit. These closely match Civil Defense zones. The broader problem is one of defining appropriate zoning systems for different purposes. Another example is the design of [transport analysis zones](https://dx.doi.org/10.1080/03081069708717601).

The **zone design problem** is a common one in GIS settings, and this project would seek to explore that topic, in whatever way you see fit.


### Cartograms
Cartograms are maps where areas are changed to represent something other than area on earth surface. A common example is for presenting election results. For example, see this discussion

https://onlinejournalismblog.com/2016/06/28/cartogram-or-election-map-the-guardian-vs-the-new-york-times/

of the pros and cons. Here's an example from fivethirtyeight.com

<img src="hexagram.png"><br />  

Note that cartograms don't have to use hexagons, although many do.

[This project](https://github.com/LokiTechnologies/equalareacartogram) can make hex cartograms from shapefiles or other inputs. This project could pick up from there and advance the method a bit further along in some way.

### Visibility graphs
Visibility graphs are networks where nodes represent locations or objects, and edges exist between the nodes if they are mutually visible. I did some early work on this [years ago](https://www.tandfonline.com/doi/pdf/10.1080/13658810151072859?needAccess=true) (sensing a theme here?).

You can probably do visibility analyses most easily using ESRI's products, so in this project I'd most likely expect you to figure out how to work with the needed ESRI python libraries to build visibility graphs.

### Accessibility measures
Isochrones are an example of one approach to measuring accessibility. More generally, we can look at things like the availability of bus routes, proximity to bus stops, frequency of services, proximity to rail stations. This topic would involve exploring such approaches, using GTFS data (see [above](#isochrones)).

### Your idea here
Something completely different!

## Scope and logistics
### Deliverable
You have the whole second half of trimester to work on this. The expectation in terms of a deliverable item is one (or more) of the following:

+ a Jupyter notebook or set of notebooks that explore ideas, explain code, and implement aspects of the selected topic; or
+ standalone python script that can apply the analysis method associated with your topic; or
+ ArcGIS or QGIS tools that implement the analysis method associated with your topic.

The last of these would involve figuring out model builder (Arc) or model designer (Q), or perhaps even plugins. I can help you with this, but we'll be learning together!

Alternative formats of submitted work are potentially allowable by agreement with me (arrange a meeting to discuss).

Any submitted work *must* be thoroughly commented (this is important) either in the code, or if you submit notebooks, in the markdown cells in the notebook.

### Alone or in a pair
You can work alone, or in a pair. I highly recommend the pair option. There is a lot to be said for [pair programming](https://en.wikipedia.org/wiki/Pair_programming) so whatever reservations you might have about group work, you should strongly consider this.

### Topic selection
We'll see how it goes on this, but my strong preference is that every project be different. I can consider two people or pairs working on the same topic, but would prefer that this not be the case.

### Tools etc.
We will spend time in class in the second half of semester on tools and approaches you need to make this work. Some of what we cover will depend on problems and challenges faced by groups as they arise.
