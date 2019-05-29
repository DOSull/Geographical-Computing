# GISC 425 Emerging Topics in GIScience: Geographical Computing
Recent years have seen the (re)emergence of programmatic approaches to geographical information science and the de-emphasis of established desktop 'GIS' packages, both in research settings and in the commercial world. This class introduces the Python programming language and the Python geospatial ecosystem to prepare students for conducting research in this new context.

## Important dates
Item | Dates
 -: | :-
Trimester | 4 March to 29 June 2019
Teaching period | 4 March to 7 June 2019
Mid-trimester break | 15 April to 29 April 2019
Last assessment item due | 14 June 2019
Study period | NA
Examination period | NA
Withdrawal dates | See [Course additions and withdrawals](www.victoria.ac.nz/home/admisenrol/payments/withdrawalsrefunds)

If you cannot complete an assignment or sit a test or examination, refer to [Aegrotats](www.victoria.ac.nz/home/study/exams-and-assessments/aegrotat)

## Lecture and lab schedule
Lectures are in Cotton 110 at 10AM on Thursdays and will be followed immediately by related lab sessions in the same location. The combined session will last up to three hours, finishing up before 1PM.

## Contact details
### Lecturer/coordinator
**Prof. [David O'Sullivan](mailto:david.osullivan@vuw.ac.nz)**
**Office** CO227 **Extn.** 6492 **Office hours by appointment** [click here](http://calendly.com/dosullivan)

### GIS Technician
**[Andrew Rae](mailto:andrew.rae@vuw.ac.nz)**
**Office** CO502 **Office hours** TBD

## Lab and lecture timetable
Here's the trimester schedule we will aim to follow. **Bolded labs** have an associated assignment that must be submitted and contributes the indicated percentage of the course credit.  Relevant materials (lecture slides, lab scripts and datasets) are linked below, when available.

Week# | Date | Lecture topic | Lab topic | Notes
:----:|:---- |:------------- |:--------- |:---
1 | 7 Mar | Course overview; why python; variables and operators | [Introduction to code and setting up the GISC 425 environment](labs/week-1/week-1.zip?raw=true)
2 | 14 Mar | [Programming 1: functions and conditionals](https://southosullivan.com/gisc425/functions-and-conditionals/) | [**`geopandas`: working with spatial data using code**](labs/week-2/week-2.zip?raw=true) (5%) | due 20 Mar
3 | 21 Mar | [Programming 2: flow control and iteration](https://southosullivan.com/gisc425/loops-and-sequences/) | [**Repetive tasks and collections**](labs/week-3/week-3.zip?raw=true) (10%) | due 27 Mar
4 | 28 Mar | Programming 3: Dictionaries and a pause to review | [**Reclassify complex landuse data programmatically**](labs/week-4/week-4.zip?raw=true) (15%) | due 10 Apr
5 | 4 Apr | Programming 4: [Objects and APIs](labs/week-5/object-orientation.ipynb); [thinking algorithmically](https://www.youtube.com/watch?v=k2AqGongii0) | Thought experiment exercise |
6 | 11 Apr | `geopandas` as a GIS | [**Perform basic GIS operations in `geopandas`**](labs/week-6/week-6.zip?raw=true) (15%) | due 8 May
&nbsp; | Trimester break | | |
7 | 2 May | Introducing some potential project topics | [**Final programming project**](labs/week-7/longer-project-ideas-and-scope.md) (25%) | due 14 Jun
8 | 9 May | Beyond notebooks: virtual environments, IDEs and version control | Hands on with `conda`, `git`, and an IDE |  
9 | 16 May | [A glimpse of other languages: same only different](https://southosullivan.com/gisc425/other-languages/) | `R` `javascript` `java` `netlogo` |
10 | 23 May | Instructor out of town | Work on projects |
11 | 30 May | Web scraping | [`BeautifulSoup`](labs/week-11/web-scraping-in-python.ipynb?raw=true) |
12 | 6 Jun | Course review | **In class test** (30%)

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

When we come to the final assignment it will be more effective to work in an *Integrated Development Environment* (IDE) such as [PyCharm](https://www.jetbrains.com/pycharm/) and use a version control tool such as [git](https://git-scm.com/).

All these tools are freely available for all platforms (although there are a few wrinkles and variations between platforms). If you wish to replicate the lab set up on a personal machine, follow [these instructions](labs/week-1/setting-up-the-gisc-425-environment.ipynb).

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
`geopandas`: working with spatial data using code | 5% | 20 March | 1 2 3
Repetive processing tasks | 10% | 27 March | 2 3
Reclassify complex landuse data programmatically | 15% | 10 April | 1 3
Generate and customize a web map from multiple data layers | 15% | 31 May | 2 4
Programming mini-project | 25% | 14 June | 1 2 3 4
In class test | 30% | 6 June | 5

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
