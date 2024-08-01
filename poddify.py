import requests
from solid.auth import Auth
from solid.solid_api import SolidAPI

api = SolidAPI()
POD_Provider = "https://solidcommunity.net/"
POD_ENDPOINT = "https://restaurierungsvokabular.solidweb.org/" # Pod to demostrate. Replace it with yours.
folder_name = 'wuerste/' 
folder_path = POD_ENDPOINT+folder_name
file_name = "krakauer.ttl"
file_path = POD_ENDPOINT+folder_name+file_name

data = "<http://example.org/krakauer> <http://example.org/a> <http://example.org/wurst> ."
data2 = "<http://example.org/lyoner> <http://example.org/a> <http://example.org/wurst> ."
data3 = "<http://example.org/thueringer> <http://example.org/a> <http://example.org/wurst> ."

username = "restaurierungsvokabular"
password = "hPYf!HCE6pz8ys"

#print(api.put_file(file_path, data, 'text/turtle'))
#print(api.post(file_path, data, 'text/turtle'))
#print(requests.get(file_path).text)

auth = Auth()
api = SolidAPI(auth)
auth.login("https://solidcommunity.net/","restaurierungsvokabular", "87M!i#xQo#&5@r")
if not api.item_exists(folder_path):
    print("YES")
    print(api.create_folder(folder_path))
    print(api.put_file(file_path, data2, 'text/ttl'))

# https://restaurierungsvokabular.solidweb.org/wuerste/krakauer.ttl