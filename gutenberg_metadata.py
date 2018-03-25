def scrape():
    """Got through the metadata for Gutenburg books and get the author, title for each file.
		INPUT: The rdf files downloaded from Gutenberg containing the metadata
		FUNCTION: scrape()
		OUTPUT: A dictionary containing the filename as key and author,title in a list.
        Time taken: 5h 31min 38s"""
    #%%
    from cPickle import dump
    from bs4 import BeautifulSoup
    from string import punctuation
    import subprocess
    from glob import glob
    
    catalogue = {}
    items = glob('metadata/*/*.rdf')
    for item in items:
        submit_name = "sed 's/:/_/g' " + item + " > metadata/temp.txt"
        subprocess.call([submit_name], shell=True)
        
        f = open("metadata/temp.txt", 'r')
        soup = BeautifulSoup(f, "lxml")
        f.close()
        
        # Only get it if the language is English
        lang = True
        if soup.body.dcterms_language.rdf_value != None:
            if soup.body.dcterms_language.rdf_value.contents[0] != 'en':
                lang = False
        elif soup.body.dcterms_languag != None:
            if soup.body.dcterms_language.contents[0] != 'en':
                lang = False
        else:
            lang = False
            
        if lang:
            if soup.dcterms_creator != None:
                save = True
                title = soup.dcterms_title.contents[0]
                title = title.replace('\r\n', ' ')
                title = title.replace('\n', ' ')
                titlefile = str(title.encode('ascii', 'ignore').decode('ascii'))
                titlefile = titlefile.translate(None, punctuation)
                titlefile = titlefile.replace(' ', '_')
            
                if soup.dcterms_creator.pgterms_agent != None:
                    author = soup.dcterms_creator.pgterms_agent.pgterms_name.contents[0]
                elif soup.pgterms_agent != None:
                    author = soup.pgterms_agent.pgterms_name.contents[0]
                else:
                    save = False
                author = author.replace('\r\n', ' ')
                author = author.replace('\n', ' ')
                authorfile = str(author.encode('ascii', 'ignore').decode('ascii'))
                authorfile = authorfile.translate(None, punctuation)
                authorfile = authorfile.replace(' ', '_')
                temp = author.split(', ')
                if len(temp) == 2:
                    author = temp[1] + ' ' + temp[0]
                
            
        
                temp = str(soup.pgterms_ebook['rdf_about'])
                temp = temp.split('/')
                zipfile = temp[-1]
            
                if save:
                    catalogue[zipfile] = [author,title] # ,authorfile,titlefile
        
        submit_name = "rm metadata/temp.txt"
        subprocess.call([submit_name], shell=True)
        
    return(catalogue)