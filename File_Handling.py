import os
import shutil
import csv


'''f = "/Users/egehankoyuncu/Desktop/deneme1/demofile.txt"


with open(f,"r") as my_file:
    r = my_file.read()

    print(r)

f = "/Users/egehankoyuncu/Desktop/deneme1/demofile.txt"


with open(f,"r+") as my_file:
    my_file.write("\tbananaSA")
    content = my_file.read()
print(content)




else:

print(os.path.exists("/Users/egehankoyuncu/Desktop/amam.docx"))

    with open("demofile.txt", "x") as deneme:
       deneme.write("anan")
    
    with open("demofile.txt", "r") as myfile:
        content = myfile.read()
        print(content)

     


os.mkdir("/Users/egehankoyuncu/Desktop/silinecek folder")


if os.path.exists("Users/egehankoyuncu/Desktop/teoman"):
    print("ajhsj")
    shutil.rmtree("Users/egehankoyuncu/Desktop/teoman")

else:
    print("yok")
    shutil.rmtree("Users/egehankoyuncu/Desktop/teoman")
    os.mkdir("/Users/egehankoyuncu/Desktop/teoman")
with open("/Users/egehankoyuncu/Desktop/teoman/teoman.txt", "x") as oguzhan:
    a = "babaanne"
    oguzhan.write(a)
with open("/Users/egehankoyuncu/Desktop/teoman/egehan.txt", "x")as demirhan:
    b= "anneanne"
    demirhan.write(b)

z = input("Enter the path of your directory: ")
if os.path.exists(z):
    shutil.rmtree(z)
else:
    print("No such directory exists")


file_path = "/Users/egehankoyuncu/Downloads/annual-enterprise-survey-2021-financial-year-provisional-csv.csv"

with open (file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in file:
        if row == "2010":
            print(row)

a = "1"
a= float(a)
print(type(a))

def question (name, age):
    question = []
    
    if os.path.exists("data.csv"):
        with open("data.csv", "r") as my_file:
            csv_reader = csv.reader(my_file)
            for i in csv_reader: '''