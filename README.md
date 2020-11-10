# highlighter
project A-List or Highlighter repo

## Environment
Vlad wrote a pretty great summary to pyenv + pipenv working on a mac.
https://github.com/ideo/softserve/blob/master/Python.md

### python settings
for this project my python is set to: Python 3.7.4, but we could set it up to something else pretty easily too right now with minimal headache.

### the Pipenv "Virtual Environment"
so pipenv isolates your project so you can keep package versions consistent and working with collaborators. (and with your future self who can't remember where the origional code was and wants to get it running from github).

to init type: `pipenv install`
and as long as the python environment

### in case of emergency
delete the .venv file that contains all the python packages associated with this project, reset the python environment so it lines up with the version you want, and use `pipenv install` to try again.

## Organization

right now there's two directories:

- `/notebooks` which is for jupyter notebooks
- `/src` which is for python code files

To create symlinks to:
- `/1_data` for odds and ends
- `/2_plots` for figs

open the create_symlink script, change the value of the `datadir` variable and then run the script from the command line using `bash create_symlinks`.

check if it worked by looking into one of the symlinks to see if if finds anything `ls 1_data`

If you need to redo the process, delete the existing failed symlinks manually and try again.

### Don't we have a google drive?

For presentations, writing things, and spreadsheets. It's probably gotten better by now, but i always found reading/writing to and from google drive to be finniky.


## Notebooks

once you've got everything install, then just start a notebook server by typing: `pipenv run jupyter notebook`

or go into the `pipenv shell` and then type `jupyter notebook`

Once you've explored enough with notebooks then it get's turned into functions and moved into .py files in `/src`.


## Potential Datasets

https://www.english-corpora.org/now/

The bloomberg youtube channel + automatic transcript extraction.
I haven't tried this one but it looks promising: https://pypi.org/project/youtube-transcript-api/

...maybe there are some other youtube channels we could scrape?