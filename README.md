# get_article_from_web
This project aims at collecting all articles related to a given topic, given a pre defined list of newspaper/magazines.

The algorithm makes a Google search based on the keywords provided in `list_keywords` in `main.py`. It selects the first pages of the search (`num_page` in `main.py`). 

It keeps results of the search if url is hosted on a specific website provided in a text file in config (name of the file containing the list of all newspaper names must be provided in `name_file_list_newspaper` in `main.py`). 

Then, using the library `newspaper3k`, it extracts the content of the selected article and export it to a file in the folder provided in `main.py` (`output_path`).

To run the code, you have to:
- write the list of the newspaper you want to extract article from and move it to `config`
- specify all required field in `main.py`
- install `requirements.txt`
- run `main.py` with Python >= 3.6
