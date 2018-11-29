from src.custom_classes.def_class_article import ArticleFromSearch
from google import google


def return_articles(list_keywords, num_page, list_newspaper_website):
    """return link of newspaper related to a given google request"""
    if isinstance(list_keywords, str):
        list_keywords = [list_keywords]
    dic_google_search_filtered = {}
    for keywords in list_keywords:
        list_search_results = google.search(keywords, num_page)
        for search in list_search_results:
            if (search.link is not None) \
                    and any(newspaper_website in search.link for newspaper_website in list_newspaper_website):
                article = ArticleFromSearch(
                    link=search.link,
                    google_search_title=search.name,
                    google_search_description=search.description
                )
                try:
                    article.extract_article_from_link('fr')
                except BaseException as e:
                    print('link: %s not working with error %s' % (search.link, e))
                dic_google_search_filtered[search.link] = article.concatenate_output()
    return dic_google_search_filtered
