import pandas
import re
import gzip
import requests

class Downloader:
    def download_full_csv(language, n, alphabet):
        try:
            url = "http://storage.googleapis.com/books/ngrams/books/googlebooks-"+language+"-all-"+n+"gram-20120701-"+alphabet+".gz"
            pattern = re.compile('([a-zA-Z_]+)\t(\d{4})\t(\d+)\t(\d+)')
            fileName = language + '-' + alphabet + '.csv'
            response = requests.get(url)
            content = gzip.decompress(response.content)
            content = content.decode("utf-8") 
            wordList = content.split("\n")
            with open(fileName, "a") as f_out:
                f_out.write("word, year, match_count, volume_count\n")
                for line in wordList:
                    matcher = pattern.match(line)
                    if(matcher):
                        f_out.write(matcher.group(1)
                        +','
                        +matcher.group(2)
                        +','
                        +matcher.group(3)
                        +','
                        +matcher.group(4)
                        +'\n') 
        except:
            print("Error while downloading file")
        
    def download_match_count_csv(language, n, alphabet):
        try:
            url = "http://storage.googleapis.com/books/ngrams/books/googlebooks-"+language+"-all-"+n+"gram-20120701-"+alphabet+".gz"
            pattern = re.compile('([a-zA-Z_]+)\t(\d{4})\t(\d+)\t(\d+)')
            fileName = language + '-' + alphabet + '.csv'
            dic = {}
            i = 0
            response = requests.get(url)
            content = gzip.decompress(response.content)
            content = content.decode("utf-8") 
            wordList = content.split("\n")
            for entry in wordList:
                matcher = pattern.match(entry)
                if(matcher):
                    dic[i] = {'word' : matcher.group(1), 'count' : matcher.group(3)}
                    i = i+1
            df = pandas.DataFrame.from_dict(dic, "index")
            df['count'] = df['count'].astype('int64')
            df = df.groupby(['word'])['count'].sum().reset_index()
            df.to_csv(fileName, index = None)
        except:
            print("Error while downloading file")