from grakn.client import GraknClient
import pandas as pd

name_of_type = "Courses.csv"

df = pd.read_csv(name_of_type)

with GraknClient(uri="localhost:48555") as client:
	with client.session(keyspace="nimbus") as session:
		## Insert a Person using a WRITE transaction
		with session.transaction().write() as write_transaction:
			for index, current_row in df.iterrows():

				department = current_row["DEPT"]
				course_name = current_row["COURSE_NAME"]
				course_title = current_row["COURSE_TITLE"]
				print(course_title)
				units = current_row["UNITS"]
				prerequisites = current_row["PREREQUISITES"]
				corequisites = current_row["COREQUISITES"]
				concurrent = current_row["CONCURRENT"]
				recommended = current_row["RECOMMENDED"]
				terms_offered = current_row["TERMS_TYPICALLY_OFFERED"]
				ge_areas = current_row["GE_AREAS"]
				description = "nan"

				queryToInsert = """
								insert $x isa course,
									has department "{}",
									has course_name "{}",
									has course_title "{}",
									has units "{}",
									has prerequisites "{}",
									has corequisites "{}",
									has concurrent "{}",
									has recommended "{}",
									has terms_offered "{}",
									has ge_areas "{}",
									has description "{}";
								""".format(department, course_name, course_title, 
									units, prerequisites, corequisites, 
									concurrent, recommended, terms_offered, ge_areas, description)

				print(queryToInsert)

				insert_iterator = write_transaction.query(queryToInsert).get()
				concepts = [ans.get("x") for ans in insert_iterator]
				print("Inserted a course with ID: {0}".format(concepts[0].id))
				## to persist changes, write transaction must always be committed (closed)
			write_transaction.commit()