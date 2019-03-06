# General instructions for the Labs
Each week, you should download the associated `week-n.zip` file and extract it to a folder on your computer. In Windows be particularly careful to right-click and extract the files to an actual folder as many version of Windows let you look inside zip archives without actually extracting the files.

Once you have extracted the files, then follow the instructions below as required.

## On *Windows*
+ Open the **Anaconda Prompt**.
+ Navigate to the folder where you extracted the files. First you may need to change disk, by typing `D:` or `H:` or whatever. Then you need to type `cd <path-to-your-files>` where *path-to-your-files* is the directory you extracted the files.
+ Then, at the prompt, enable the GISC 425 environment within
      conda activate gisc425
  The prompt should change to the prefix `(gisc425)`.
+ Then run Jupyter Lab by typing
      jupyter lab
  From there, things should be reasonably straightforward.

## On *MacOS* or *Linux*
Here it is assumed you have followed instructions on [this page](week-1/setting-up-the-gisc-425-environment.ipynb) to set up for the course.

+ Open a console.
+ Navigate to where you extracted the lab files.
+ Start the GISC 425 environment within
      conda activate 425
+ Run Jupyter Lab by typing
      jupyter lab
