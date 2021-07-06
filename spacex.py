from urllib.request import urlopen
import json
from pprint import pprint

url = 'https://api.spacexdata.com/v3/launches'
json_url = urlopen(json_url)
text = json.loads(json_url.read())
#pprint(text)
main_dic = {}
maind_dic['Mission Name'] = text[0][]