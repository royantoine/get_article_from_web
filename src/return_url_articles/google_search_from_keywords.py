from google import google


def return_filtered_articles_url(list_keywords, num_page, list_newspaper_website):
    """return link of newspaper related to a given google request"""
    if isinstance(list_keywords, str):
        list_keywords = [list_keywords]
    dic_google_search_filtered = {}
    for keywords in list_keywords:
        list_search_results = google.search(keywords, num_page)
        for search in list_search_results:
            if (search.link is not None) \
                    and any(newspaper_website in search.link for newspaper_website in list_newspaper_website):
                dic_google_search_filtered[search.link] = {
                    'link': search.link,
                    'google_search_title': search.name,
                    'google_search_description': search.description
                }
    return dic_google_search_filtered
