import nltk
nltk.download()
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

text = """I’ve been asked by a few friends to develop a feature for a
WhatsApp chatbot of mine, that summarizes articles based on
URL inputs. So when a friend sends an article to a WhatsApp
group, the bot will reply with a summary of the given URL
article. I like this feature because from my personal
research, 65% of group users don’t even click the shared URLs,
but 97% of them will read a few lines of the articles summary.
As part of being a Fullstack developer, it is important to
know how to choose the right stack for each product you
develop, depending on the requirements and limitations.
For web crawling, I love using Python. The Python community
is filled with efficient, easy to implement open source
libraries both for web crawling and text summarization.
Once you’re done with this tutorial, you won’t believe how
simple it is to implement the task."""

word = word_tokenize(text)