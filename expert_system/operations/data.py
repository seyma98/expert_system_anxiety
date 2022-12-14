import json

with open('static/jsonFiles/questions.json') as f:
  veri = json.load(f)
  


def takeQuestions():  
    rule_no=1
    target_no=0
    theList = list()
    for i in veri["target"][target_no]["rules"]:
        theList.append(veri["target"][target_no]["rules"][str(rule_no)])#veri["target"][0]["rules"][str(i+1)]
        rule_no+=1

    return theList

# function to add to JSON
def write_json(new_data, filename="static/jsonFiles/knowledge.json"):  
     with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["target"].append(new_data)

        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 7)

def write_question_json(filename="static/jsonFiles/questions.json"):  
     with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details

        file_data["target"][0]["rules"]["46"] = "46"


        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)




