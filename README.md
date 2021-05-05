#### GISC 420 T1 2021
# GISC 420 Geographical Computing
Recent years have seen the (re)emergence of programmatic approaches to geographical information science and the de-emphasis of established desktop 'GIS' packages, both in research settings and in the commercial world. This class introduces the Python programming language and the Python geospatial ecosystem to prepare students for conducting research in this new context.

### Note on currency of material on this site
The pages on this site are continuously updated. While material evolves from earlier versions to that current for this year (2021) for lab materials in particular you should confirm that the heading indicates that the material is current for 2021 so that you don't waste time completing earlier versions of assignments!

## COVID Alert level changes
If COVID alert levels change, the class will continue as follows:
+ **Level 1** Class as normal. Attendance in person preferred, streamed content will be available at the link posted on Blackboard. **Stay home if you are unwell**.
+ **Level 2** Room entry must be recorded using COVID app and/or the sign-in sheet. Sanitise hands on entry and exit from the lab. Wipe down your workstation (keyboard, mouse) with wipes provided at start and end of session. And, since the sessions are 3 hours long, wear a mask. As at other levels class will be streamed and recorded for those unwilling or unable to attend. Above all **stay home if you are unwell**.
+ **Level 3** or **Level 4** Class will be conducted solely over zoom with recordings available later for review.

## Link to video segments from zoom sessions
A consolidated list of the video material for this class is available on [this page](video-links.md).

## Important dates
Item | Dates
 -: | :-
Trimester | 22 February to 19 June 2021
Teaching period | 22 February to 28 May 2021
Mid-trimester break | 5 April to 16 April 2021
Last assessment item due (in this class) | 31 May 2021
Study period | NA
Examination period | NA
Withdrawal dates | See [Course additions and withdrawals](www.wgtn.ac.nz/home/admisenrol/payments/withdrawalsrefunds)

If you cannot complete an assignment or sit a test or examination, refer to [Aegrotats](www.wgtn.ac.nz/home/study/exams-and-assessments/aegrotat)

## Lecture and lab schedule
Lectures are in Cotton 110 at 9AM on Thursdays and will be followed immediately by related lab sessions in the same location. The combined session will last up to three hours, finishing before noon.

## Contact details
### Lecturer/coordinator
**Prof. [David O'Sullivan](mailto:david.osullivan@vuw.ac.nz)**
**Office** CO227 **Extn.** 6492 **Office hours preferably by appointment** [click here](https://calendly.com/dosullivan) but direct message me on [the Slack](https://vuwgisc2021.slack.com) and we can arrange contact. The office phone system is not a good way to reach me.

### GIS Technician
**[Andrew Rae](mailto:andrew.rae@vuw.ac.nz)**
**Office** CO502 **Office hours** 1-3PM Mondays

## Lab and lecture timetable
Here's the trimester schedule we will aim to follow. **Bolded labs** have an associated assignment that must be submitted and contributes the indicated percentage of the course credit.  Relevant materials (lecture slides, lab scripts and datasets) are linked below, when available.

Week# | Date | Lecture topic | [Supporting materials](labs/README.md) | Notes | [Videos](video-links.md)
:----:|:---- |:------------- |:--------- |:--- | :--
1 | 25 Feb | Course overview; why python; variables and operators | [Introduction to Python code](labs/intro-to-python/README.md) | | [Videos](video-links#week-1-introduction)
2 | 4 Mar | [Programming 1](https://southosullivan.com/gisc420/functions-and-conditionals/) functions and conditionals | [**`geopandas`: working with spatial data using code**](labs/intro-to-geopandas/intro-to-geopandas.zip?raw=true) (5%) | due 10 Mar | [Videos](video-links.md#week-2-functions-and-conditionals)
3 | 11 Mar | [Programming 2](https://southosullivan.com/gisc420/sequences-and-iteration/): Loops, strings, and lists | [**Loops and iteration**](labs/sequences-and-iteration/sequences-and-iteration.zip?raw=true) (10%) | due 24 Mar | [Videos](video-links.md#week-3-iteration-and-sequences)
4 | 18 Mar | [Programming 3](labs/dictionaries/00-overview.ipynb): Dictionaries | [**Reclassify complex landuse data programmatically**](labs/dictionaries/dictionaries.zip?raw=true) (15%) | due 31 Mar | [Videos](video-links.md#week-4-dictionaries-and-data-decoding)
5 | 25 Mar | [`geopandas` as a GIS](labs/geopandas-as-gis/00-overview.ipynb) | [**Perform basic GIS operations in `geopandas`**](labs/geopandas-as-gis/geopandas-as-gis.zip?raw=true) (15%) | due 28 Apr | [Videos](video-links.md#week-5-geopandas-as-a-gis)
6 | 1 Apr |  Beyond notebooks: virtual environments, IDEs and version control | Introducing some potential project topics<br />[**Mini-programming project**](labs/mini-projects/) (30%) | due 31 May
 &nbsp; | 5 Apr - 16 Apr | **SEMESTER BREAK** | **NO TEACHING**
7 | 22 Apr | Programming 4: [Objects](labs/object-orientation/object-orientation.ipynb) and APIs; thinking algorithmically | A look at the `shapely` API<br />work on mini-projects
8 | 29 Apr | [Web-scraping and the DOM](labs/web-scraping/web-scraping-in-python.ipynb) | [`BeautifulSoup`](labs/web-scraping/web-scraping-in-python.ipynb?raw=true)
9 | 6 May | [Automating QGIS](labs/pyqgis/Exploring%20the%20python%20QGIS%20API.ipynb) | the [materials](labs/pyqgis/pyqgis.zip?raw=true)
10 | 13 May | [A glimpse of other languages: same only different](https://southosullivan.com/gisc420/other-languages/) | `pydeck` - making JavaScript using Python
11 | 20 May | Course review (ask me anything!) | Working on mini-projects
12 | 27 May | **In-class 'e-test'** (25%) | Working on mini-projects

## Lectures
Lectures will generally consist of up to an hour of presented material, and up to 30 minutes of more open-ended discussion and Q&A based on the materials and on reading which students will have been expected to do ahead of class. After that we will dive into the associated lab materials.

### Readings  
A really great introduction to Python is provided by this freely available PDF book (also available to purchase), from which readings will be assigned, especially in the first half of trimester.

+ Downey A. 2015. [*Think Python: How to think like a Computer Scientist*](https://greenteapress.com/thinkpython2/thinkpython2.pdf) 2nd edn. Green Tea Press, Needham, MA.

Other useful resources are generally found online and will be called out in lectures as we proceed or provided via Blackboard if needed.

<!--There will probably be readings set from

+ Crickard P, E van Rees and S Toms. 2018. [*Mastering Geospatial Analysis with Python*](https://www.packtpub.com/application-development/mastering-geospatial-analysis-python). Packt Publishing.

+ Westra E. 2016. [*Python geospatial development*](https://www.packtpub.com/application-development/python-geospatial-development) 3rd edn. Packt Publishing.

These are both accessible via a university subscription through the library, and PDFs are purchasable for only US$5.-->

## Labs
Lab sessions follow the lecture sessions and will cover related practical topics. General directions for the labs are found [here](labs/README.md). Five sessions have an associated assessed assignment, but you should attend all labs and participate fully to broaden your knowledge of GIScience methods and tools as any of the approaches covered may prove useful for you in other parts of the program.

The final assignment may be organised in pairs or small groups, depending on differing student interests and skillsets.

### Software
Most of the lab assessments will be completed in [Jupyter Notebook](https://jupyter.org/) or similar [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) environments. These are good for incrementally becoming accustomed to code, then writing small amounts of code, building up to writing more extensive blocks of code.

When we come to the mini-project assignment it will be more effective to work in an *Integrated Development Environment* (IDE) such as [VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) and use a version control tool such as [git](https://git-scm.com/).

All these tools are freely available for all platforms (although there are a few wrinkles and variations between platforms). We will look at these in class in week 6.

## Course learning objectives (CLOs)
1. manage, analyse, visualize and present spatial data using a range of programming tools
2. configure and manage a computing environment suitable for geographical information analysis
3.automate geographic information analysis workflows
4. setup and manage version control for geographical analysis projects
5. Specify an appropriate combination of tools and languages suitable for the conduct of any well-defined geographical data management and analysis project

## Assessment
This course is 100% internally assessed.  Assessment is based on four lab assignments worth 12.5% of overall course credit each, and a final assignment worth 50% of course credit due in the exam period.

Assessment item | Credit | Due date | CLOs
:- | :-: | :-: | :-:
`geopandas`: working with spatial data using code | 5% | 10 March | 1 2 3
Loops and iteration | 10% | 24 March | 2 3
Reclassify complex landuse data programmatically | 15% | 31 March | 1 3
Using `geopandas` as a GIS | 15% | 28 April | 2 4
Programming mini-project | 30% | 31 May | 1 2 3 4
In class test | 25% | 27 May | 5

Assessments are submitted electronically via dropbox on [Blackboard](https://blackboard.vuw.ac.nz/). I will aim to return coursework within 3 weeks. Extensions should be requested from the SGEES administration office. If you anticipate problems come and talk to me.

### Late submission penalties
All assignments must be handed in by their due dates. Non-submission  by the required date will result in a 5% penalty  off your grade for that assignment for each day or part thereof that the coursework is late.  No submissions will be accepted more than 5 days after the due date.

Computer crash or similar excuses are not acceptable. Save your material and make sure you have something to submit by the due date.

### Non-assessed lab work
Note that there are also non-assessed lab sessions. These will be important for your ability to complete the final assignment effectively and to your all-around training in GIScience, so it is vital that you take them seriously as part of the course.

## Additional information
The primary mode of communication for the course will be via Blackboard, so please ensure that your contact details there are up to date and are regularly checked (note that Blackboard defaults to your myvuw email address).

### Class representatives
A volunteer is need to act as class representative. If you are interested let me know. Further information about the role is available [here](https://www.vuwsa.org.nz/class-representatives/).

### Other useful resources
+ [Academic Integrity and Plagiarism](https://www.wgtn.ac.nz/home/study/plagiarism)
+ [Aegrotats](https://www.wgtn.ac.nz/home/study/exams-and-assessments/aegrotat)
+ [Academic Progress](https://www.wgtn.ac.nz/home/study/academic-progress) (including restrictions and non-engagement)
+ [Dates and deadlines](https://www.wgtn.ac.nz/home/study/dates)
+ [Grades](https://www.wgtn.ac.nz/home/study/exams-and-assessments/grades)
+ [Resolving academic issues](https://www.wgtn.ac.nz/home/about/avcacademic/publications2#grievances)
+ [Special passes](https://www.wgtn.ac.nz/home/about/avcacademic/publications2#specialpass)
+ [Statutes and policies including the Student Conduct Statute](https://www.wgtn.ac.nz/home/about/policy)
+ [Student support](https://www.wgtn.ac.nz/home/viclife/studentservice)
+ [Students with disabilities](https://www.wgtn.ac.nz/st_services/disability)
+ [Student Charter](https://www.wgtn.ac.nz/learning-teaching/partnership/student-charter)
+ [Student Contract](https://www.wgtn.ac.nz/home/admisenrol/enrol/studentcontract)
+ [Turnitin](http://www.cad.vuw.ac.nz/wiki/Turnitin.html)
+ [VUWSA](https://www.vuwsa.org.nz)
