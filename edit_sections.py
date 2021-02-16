import pandas as pd

df = pd.read_csv("Sections.csv")

for index, row in df.iterrows():
    name_and_section = str(row['COURSE_ID']).replace(' (1)', '').replace(' (2)', '').replace(' /2', '').replace(' /3', '').split('_')

    df['COURSE_NAME'][index] = name_and_section[0]

    split_name = name_and_section[0].split()
    dept = split_name[0]
    df['DEPT'][index] = dept

    if len(name_and_section) > 1:
        section_number = name_and_section[1]
        df['SECTION_NUMBER'][index] = section_number

df.to_csv("Sections.csv", index=False)
