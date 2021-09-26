import json

lst=["add","search","list","exit"]

with open('birthday.json', "r") as dicti:
    dictionar = json.load(dicti)

def list():
        for position,(a,b) in enumerate(dictionar.items()):
            print(position+1,"-",a,b)

def add():
    friend_name = str(input("Type name of the friend who you want to add: "))
    friend_date = str(input("Type date of birth: "))
    dictionar[friend_name] = friend_date
    with open('birthday.json',"w") as dicti:
        json.dump(dictionar,dicti)
    print(friend_name, "added sucessfully")

def search():
    search_name = str(input("Type name of the friend who you want to find out the birthdate?"))
    if search_name in dictionar:
        print(search_name, dictionar[search_name])
    else:
        print("Incorrect name")

while True:
    user_answer=str(input("To add a birthday type: add. To search a birthday type: search. To see entire list type: list. For exit type: exit.\nType here your answer:"))
    if user_answer not in lst:
        print("Wrong answer!")
    elif user_answer =="add":
        add()
    elif user_answer =="search":
        search()
    elif user_answer =="list" :
        list()
    elif user_answer=="exit" :
        break
