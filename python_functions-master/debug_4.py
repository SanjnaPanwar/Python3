# def greet(names):
#     for name in names:
#         print("Welcome", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")

def greet(*names):
    for name in names:
        print("Welcome", name)
greet("Rinki", "Vishal", "Kartik", "Bijender")