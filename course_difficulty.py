# have each homework assignment be ranked based on difficulty of the course and on difficulty of the assignment itself
# list_of_courses_and_difficulty only takes into consideration the difficulty of the course, not the assingment

# --------------------------------------------- #
# Hey Koki, this is super cool. I love making CLI interfaces, there's a ton you can do in Python
# There are a bunch of cool libraries such as blessed, curses, and more that allow you to do insane stuff.
# Just take a look at https://pypi.org/project/blessed/, the possibilities are endless!
# --------------------------------------------- #

from array import *

def set_courses_and_difficulties():
    value_c = input("Please enter the names of all your courses with spaces in between each course name:\n")

    def get_courses():
    # sets everything to upper case and removes surrounding whitespace, makes sure there is only one space between course names
        courses = value_c.strip().upper()
        return courses

    format_courses = get_courses()
    # --------------------------------------------- #
    # The \u... stuff is an ANSI color code.
    # You can find a bunch more https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#256-colors
    # If you don't like it of course feel free to remove, all up to you :)
    # --------------------------------------------- #
    value_d = input(u"\u001b[38;5;133m " + f"""
===========================================================================
Please enter the difficulty of each course in the same order with spaces in between each ranking.
The levels of difficulty are as following:
    1 = Easy and quick
    2 = Easy but time-consuming
    3 = Medium
    4 = Hard material, quick work
    5 = Hard, tedious, and time-consuming

Reminder, your courses are: {format_courses}
===========================================================================\u001b[0m""") # Changed to triple string :)

    def get_difficulties():
        difficulties = value_d.strip()
        return difficulties

    def string_to_array(s):
    # defines a method that creates an array of strings, the strings consist of the content in between each spaces
        return s.split(" ")

    list_courses = string_to_array(get_courses())

    list_difficulties = string_to_array(get_difficulties())

    num_courses = len(list_courses)
    # interger that represents the length of the courses array, isn't used as of now but is here in case you need it later

    print(f'\nYour course list:\n{list_courses}\nTheir corresponding difficulties:\n{list_difficulties}')


def coursecheck():
    #checks that the courses the user entered are in line with what they want

    check = input("Please check that these are the courses you're taking.\n") # Added in line break
    if check.lower() == 'yes':
        print(f'\nYay! You are ready to move on.')
    elif check.lower() == 'no':
        set_courses_and_difficulties()
    else:
        print(f'\nError. Please retry.')
        coursecheck()

coursecheck() # I would possibly remove this, since it's a bit confusing to start off with

if __name__ == "__main__":
    set_courses_and_difficulties()
