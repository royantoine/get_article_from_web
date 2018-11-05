from src.return_url_articles.google_search_from_keywords import return_filtered_articles_url
from src.utils.load_config import return_list_newspaper_website

name_file_list_newspaper = 'list_website_newspaper.csv'
list_keywords = ["grossesse tardive", "paternité tardive"]
num_page = 50

list_newspaper_website = return_list_newspaper_website(name_file_list_newspaper)
dic_google_search_filtered = return_filtered_articles_url(list_keywords, num_page, list_newspaper_website)
print(len(dic_google_search_filtered))