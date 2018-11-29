from config.headers import headers
import requests


def return_info_url(url):
    r = requests.head(url, headers=headers)
    print(r.headers)

return_info_url('https://www.sciencesetavenir.fr/sante/grossesse/grossesse-tardive-quels-sont-les-risques_30126')