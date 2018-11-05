from src.utils.paths import PROJECT_PATH
import csv, os


def return_list_newspaper_website(name_file_list_newspaper):
    with open(os.path.join(PROJECT_PATH, 'config', name_file_list_newspaper), 'r') as f:
        list_newspaper_website_raw = list(csv.reader(f))
    list_newspaper_website = []
    for newspaper_website in list_newspaper_website_raw:
        cleaned_name = newspaper_website[0].lower()
        list_newspaper_website.append(cleaned_name)
    return list_newspaper_website
