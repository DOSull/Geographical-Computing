#### GISC 420 T1 2022
# GISC 420 Geographical Computing
Recent years have seen the (re)emergence of programmatic approaches to geographical information science and the de-emphasis of established desktop 'GIS' packages, both in research settings and in the commercial world. This class introduces the Python programming language and the Python geospatial ecosystem to prepare students for conducting research in this new context.

### Note on currency of material on this site
The pages on this site are continuously updated. While material evolves from earlier versions to that current for this year (2022) for lab materials in particular you should confirm that the heading indicates that the material is current for 2022 so that you don't waste time completing earlier versions of assignments!

## COVID provisions
More information [here](covid.md). The class zoom session information is on [Blackboard](https://blackboard.vuw.ac.nz/webapps/blackboard/content/listContentEditable.jsp?content_id=_3363860_1&course_id=_117008_1&mode=reset "login required")

## Link to video segments from zoom sessions
A consolidated list of the video material for this class is available on [this page](video-links.md). Note that some video content is from earlier years, but remains relevant.

Item | Dates
 -- | --
Trimester | 28 February to 28 June 2022
Teaching period | 28 February to 3 June 2022
Mid-trimester break | 11 April to 25 April 2022
Last assessment item due | 3 June 2022
Study period | NA
Examination period | NA
Withdrawal dates | See [Course additions and  withdrawals](https://www.wgtn.ac.nz/home/admisenrol/payments/withdrawalsrefunds "Course additions and withdrawals")

If you cannot complete an assignment or sit a test or examination, refer to [Aegrotats](www.wgtn.ac.nz/home/study/exams-and-assessments/aegrotat)

## Lecture and lab schedule
Lectures are in Cotton 110 at 9AM on Tuesdays and will be followed immediately by related lab sessions in the same location. The combined session will last up to three hours, finishing before noon.

## Contact details
### Lecturer/coordinator
**Prof. [David O'Sullivan](mailto:david.osullivan@vuw.ac.nz)**
**Office** CO227 **Extn.** 6492 **Office hours preferably by appointment** [click here](https://calendly.com/dosullivan) but direct message me on [the Slack](https://vuwgisc4202022.slack.com) and we can arrange contact. The office phone system is not a good way to reach me!

### GIS Technician
**Wingya Su** email TBC
**Office** CO502 **Office hours** TBC

## Lab and lecture timetable
Here's the trimester schedule we will aim to follow. **Bolded labs** have an associated assignment that must be submitted and contributes the indicated percentage of the course credit.  Relevant materials (lecture slides, lab scripts and datasets) are linked below, when available.

Date | Lecture topic | [Lab materials](labs/README.md) | [Videos](video-links.md)
:-:|:-|:-|:-:
1 Mar | Course overview; why python; variables and operators | [Introduction to Python code](labs/intro-to-python/README.md) | [Videos](video-links.md#week-1-introduction)
8 Mar | [Programming 1](https://southosullivan.com/gisc420/functions-and-conditionals/) functions and conditionals | [**`geopandas`: working with spatial data using code**](labs/intro-to-geopandas/intro-to-geopandas.zip?raw=true) (5%) due 14 Mar | [Videos](video-links.md#week-2-functions-and-conditionals)
15 Mar | [Programming 2](https://southosullivan.com/gisc420/sequences-and-iteration/): Loops, strings, and lists | [**Loops and iteration**](labs/sequences-and-iteration/sequences-and-iteration.zip?raw=true) (10%) due 28 Mar | [Videos](video-links.md#week-3-iteration-and-sequences)
22 Mar | [Programming 3](labs/dictionaries/00-overview.ipynb): Dictionaries | [**Reclassify complex landuse data programmatically**](labs/dictionaries/dictionaries.zip?raw=true) (15%) due 4 Apr | [Videos](video-links.md#week-4-dictionaries-and-data-decoding)
29 Mar | [`geopandas` as a GIS](labs/geopandas-as-gis/00-overview.ipynb) | [**Perform basic GIS operations in `geopandas`**](labs/geopandas-as-gis/geopandas-as-gis.zip?raw=true) (15%) due 2 May | [Videos](video-links.md#week-5-geopandas-as-a-gis)
5 Apr | Programming 4: [Objects](labs/object-orientation/object-orientation.ipynb) [[download notebook](labs/object-orientation/object-orientation.ipynb?raw=true)] and APIs; thinking algorithmically | Introducing some potential project topics<br />[**Mini-programming project**](labs/mini-projects/) (30%) due 3 Jun
&nbsp; | **SEMESTER BREAK** | **NO TEACHING**
26 Apr | Beyond notebooks: virtual environments, IDEs and version control | A look at the `shapely` API<br />work on mini-projects | [Videos](video-links.md#week-7-object-orientation)
3 May | [Web-scraping and the DOM](labs/web-scraping/web-scraping-in-python.ipynb) | [`BeautifulSoup`](labs/web-scraping/web-scraping-in-python.ipynb?raw=true) | [Videos](video-links.md#week-8-web-scraping)
10 May | [Automating QGIS](labs/pyqgis/Exploring%20the%20python%20QGIS%20API.ipynb) | the [materials](labs/pyqgis/pyqgis.zip?raw=true) | [Videos](video-links.md#week-9-automating-gis-with-python)
17 May | [A glimpse of other languages: same only different](https://southosullivan.com/gisc420/other-languages/) | [`pydeck` - making JavaScript using Python](labs/deck/tereo-name-pydeck-example.ipynb) |
24 May | Course review (ask me anything!) | Working on mini-projects
31 May | **In-class 'e-test'** (25%) | Working on mini-projects

## Lectures
Lectures will generally consist of an hour or so of presented material, and up to 30 minutes of more open-ended discussion and Q&A based on the materials and on reading which students will have been expected to do ahead of class. After that we will dive into lab materials.

### Readings  
A really great introduction to Python is provided by this freely available PDF book (also available to purchase), from which readings will be assigned, especially in the first half of trimester.

+ Downey A. 2015. [*Think Python: How to Think Like a Computer Scientist*](https://greenteapress.com/thinkpython2/thinkpython2.pdf) 2nd edn. Green Tea Press, Needham, MA.

Other useful resources are generally found online and will be called out in lectures as we proceed or provided via Blackboard if needed.

## Labs
Lab sessions follow the lecture sessions and will cover related practical topics. General directions for the labs are found [here](labs/README.md). Five sessions have an associated assessed assignment, but you should attend all labs and participate fully to broaden your knowledge of python geospatial methods and tools (we're all here to learn, after all!).

The final mini-project assignment may be organised in pairs or small groups, depending on differing student interests and skillsets.

### Software
Most of the lab assessments will be completed in [Jupyter Notebook](https://jupyter.org/) or similar [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) environments. These are good for incrementally becoming accustomed to code, then writing small amounts of code, building up to writing more extensive blocks of code.

When we come to the mini-project assignment it will probably be more effective to work in an *Integrated Development Environment* (IDE) such as [VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) and use a version control tool such as [git](https://git-scm.com/).

All these tools are freely available (although there are a few wrinkles and variations between platforms). We will introduce these in class as needed. All are available on the lab machines, but you may prefer to work on your own computer.

## Course learning objectives (CLOs)
1. manage, analyse, visualize and present spatial data using a range of programming tools
2. configure and manage a computing environment suitable for geographical information analysis
3.automate geographic information analysis workflows
4. setup and manage version control for geographical analysis projects
5. Specify an appropriate combination of tools and languages suitable for the conduct of any well-defined geographical data management and analysis project

## Assessment
This course is 100% internally assessed.  Assessment is based on four lab assignments worth 12.5% of overall course credit each, and a final assignment worth 50% of course credit due in the exam period.

Assessment item | Credit | Due date | CLOs
:- | :-: | :-: | :-
`geopandas`: working with spatial data using code | 5% | 14 March | 1 2 3
Loops and iteration | 10% | 28 March | 2 3
Reclassify complex landuse data programmatically | 15% | 4 April | 1 3
Using `geopandas` as a GIS | 15% | 2 May | 2 4
Programming mini-project | 30% | 3 June | 1 2 3 4
In class test | 25% | 31 May | 5

Assessments are submitted electronically via dropbox on [Blackboard](https://blackboard.vuw.ac.nz/). I will aim to return coursework within 3 weeks. Extensions should be requested from the SGEES administration office. If you anticipate problems come and talk to me.

### Late submission penalties
All assignments must be handed in by their due dates. Non-submission  by the required date will result in a 5% penalty  off your grade for that assignment for each day or part thereof that the coursework is late.  No submissions will be accepted more than 5 days after the due date.

Computer crash or similar excuses are not acceptable. Save your material and make sure you have something to submit by the due date.

### Non-assessed lab work
Note that there are also non-assessed lab sessions. These will be important for your ability to complete the final assignment effectively and to your all-around training in GIScience, so it is vital that you take them seriously as part of the course.

## Additional information
The primary mode of communication for the course will be via Blackboard, so please ensure that your contact details there are up to date and are regularly checked (note that Blackboard defaults to your myvuw email address).

### Class representatives
A volunteer is needed to act as class representative. If you are interested let me know. Further information about the role is available [here](https://www.vuwsa.org.nz/class-representatives/). Given the small size of the class, we might be OK without.

### Other useful resources
The links below may be useful if you need help, advice, or any other more general information about relevant university policies and resources.
+ [Academic Integrity and Plagiarism](https://www.wgtn.ac.nz/home/study/plagiarism)
+ [Aegrotats](https://www.wgtn.ac.nz/home/study/exams-and-assessments/aegrotat)
+ [Academic Progress](https://www.wgtn.ac.nz/home/study/academic-progress) (including restrictions and non-engagement)
+ [Dates and deadlines](https://www.wgtn.ac.nz/home/study/dates)
+ [Grades](https://www.wgtn.ac.nz/home/study/exams-and-assessments/grades)
+ [Statutes and policies including the Student Conduct Statute](https://www.wgtn.ac.nz/students/study/academic-policies)
+ [Student support](https://www.wgtn.ac.nz/students/support)
+ [Students with disabilities](https://www.wgtn.ac.nz/disability)
+ [Student Charter](https://www.wgtn.ac.nz/learning-teaching/partnership/student-charter)
+ [VUWSA](https://www.vuwsa.org.nz)
