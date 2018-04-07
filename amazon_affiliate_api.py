def find_asin(title='Around the World in Eighty Days',author='Jules Verne'):
    """Find the unique ASIN identifier for the book
		INPUT: Book title and author
		FUNCTION: find_asin()
		OUTPUT: The unique asin identifier
        Time taken: < 1 second"""
    
    from amazonproduct import API
    api = API(locale='uk')
    items = api.item_search('Books', Title=title, Author=author)
    # Take the first result
    for book in items:
        break
    asin = str(book.ASIN)
    
    return(asin)