def convert(type='books/*.mobi'):
    """Convert books in the current directory using Calibre command line function.
		INPUT: The format of books to convert in the current directory.
		FUNCTION: convert(type)
		OUTPUT: All the books of that type converted to txt files.
        Time taken: < 1 minute per mobi file (< 10 MB), longer for pdfs."""
    
    from glob import glob
    from os import remove
    import subprocess
    import time
    start_time = time.time()
    
    ebooks = glob(type)
    
    for n,item in enumerate(ebooks):
        temp = item.split('.')
        if temp[-1] != 'txt':
            submit_name = '/Applications/calibre.app/Contents/console.app/Contents/MacOS/./ebook-convert "'+ item + '" "' + temp[0] + '.txt"'
            subprocess.call([submit_name], shell=True)
            # remove(item) # Uncomment if you want to remove the original book format after conversion
            print n, (time.time() - start_time)