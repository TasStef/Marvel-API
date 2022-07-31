# Marvel_API_Characters

## Tasso Stefanidis 30-Jul-2022

### -----Description-----
This projects creates 3 json files. The first file (All_Characters.json) can be ignored as it is just being used internally by the app. The second file, Characters_ID.json, contains the IDs of all the characters of the Marvel APi. The last file, Characters_Info.json, contains the <id, name, description, modified, thumbnail> for all characters.
In order to use this you will be prompted to give a Public and a Private Key, which can be generated at https://developer.marvel.com/account after you sign in to your account.


### -----Run-----
just run the main.exe (only executable in folder). This will generate the json files.


### -----Contributing----
https://github.com/TasStef/Marvel-API


### -----Json Files-----
-All_Characters.json: Contains all the information for all the characters, from the API

-Characters_ID.json: Contains all the IDs of the characters in the API

-Characters_Info.json: Contains spesific information for all the characters in API. for each character: id, name, description, modified and thumbnail.


### -----Exe Files-----
main.exe: the main.py executable. Will run all the necesary py files (listed below in "Python Files" section) in order to create the json files that are listed in the "Json Files" cataegory.


### -----Python Files-----
-main.py: 

-Methods.py: container of methods to be used towards the project between different apps

-Tokens.py: container, holds the Private and Public tokens form my Marvel API account, in order to access the API

-Creating_All_Characters.py: Creates the All_Characters.json file that holds all the information for all the characters in the API's database

-Characters_ID.py: Takes the IDs from the All_Characters.json and writes them in to the Characters_ID.json

-Info.py: Creates the Characters_Info.json, with the filter information of id, name, description, modified and thumbnail, for each character. Info.py uses the character{id} module of the Marvel API which will take only on input at a time. This means that there will be 1562 (current number of characters in the API) requests.


### -----Contact-----
9004757@gmail.com
