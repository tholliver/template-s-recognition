import json
import os

# print(f'The file parent: {os.path.abspath(os.curdir)}')
# Ruta a los templates
templatePath = '../templates/audios'
templateDB = "../templates/templates.json"
# fullPath = os.path.abspath(os.curdir)+templatePath
# print(f'The file parent: {fullPath}')
# Data to be written
templateModel = {
    "ruta": "",
    "palabra": "",
    "specTemplate": []
}

filelist = []

# list file and directories
res = os.listdir(templatePath)
print(res)


# # Serializing json
# json_object = json.dumps(templateModel, indent=4)

# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)
