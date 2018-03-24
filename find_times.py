## Spark Application - execute with spark-submit

## Imports
from pyspark import SparkConf, SparkContext

## Module Constants
APP_NAME = "My Spark Application"

## Closure Functions

## Main functionality

def main(sc):
    """Get information about when the samples were sequenced.
		INPUT: The times to search for in a list. The folders containing the books, also in a list.
		FUNCTION: main()
		OUTPUT: Around 10 seconds per book for an obscure time."""
    
    from get_times import get_times
    times_to_get = ['04:25', '11:29']
    to_lookup = {}
    all_times = []
    for time in times_to_get:
        some_times = get_times(time)
        for item in some_times:
            to_lookup[item] = time
        all_times = all_times + some_times
            
    import time
    start_time = time.time()
    with open('time_results.tsv', 'wb') as f:
        for i in ['books/']:
            lines = sc.wholeTextFiles(str(i) + '/*.txt')
            print i, (time.time() - start_time)
            noon = lines.filter(lambda a: any(x in a[1] for x in all_times))
            a = noon.collectAsMap()
            for key in a:
                uemp = str(key)
                temp = uemp.split('/')
                semp = temp[-1].split('.txt')
                remp = semp[0].split(' - ')
                pemp = remp[-1].split('[')
                oemp = pemp[0].split('(')
                title = oemp[0]
                if ',' in remp[-1]:
                    qemp = remp[0].split(', ')
                    author = qemp[-1] + ' ' + qemp[0]
                else:
                    author = remp[0]
                to_parallel = a[key]
                sentences = sc.parallelize(to_parallel.split('. '))
                midday = sentences.filter(lambda a: any(x in a for x in all_times))
                for sentence in midday.collect():
                    new_sentence = sentence.replace('\r\n', ' ')
                    new_sentence = new_sentence.replace('\n', ' ')
                    new_sentence = new_sentence.replace('\t', ' ')
                    contained = [x for x in all_times if x in new_sentence]
                    new_title = title.replace('_', ':')
                    new_author = author.replace('_', '.')
                    f.write(to_lookup[contained[0]] + '\t' + new_sentence.encode('utf8') + '.\t' + new_title + '\t' + new_author + '\n')
                to_parallel = []


if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)

    # Execute Main functionality
    main(sc)