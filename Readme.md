## Literary clock code

### Requirements:
Calibre version 2.85.1 - Downloadable from [here](https://calibre-ebook.com/download) - needed to convert the ebooks to text file.

Python 2.7 - I have [Anaconda Python 2.7 version](https://www.anaconda.com/download/) installed.

Spark 2.20 - Can be downloaded from [Apache](https://www.apache.org/dyn/closer.lua/spark/spark-2.2.0/spark-2.2.0-bin-hadoop2.7.tgz).

### Description
#### Code 
Code that helped build the literary clock, further explanation can be found at [www.literaryclock.com](http://www.literaryclock.com/posts/).

&nbsp;

	convert_books_wrapper.py
This is a wrapper around the Calibre command line tools to convert ebooks to txt files. Detailed documentation for the calibre command line tools can be found [here](https://manual.calibre-ebook.com/generated/en/ebook-convert.html).

&nbsp;

	get_times.py
`find_times.py` calls the `get_times` function, which converts digital times of the form 11:29 to many different ways that it could be transcribed in a book:

<sub>
'11:29', '11.29', '1129', 'twenty-nine past eleven', 'twenty-nine minutes past eleven', '29 minutes past eleven', '29 past eleven', 'twenty-nine after eleven', 'twenty-nine minutes after eleven', '29 minutes after eleven', '29 after eleven', 'twenty-nine past 11', 'twenty-nine minutes past 11', '29 minutes past 11', '29 past 11', 'twenty-nine after 11', 'twenty-nine minutes after 11', '29 minutes after 11', '29 after 11', 'eleven twenty-nine', 'eleven-twenty-nine', '1 twenty-nine', '1-twenty-nine'
</sub>

&nbsp;

In this file is also the `digit2word` function which turns numbers from 0 to 59 into words, which is needed in the `get_times` function.
Possible improvement for this function is also to have capitalised times. 

&nbsp;

	find_times.py
This needs to run using the PySpark API. I must confess I could not get this to work as a stand alone file. Instead I removed the indentation of the main function code and ran it in the `$SPARK/bin/./pyspark` command line. If the folder containing the books returns times greater than the memory available this will crash. Hence I try divide the books between many folders and run the code iteratively for each folder. The code expects the file name to be of the form `author - book_title.txt`. If it part of series, I have also added code to deal with `author - book_title (3rd Series Title)` - basically all I want from the filename is the author and book title (and it expects them in that order separated by ` - `). The output in the tab separated file (time_results.tsv) will not be in any necessary order and may contain many false positives.

&nbsp;

	gutenberg_metadata.py
Having downloaded ~ 50,000 ebooks from [Project Gutenberg](https://www.gutenberg.org/) as discussed in [this post](http://www.literaryclock.com/posts/Lt3_50000_Books), this is some nifty code so we can link the filenames downloaded with the author and title of the books they contain. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) (version 4.5.3) does the heavy lifting, with some hacks either side of it to get the author and title as plain strings. The results are returned as dictionary, with the filename as key and author and title in a list. I used these results to rename and move the 50,000 files into many folders to set `find_times.py` on.

&nbsp;

#### Data
In the books folder I have two books; a Sherlock Holmes Collection and Around the World in Eighty Days. These were downloaded from [Project Gutenberg](https://www.gutenberg.org) in mobi form and converted to text files using `convert_books_wrapper.py`.

#### Metadata
Here are two examples of the rdf files downloaded from [Project Gutenberg](https://www.gutenberg.org/wiki/Gutenberg:Feeds), covering the metadata of the two books described above.

#### Results
`time_results.tsv` contains the results of `find_times.py` run on the books above for the times 04:25 and 11:29. It can be opened as a spreadsheet for easier viewing.
