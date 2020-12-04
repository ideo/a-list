# A-List
project A-List or Highlighter repo

### Heres google drive for more background
[It's here](https://drive.google.com/drive/folders/1LrgbSD7kSUEJUjaxkUGJfXpDncFAhTl8?usp=sharing), it has the project brief. We use that for presentations, writing things, and spreadsheets.

## Environment
Vlad wrote a pretty great summary to pyenv + pipenv working on a mac.
https://github.com/ideo/softserve/blob/master/Python.md

### python settings
for this project my python is set to: Python 3.7.4

### the Pipenv "Virtual Environment"
so pipenv isolates your project so you can keep pa.ckage versions consistent and working with collaborators. (and with your future self who can't remember where the origional code was and wants to get it running from github).

to init type: `pipenv install`
and as long as the python environment

### in case of emergency
delete the .venv file that contains all the python packages associated with this project, reset the python environment so it lines up with the version you want, and use `pipenv install` to try again.

## Organization

right now there's two directories:

- `/notebooks` which is for jupyter notebooks
- `/src` which is for python code files

We store all the data for this project on [Dropbox](https://www.dropbox.com/sh/tnpmbi6y1gxcgt4/AAAtdR0MRXmPtVRqW4RSqbDma?dl=0) (PW: data).

Once you have access to it, set-up the folder access so that it's stored on your local computer and syncd to the cloud.

Then create symlinks to the key dropbox directories:
- `/1_data` for odds and ends
- `/2_plots` for figs

open the create_symlink script, change the value of the `datadir` variable and then run the script from the command line using `bash create_symlinks`.

check if it worked by looking into one of the symlinks to see if if finds anything `ls 1_data`

If you need to redo the process, delete the existing failed symlinks manually and try again.



## Notebooks

once you've got everything install, then just start a notebook server by typing: `pipenv run jupyter notebook`

or go into the `pipenv shell` and then type `jupyter notebook`

Once you've explored enough with notebooks then it get's turned into functions and moved into .py files in `/src`.

Most critical notebooks:
- **5_exploritory_ceos** - This has all the crunchbase data exploration and is used to create our BIG list of ceos to explore
- **8_injest_data** - This contains code for cleaning up all the raw data files and creating the combined `docs.db` sqlite3 database
- **9_nlp_on_injested** - This loads the database and runs most of the final analysis

The'res also a number of notebooks for scaping different data sources. They were never completely automated for repeated scraping, but ususally need a bit of manual TLC to get new data downloaded and set up to be injested into the DB.

## Datasets

### Core Datasets

**Crunchbase**: 
These csvs were created manually using a set of criterion that matched Kathy and Katrin's description of interesting targets. It's our source of The Big List of new places to look into.
An idea for future development is to use this data to provide more context on CEOs and organizations, but we haven't yet set up code to try and cross-reference it with the other sources since all the organization names are free text and will likely require a fair bit of data-munging efforts.

**Good Leads Articles**:
Kathy took a list of our current transformational clients and found 34 articles about those clients from 1 to 2 years before they started working with IDEO.
We downloaded the text by hand. This is the source of most of our analysis.

**NYT Corner Office**:
This is our reference for "how ceo's sound in interviews".
This was pretty tricky to scrape and an NYT membership is required. Although NYT indicates that 500+ of these articles were in the collection the online indexes only seemed to have links for 218. We downloaded the text for what we could.

**Earnings Call transcripts from Seeking Alpha**:
Scraped from seeking alpha. We used a trial membership to Seeking Alpha to get this sample of their much larger dataset. 500 transcripts were downloaded. 50,000 (?) or so were indexed. We decided to not scrape further, since they

**Current Transformational Clients**:
Like the good leads articles, these aricles are about current clients and were curated and downloaded by hand.

### Interesting but tangential data we aquired

**Now**:
https://www.english-corpora.org/now/
This provides a corpus that can easily scan many many online news articles, but doesn't actually let you download the full text, only surrounding words.
We invested a couple days in getting a scraping interface set up that can actually download the tables it creates.


**IDEO Journal**:
This is our reference for "what IDEO sounds like". It was used in one of our earlier directions but we shifted away from this direction because we increasingly focused on our "good leads" sample.
A proper index.csv file still needs to be created for this dataset, because it was last featured in our analysis before we settled on a standardized format.

### untapped data
These are areas that seem promising but haven't gotten around to looking into more.

The bloomberg youtube channel + automatic transcript extraction.
I haven't tried this one but it looks promising: https://pypi.org/project/youtube-transcript-api/

...maybe there are some other youtube channels we could scrape?
