# Quotes to Scrape using Beautifulsoup


## Info

Using Python3+ and BeautifulSoup to scrape (http://quotes.toscrape.com/). 

## Requirements

* Python3+
* BeautifulSoup

## Usage
```python
>>> _Quotes = Quotes()
>>> data_dict_res = _Quotes.get_data()
>>> print(data_dict_res)
{'status': 200, 'data': {0: {'qoute_text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'quote_author': <small class="author" itemprop="author">Albert Einstein</small>, 'quote_tags': ['change', 'deep-thoughts', 'thinking', 'world']}, 1: {'qoute_text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'quote_author': <small class="author" itemprop="author">J.K. Rowling</small>, 'quote_tags': ['abilities', 'choices']}, 2: {'qoute_text': '“There are only two
ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'quote_author': <small class="author" itemprop="author">Albert Einstein</small>, 'quote_tags': ['inspirational', 'life', 'live', 'miracle', 'miracles']}, 3: {'qoute_text': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'quote_author': <small class="author" itemprop="author">Jane Austen</small>, 'quote_tags': ['aliteracy', 'books', 'classic', 'humor']}, 4: {'qoute_text': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'quote_author': <small class="author" itemprop="author">Marilyn Monroe</small>, 'quote_tags': ['be-yourself', 'inspirational']}, 5: {'qoute_text': '“Try not to become a man of success. Rather become a man of value.”', 'quote_author': <small class="author" itemprop="author">Albert Einstein</small>, 'quote_tags': ['adulthood', 'success', 'value']}, 6: {'qoute_text': '“It is better to be hated for what you are than to be loved for what you are not.”', 'quote_author': <small class="author" itemprop="author">André Gide</small>, 'quote_tags': ['life', 'love']}, 7: {'qoute_text': "“I have not failed. I've just found 10,000 ways that won't work.”", 'quote_author': <small class="author" itemprop="author">Thomas A. Edison</small>, 'quote_tags': ['edison', 'failure', 'inspirational', 'paraphrased']}, 8: {'qoute_text': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'quote_author': <small class="author" itemprop="author">Eleanor Roosevelt</small>, 'quote_tags': ['misattributed-eleanor-roosevelt']}, 9: {'qoute_text': '“A day without sunshine is like, you know, night.”', 'quote_author': <small class="author" itemprop="author">Steve Martin</small>, 'quote_tags': ['humor', 'obvious', 'simile']}}}
```
