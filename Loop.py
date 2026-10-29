i = 3
while i != 0:
    print("meow")
    i = i - 1



for i in range(3):
    print("meow")




print("meow\n" * 3, end="")






student = ["hermione", "harry", "ron", "draco"]

houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]





student2 = [
    {"name": "hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "ron", "house": "Gryffindor", "patronus": "rat"},
    {"name": "draco", "house": "Slytherin", "patronus": "serpent"}
]
for student in student2:
    print(student["name"], student["house"], student["patronus"])




def main 