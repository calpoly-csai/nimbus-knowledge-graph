from grakn.client import GraknClient
import pandas as pd

name_of_type = "Sections.csv"

df = pd.read_csv(name_of_type)

with GraknClient(uri="localhost:48555") as client:
	with client.session(keyspace="calpoly") as session:
		## Insert a Person using a WRITE transaction
		with session.transaction().write() as write_transaction:
			for index, current_row in df.iterrows():

				# Gather professor/section info
				prof_name = current_row["INSTRUCTOR"].split(", ")
				first_name = prof_name[1]
				last_name = prof_name[0]
				title = current_row["TITLE"]
				phone = current_row["PHONE"]
				alias = current_row["ALIAS"]
				email = alias + "@calpoly.edu"
				office = current_row["OFFICE"]

				professorQuery = """
								insert $x isa professor,
									has first_name "{}",
									has last_name "{}",
									has	title "{}",
									has	phone "{}",
									has	alias "{}",
									has	email "{}",
									has	office "{}";
								""".format(first_name, last_name, title, phone, 
										alias, email, office)

				# Section-only info
				course_name = current_row["COURSE_NAME"]
				section_number = current_row["SECTION_NUMBER"]
				instructor = first_name + " " + last_name
				# alias = current_row["alias"]
				# title = current_row["title"]
				# phone = current_row["phone"]
				# office = current_row["OFFICE"]
				section_type = current_row["TYPE"]
				days = current_row["DAYS"]
				start = current_row["START"]
				end = current_row["END"]
				location = current_row["LOCATION"]
				department = current_row["DEPT"]

				queryToInsert = """
								insert $x isa section,
									has section_name "{}",
									has instructor "{}",
									has	alias "{}",
									has	title "{}",
									has	phone "{}",
									has	office "{}",
									has	section_type "{}",
									has	days "{}",
									has	start "{}",
									has	end "{}",
									has	location "{}",
									has	department "{}";
								""".format(section_name, instructor, alias, title, phone, office, section_type, days, start, end, location, department)

				insert_iterator = write_transaction.query(queryToInsert).get()
				concepts = [ans.get("x") for ans in insert_iterator]
				print("Inserted a section with ID: {0}".format(concepts[0].id))
				## to persist changes, write transaction must always be committed (closed)
			write_transaction.commit()