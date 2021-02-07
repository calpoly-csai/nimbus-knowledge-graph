from grakn.client import GraknClient
import pandas as pd

name_of_type = "Sections.csv"

df = pd.read_csv(name_of_type)

with GraknClient(uri="localhost:48555") as client:
	with client.session(keyspace="nimbus") as session:
		## Insert a Person using a WRITE transaction
		with session.transaction().write() as write_transaction:
			for index, current_row in df.iterrows():

				section_name = current_row["section_name"]
				instructor = current_row["instructor"]
				alias = current_row["alias"]
				title = current_row["title"]
				phone = current_row["phone"]
				office = current_row["office"]
				section_type = current_row["type"]
				days = current_row["days"]
				start = current_row["start"]
				end = current_row["end"]
				location = current_row["location"]
				department = current_row["department"]

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