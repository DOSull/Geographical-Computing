#### GISC 420 T1 2021
# GISC 420 Geographical Computing
Recent years have seen the (re)emergence of programmatic approaches to geographical information science and the de-emphasis of established desktop 'GIS' packages, both in research settings and in the commercial world. This class introduces the Python programming language and the Python geospatial ecosystem to prepare students for conducting research in this new context.

### Note on currency of material on this site
The pages on this site are continuously updated. While material evolves from earlier versions to that current for this year (2021) for lab materials in particular you should confirm that the heading indicates that the material is current for 2021 so that you don't waste time completing earlier versions of assignments!

## COVID Alert level changes
If COVID alert levels change, the class will continue as follows:
+ **Level 1** Class as normal. Attendance in person preferred, streamed content will be available at the link posted on Blackboard.
+ **Level 2** Room capacity will be reduced. We will determine which students and how many wish to attend in person consistent with those limitations. Otherwise as level 1.
+ **Level 3** or **Level 4** Class will be conducted solely over zoom with recordings available later for review.

## Link to video segments from zoom sessions
Some of these were recorded in 2020. However, they should still be useful as refreshers on the content covered

[https://southosullivan.com/gisc420/videos/](https://southosullivan.com/gisc420/videos/)

These videos will be updated as we get to that material in class this year.

## Important dates
Item | Dates
 -: | :-
Trimester | 22 February to 19 June 2021
Teaching period | 22 February to 28 May 2021
Mid-trimester break | 5 April to 16 April 2021
Last assessment item due (in this class) | **TBD**
Study period | NA
Examination period | NA
Withdrawal dates | See [Course additions and withdrawals](www.victoria.ac.nz/home/admisenrol/payments/withdrawalsrefunds)

If you cannot complete an assignment or sit a test or examination, refer to [Aegrotats](www.victoria.ac.nz/home/study/exams-and-assessments/aegrotat)

## Lecture and lab schedule
Lectures are in Cotton 110 at 9AM on Thursdays and will be followed immediately by related lab sessions in the same location. The combined session will last up to three hours, finishing before noon.

## Contact details
### Lecturer/coordinator
**Prof. [David O'Sullivan](mailto:david.osullivan@vuw.ac.nz)**
**Office** CO227 **Extn.** 6492 **Office hours preferably by appointment** [click here](http://calendly.com/dosullivan) but direct message me on [the Slack](https://vuwgisc2021.slack.com) and we can arrange contact. The office phone system is not a good way to reach me.

### GIS Technician
**[Andrew Rae](mailto:andrew.rae@vuw.ac.nz)**
**Office** CO502 **Office hours** 1-3PM Mondays

## Lab and lecture timetable
Here's the trimester schedule we will aim to follow. **Bolded labs** have an associated assignment that must be submitted and contributes the indicated percentage of the course credit.  Relevant materials (lecture slides, lab scripts and datasets) are linked below, when available.

Week# | Date | Lecture topic | [Lab materials](labs/README.md) | Notes
:----:|:---- |:------------- |:--------- |:---
1 | 25 Feb | Course overview; why python; variables and operators | [Introduction to Python code](labs/intro-to-python/README.md)
2 | 4 Mar | [Programming 1: functions and conditionals](labs/intro-to-geopandas/00-overview.ipynb) | [**`geopandas`: working with spatial data using code**](labs/intro-to-geopandas/intro-to-geopandas.zip?raw=true) (5%) | due 10 Mar
3 | 11 Mar | [Programming 2: flow control and iteration](labs/sequences-and-iteration/00-overview.ipynb) | [**Loops and iteration**](labs/sequences-and-iteration/sequences-and-iteration.zip?raw=true) (10%) | due 24 Mar
4 | 18 Mar | [Programming 3: Dictionaries](labs/dictionaries/00-overview.ipynb) | [**Reclassify complex landuse data programmatically**](labs/dictionaries/dictionaries.zip?raw=true) (15%) | due 31 Mar
5 | 25 Mar | [`geopandas` as a GIS](labs/geopandas-as-gis/00-overview.ipynb) | [**Perform basic GIS operations in `geopandas`**](labs/geopandas-as-gis/geopandas-as-gis.zip?raw=true) (15%) | due 28 Apr
6 | 1 Apr |  Beyond notebooks: virtual environments, IDEs and version control | Introducing some potential project topics<br />[**Mini-programming project**](labs/mini-projects/mini-project-ideas-and-scope.md) (30%) | due 31 May
 &nbsp; | 5 Apr - 16 Apr | **SEMESTER BREAK** | **NO TEACHING**
7 | 22 Apr | Programming 4: Objects and APIs; thinking algorithmically | [Object orientation](labs/object-orientation/object-orientation.ipynb) and thought experiment exercise |
8 | 29 Apr | QGIS and Arc APIs and plugins | Coming soon: material on working with `pyqgis` and/or `arcpy`. Work on projects |  
9 | 6 May | [A glimpse of other languages: same only different](https://southosullivan.com/gisc425/other-languages/) | Coming soon: some Javascript. Work on projects |
10 | 13 May | Lab only | Work on projects |
11 | 20 May | Course review (ask me anything!) | [`BeautifulSoup`](labs/web-scraping/web-scraping.zip?raw=true) |
12 | 27 May | &nbsp; | **In-class 'e-test'** (25%)

## Lectures
Lectures will generally consist of up to an hour of presented material, and up to 30 minutes of more open-ended discussion and Q&A based on the materials and on reading which students will have been expected to do ahead of class. After that we will dive into the associated lab materials.

### Readings
A really great introduction to Python is provided by this freely available PDF book (also available to purchase), from which readings will be assigned, especially in the first half of trimester.

+ Downey A. 2015. [*Think Python: How to think like a Computer Scientist*](http://greenteapress.com/thinkpython2/thinkpython2.pdf) 2nd edn. Green Tea Press, Needham, MA.

Other useful resources are found online and will be called out in lectures as we proceed. There will probably be readings set from

+ Crickard P, E van Rees and S Toms. 2018. [*Mastering Geospatial Analysis with Python*](https://www.packtpub.com/application-development/mastering-geospatial-analysis-python). Packt Publishing.

+ Westra E. 2016. [*Python geospatial development*](https://www.packtpub.com/application-development/python-geospatial-development) 3rd edn. Packt Publishing.

These are both accessible via a university subscription through the library, and PDFs are purchasable for only US$5.

## Labs
Lab sessions follow the lecture sessions and will cover related practical topics. General directions for the labs are found [here](labs/README.md). Five sessions have an associated assessed assignment, but you should attend all labs and participate fully to broaden your knowledge of GIScience methods and tools as any of the approaches covered may prove useful for you in other parts of the program. (Note also that a portion of the course credit is for participation in all aspects of the course.)

The final assignment may be organised in pairs or small groups, depending on differing student interests and skillsets.

### Software
Most of the lab work will be completed in [Jupyter Notebook](https://jupyter.org/) or similar [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) environments. These are good for incrementally becoming accustomed to code, then writing small amounts of code, building up to writing more extensive blocks of code.

When we come to the final assignment it may be more effective to work in an *Integrated Development Environment* (IDE) such as [VSCode](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) and use a version control tool such as [git](https://git-scm.com/).

All these tools are freely available for all platforms (although there are a few wrinkles and variations between platforms).

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
Since this is a relatively small graduate class, I expect that it will not be a problem to raise any issues or concerns directly with me, or with the GIS technician.

### Other useful resources
+ [Academic Integrity and Plagiarism](http://www.victoria.ac.nz/home/study/plagiarism)
+ [Aegrotats](http:\\www.victoria.ac.nz/home/study/exams-and-assessments/aegrotat)
+ [Academic Progress](http:\\www.victoria.ac.nz/home/study/academic-progress) (including restrictions and non-engagement)
+ [Dates and deadlines](http:\\www.victoria.ac.nz/home/study/dates)
+ [Grades](http:\\www.victoria.ac.nz/home/study/exams-and-assessments/grades)
+ [Resolving academic issues](http:\\www.victoria.ac.nz/home/about/avcacademic/publications2#grievances)
+ [Special passes](http:\\www.victoria.ac.nz/home/about/avcacademic/publications2#specialpass)
+ [Statutes and policies including the Student Conduct Statute](http:\\www.victoria.ac.nz/home/about/policy)
+ [Student support](http:\\www.victoria.ac.nz/home/viclife/studentservice)
+ [Students with disabilities](http:\\www.victoria.ac.nz/st_services/disability)
+ [Student Charter](http:\\www.victoria.ac.nz/home/viclife/student-charter)
+ [Student Contract](http:\\www.victoria.ac.nz/home/admisenrol/enrol/studentcontract)
+ [Turnitin](http:\\www.cad.vuw.ac.nz/wiki/index.php/Turnitin)
+ [University structure](http:\\www.victoria.ac.nz/home/about)
+ [VUWSA](http:\\www.vuwsa.org.nz)
