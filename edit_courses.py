import pandas as pd

df = pd.read_csv("Courses.csv")

for index, row in df.iterrows():
    # Clean up the course name and title and split them into different rows
    name_and_section = str(row['COURSE_NAME_AND_TITLE']).replace('\xa0', ' ').split('. ')
    name_and_section[1] = name_and_section[1].replace('.', '')

    df['COURSE_NAME'][index] = name_and_section[0]
    if len(name_and_section) > 1:
        df['COURSE_TITLE'][index] = name_and_section[1]

    print(name_and_section)

    # Remove unncessary commas
    prerequisites = str(row['PREREQUISITES'])
    prerequisites = prerequisites.replace(',', ' ')
    prerequisites = prerequisites.replace('  ', ', ')
    df['PREREQUISITES'][index] = prerequisites

df.to_csv("Courses.csv", index=False)
