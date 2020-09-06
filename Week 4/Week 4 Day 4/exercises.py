#ex1
# def display_message():
#     print("we are learning about functions")
# display_message()
# ex2
# def favorite_book(title):
#     print(f"my favorite book is {title}!")
# favorite_book("Harry Potter")
# # ex3
# def make_shirt(size="Large", text="I love Python"):
#     print(f"This shirt is a size {size} and says {text}.")
# make_shirt("large", "just do it")
# make_shirt(size="medium", text="ya never know")
# make_shirt()
# make_shirt("medium")
# make_shirt(text="Hello World")
# # ex4
# def show_magicians(list_of_magicians):
#     for i in range(len(list_of_magicians)):
#         list_of_magicians[i] = list_of_magicians[i] + " the great"
#     print(list_of_magicians)
# show_magicians(["michael", "shlomo"])

# # ex5
# def describe_city(city, country="Germany"):
#     print(f"{city} is a city in {country}.")
# describe_city("Berlin")
# describe_city("Munich")
# describe_city("Baltimore", "United States")
# describe_city("Haarlem", "Holland")
# # ex6
def get_age(year, month, day):
    cur_year = 2020
    cur_month = 9
    cur_day = 2
    if (cur_day - day) >= 0:
        if (cur_month - month) >= 0:
            return (cur_year - year)
        else:
            return (cur_year - year -1)
    elif (cur_month - month) >= 1:
        return (cur_year - year)
    else: 
        return (cur_year - year -1)  
print(get_age(1997, 9, 22))
print(get_age(1997, 10, 1))
print(get_age(1997, 8, 3))
def can_retire(gender, date_of_birth):
    if gender == "male":
        if get_age(*date_of_birth) >= 67:
            print('you can retire')
        else:
            print('keep at it young man!')
    elif gender == "female":
        if get_age(*date_of_birth) >= 62:
            print("you can retire")
        else:
            print("keep at it young lady!")
can_retire("male", [1953, 9, 1])

# ex7
users = []
for i in range(3):
    diction = {
        "name": 'larry', 
        "address": '1234 main street', 
        "langage_spoken": 'esperabicish'
    }
    users.append(diction)
print(users)


        