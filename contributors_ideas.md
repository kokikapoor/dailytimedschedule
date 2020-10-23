# Contributor's Ideas
## Space for contributors' responses to the "Recommended Help" section of the README.md file 

### On improving the correlation between class difficulty and time: 
In terms of requesting information about class difficulty, rather than asking users to match their class to a category, you could consider asking them to input a rating of 1) how much time they spend on the given class and 2) how intense/difficult the material is. The information you are requesting right now is nearly identical, and if you asked users to rate on a scale of 1-3, you'd get 9 possible combinations that correspond closely to the categories from your README. However, I suggest this format because 2 numerical values for each class may be easier to work with than one categorical value downstream. 

If I'm understanding your question, you're looking for ways to more accurately use inputted difficulty to estimate how long daily classwork may take. Depending on how you are planning to make that estimation, numbers may be easier to use in calculations. In particular, if you're hoping to improve the correlation between class difficulty and time and believe users might not be the best at estimating the time their classes would take, using a numerical format could allow you to take their uncertainty/inaccuracy into account and scale/adjust expected time without the tangle of if statements that a categorical analysis might necessitate.

Moreover, a numerical input format could potentially make for a more intuitive and more streamlined input experience (simpler prompts).

### On reducing time a user spends inputting data:
To store previous answers, you could consider creating a (potentially hidden) file in a user's home directory (or somewhere else) that could store users' inputted information in CSV format. In its simplest form, each row of the file could use the format `course,difficulty`, and you could quickly write/read the information either using plain Python code or by leveraging the `pandas` library ([read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) and [to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) specifically) if you'd like to avoid implementation details.


## Ideas for future features of the program 
You could make this program responsive to daily user feedback. For example, if a user inputted a class as very easy and quick but spent more than the time allotted on their assignments, you could allow them to go back and re-rate class difficulties or (maybe more interestingly) provide a daily feedback form of sorts asking how long they expected to take on a class vs. how long they actually did (either actual numerical estimates or a just a sense of things). This could on one hand help them reflect upon and better understand their work habits and on the other hand allow you to adjust your time estimates for each class.

You could also potentially make the library accessible to teachers; being able to see how long students are spending on the assignments/the level of difficulty of the material for students could be really valuable for teaching and adjusting the material accordingly. It could be similar to the Quizlet "class" feature, or it could just provide overall summary statistics about difficulty/time spent on the material for each week.
