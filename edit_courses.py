import pandas as pd

df = pd.read_csv("Courses.csv")

for index, row in df.iterrows():
    name_and_section = str(row['COURSE_NAME_AND_TITLE']).replace('\xa0', ' ').split('. ')
    name_and_section[1] = name_and_section[1].replace('.', '')

    print(name_and_section)

    df['COURSE_NAME'][index] = name_and_section[0]
    if len(name_and_section) > 1:
        df['COURSE_TITLE'][index] = name_and_section[1]

df.to_csv("Courses.csv", index=False)
