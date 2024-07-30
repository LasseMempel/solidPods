import requests
from solid.auth import Auth
from solid.solid_api import SolidAPI

api = SolidAPI()
POD_ENDPOINT = "https://restaurierungsvokabular.solidweb.org/" # Pod to demostrate. Replace it with yours.
folder_name = 'wuerste' 
file_name = "krakauer.ttl"

data = "<http://example.org/krakauer> <http://example.org/a> <http://example.org/wurst> ."
print(api.item_exists(POD_ENDPOINT+folder_name+"/"))
print(api.put_file(POD_ENDPOINT+folder_name+"/"+file_name, data, 'text/turtle'))
# add a new tripe to file
data = "<http://example.org/lyoner> <http://example.org/a> <http://example.org/wurst> ."
print(api.put_file(POD_ENDPOINT+folder_name+"/"+file_name, requests.get(POD_ENDPOINT+folder_name+"/"+file_name).text + data, 'text/turtle'))
data = "<http://example.org/thueringer> <http://example.org/a> <http://example.org/wurst> ."
print(api.post_item(POD_ENDPOINT+folder_name+"/", "newfile.ttl", data, 'text/turtle'))


# https://restaurierungsvokabular.solidweb.org/wuerste/krakauer.ttl