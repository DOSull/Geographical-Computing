#### GISC 420 T1 2021
# General instructions for the Labs
We will be using some different tools as the course progresses. Follow the relevant instructions below for different platforms.

To setup the environment for the class on your own machine you need to follow the instructions on [this page](setting-up-the-gisc-420-environment.ipynb).

## Week 1
This week you can use the lab machines:
+ Open the **Anaconda Prompt**.
+ Navigate to a folder where you plan to save work. First you may need to change disk, by typing `D:` or `H:` or whatever. Then you need to type `cd <path-to-folder>`.
+ Then, at the prompt, enable the GISC 420 environment with

      conda activate g420

  The prompt should change to the prefix `(g420)`.
+ Then run IDLE by typing either

      idle

  on Windows, or

      idle3

  on MacOS or Linux.

+ In IDLE start typing python commands per the instructions.

## Weeks 2 to 5
Each week, you should download the associated `.zip` file, **linked via the lab materials column in the timetable on the course main page** and extract it to a folder on your computer. In Windows be particularly careful to right-click and extract the files to an actual folder as many version of Windows let you look inside zip archives without actually extracting the files.

Once you have extracted the files, then follow the instructions below as required.

### On *Windows*
+ Open the **Anaconda Prompt**.
+ Navigate to the folder where you extracted the files. First you may need to change disk, by typing `D:` or `H:` or whatever. Then you need to type `cd <path-to-your-files>` where *path-to-your-files* is the directory you extracted the files.
+ Then, at the prompt, enable the GISC 420 environment with

      conda activate g420

  The prompt should change to the prefix `(g420)`.
+ Then run Jupyter notebook by typing

      jupyter notebook

  From there, things should be reasonably straightforward. Just remember to start with the `00-overview.ipynb` notebook!

### On *MacOS* or *Linux*
It is hard to give detailed instructions as setups may differ, but here are the steps:

+ Open a console.
+ Navigate to where you extracted the lab files.
+ Start the GISC 420 environment within

      conda activate g420

+ Run Jupyter notebook by typing

      jupyter notebook

# Weeks 6 through 11
Instructions will vary from week to week. By then you should be familiar enough with things to figure out what to do!
