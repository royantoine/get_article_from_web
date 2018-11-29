from newspaper import Article
import nltk
nltk.download('punkt')


class ArticleFromSearch:
    def __init__(self, link, google_search_title, google_search_description):
        self.link = link
        self.google_search_title = google_search_title
        self.google_search_description = google_search_description
        self.authors = ''
        self.publish_date = ''
        self.text = ''
        self.keywords = ''
        self.summary = ''

    def extract_article_from_link(self, language):
        article = Article(self.link, language=language)
        article.download()
        article.parse()
        self.authors = article.authors
        self.publish_date = article.publish_date
        self.text = article.text
        article.nlp()
        self.keywords = article.keywords
        self.summary = article.summary

    def concatenate_output(self):
        output = {
            'link': self.link,
            'google_search_title': self.google_search_title,
            'google_search_description': self.google_search_description,
            'authors': self.authors,
            'publish_date': self.publish_date,
            'text': self.text,
            'keywords': self.keywords,
            'summary': self.summary
        }
        return output
