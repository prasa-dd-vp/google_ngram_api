# Google Ngram API
This API lets you download the Ngram dataset (Version 20120701) with specified condition from google as a CSV file.  

## Overview
Google Ngram dataset exists in the following structure:
```
ngram TAB year TAB match_count TAB volume_count NEWLINE
```
where,
- ngram represents the word(s)
- year represents the year
- match_count represents the overall count
- volume_count represents the count in distinct books

Example,
```
circumvallate   1978   335    91
```
It states that, in 1978, the word "circumvallate" occurred 335 times overall, in 91 distinct books of our sample.

## Usage
The following paragram explains the usuage of this package

### Getting it
To download this package use the following command
```sh
pip install google_ngram_api
```
### Using it
This package has a single class **Downloader** and two functions __download_full_csv__ and __download_match_count_csv__.
The method __download_full_csv__ enables you to download the complete dataset as csv whereas the function __download_match_count_csv__ enables you to download match_count (overall count) data alone. 
Each method takes in three parameters:
#### 1. language 
The language code for the following languages are:
- English - eng
- English one million - eng-1M
- American English - eng-us
- British English - eng-gb
- English Fiction - eng-fiction
- Chinese(Simplified) - chi-sim
- French - fre
- German - ger
- Hebrew - heb
- Italian - ita
- Russin - rus
- Spanish - spa
#### 2. n
n represents the 'N' in Ngrams. Possible numbers are 1,2,3,4 and 5. 
#### 3. alphabet
alphabet represents the ngram dataset associated with that alphabet.
### License
MIT License
Copyright (c) 2018 Venkatesh Prasad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
