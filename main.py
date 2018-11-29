from src.return_articles.google_search_from_keywords import return_articles
from src.utils.load_config import return_list_newspaper_website
import json, os


name_file_list_newspaper = 'listepresse.csv'
list_keywords = ["grossesse tardive", "paternité tardive", "maternité tardive"]
num_page = 10
output_path = 'D:/7. Late parenthood/output_list_links'


def main():
    list_newspaper_website = return_list_newspaper_website(name_file_list_newspaper)
    dic_google_search_filtered = return_articles(list_keywords, num_page, list_newspaper_website)
    with open(os.path.join(output_path, 'result_list_articles.json'), 'w') as outfile:
        json.dump(dic_google_search_filtered, outfile, indent=4, sort_keys=True, default=str)
    print(len(dic_google_search_filtered))

if __name__ == '__main__':
    main()
