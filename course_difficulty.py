# Koki Kapoor
# CSC 630
# Course Difficulty.py file 


# have each homework assignment be ranked based on difficulty of the course and on difficulty of the assignment itself
# list_of_courses_and_difficulty only takes into consideration the difficulty of the course, not the assignment

from array import *
# install numpy in terminal with:
    


# dictionaries mapping difficulty level to their assigned descriptions 
# commented this out to redefine the course difficulty and workload separately
"""
difficulty_levels = {
    1:'Easy and quick',
    2:'Easy but time-consuming',
    3:'Medium',
    4:'Hard material, quick work',
    5:'Hard, tedious, and time-consuming'
}
"""


# difficulty_levels2 refers to the difficulty of the course's material, not how much time it takes
# ie, there can be a very time-consuming course that has easy material
difficulty_levels = {
    1:'Easy',
    2:'Easy-Medium',
    3:'Medium',
    4:'Medium-Hard',
    5:'Hard'
}

#dictionary mapping the amount of time taken on a course's workload (which includes studying, tests, etc) 
workload_levels = {
    1:'1-1.9 hours',
    2:'1.9-2.9 hours',
    3:'2.9-3.9 hours',
    4:'3.9-4.9 hours',
    5:'4.9-5.9 hours',
    6:'6+ hours'
}


def set_courses_and_difficulties():
# user input of course names
    value_c = input("Please enter the names of all your courses with spaces in between each course name\n")

    def get_courses():
    # sets everything to upper case and removes surrounding whitespace, makes sure there is only one space between course names
        courses = value_c.strip().upper() 
        return courses
    
    format_courses = get_courses()

    value_time = input("Please enter the amount of time (between 1 and 6 hours in whole numbers) that you spend completing work for each class every day.\n"
        "The hours are as following:\n"
        "\n".join([f'Level {level}: {timetaken_desc[level]}' for level in range(1,6)])+
        f"\n\nReminder, your courses are: {format_courses}\n"
    )
  
    

    value_diff = input('\nPlease enter the difficulty of each course in the same order with spaces in between each ranking.\n' +
    'The levels of difficulty are as following:\n' +
    '\n'.join([f'Level {level}: {difficulty_desc[level]}' for level in range(1,6)])+
    f'\n\nReminder, your courses are: {format_courses}\n')
    

    def read_level_input(input_value):
        input_vals = input_value.strip().split(' ') # strip whitespace from input value and split around spaces to create an array of strings
        levels = [int(x) for x in input_vals] # cast to int
        return levels
        

    def string_to_array(s):
    # defines a method that creates an array of strings, the strings consist of the content in between each spaces
        return s.split(" ") 

    list_courses = string_to_array(get_courses())
    list_timetaken = read_level_input(value_t)
    list_difficulties = read_level_input(value_d)


    # make a joint list
    course_info = dict()
    for i,course in enumerate(list_courses):
        course_info[course] = dict()
        course_info[course]['efficiency'] = list_timetaken[i]
        course_info[course]['difficulty'] = list_difficulties[i]
    print(course_info)

    # map course difficulty and time taken to a description
    list_difficulties_desc = [difficulty_desc[diff] for diff in list_difficulties]
    list_timetaken_desc = [timetaken_desc[timetaken] for timetaken in list_timetaken]
    

    print(f'\nYour course list:\n{list_courses}\nTheir corresponding difficulties:\n{list_difficulties_desc}\nTheir corresponding time taken:\n{list_timetaken_desc}')
    
    num_courses = len(list_courses)
    # integer that represents the length of the courses array, isn't used as of now but is here in case you need it later


def coursecheck():
    #checks that the courses the user entered are in line with what they want 

    check = input("Please check that these are the courses you're taking by responding 'yes' or 'no'\n")
    if check.lower() in ['yes', 'y']:
        print(f'\nYay! You are ready to move on.')
    elif check.lower() in ['no', 'n']:
        set_courses_and_difficulties()
    else: 
        print(f'\nError. Please specify "yes" or "no".')
        coursecheck()


if __name__ == "__main__":
    set_courses_and_difficulties()
    coursecheck()


# A refined way to obtain the "difficulty of an assignment in a numerical form
# The course difficulty can weigh heavier and then the assignment diffculty can be added

# The modified parameters of this method are difficulty_level (of the course material) and workload_level (how much time you need to spend on the course)
def get_difficulty_index(difficulty_level, workload_level):

   # Through a 'joint list' implemented via a Python dictionary, `course_info`
   # make the course difficulty weighed more than the homework efficiency            
   index = (difficulty_level * 2) + workload_level
   return index
