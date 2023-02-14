#! /usr/bin/python3

import os
import requests
import json

#These variables will be used within the larger for loop
path = "./review_files"
review_txt_files = os.listdir(path)
final_dict = []

for file in review_txt_files:
        count = 0 #Used to iterate over temp_list of file contents
        inputPath = os.path.join(path, file)
        temp_list = []
        dict_list = {"title":"","name":"","date":"","feedback":""}
        with open(inputPath) as review_info:
                for line in review_info:
                        string = line.strip() #Gets rid of new line symbol.
                        temp_list.append(string) #Creates list version of file contents
                for key in dict_list:
                        dict_list[key] = temp_list[count]
                        count = count + 1
                final_dict.append(dict_list)

print(final_dict)

with open("final_dict.json", "w") as feedback_json:
        feedback = json.dump(final_dict, feedback_json, indent=2)

response = requests.post("http://35.193.51.56/feedback", data=feedback)
print(response.status_code)
