from grakn.client import GraknClient
import pandas as pd

name_of_type = "Courses.csv"

df = pd.read_csv(name_of_type)

with GraknClient(uri="localhost:48555") as client:
	with client.session(keyspace="nimbus") as session:
		## Insert a Person using a WRITE transaction
		with session.transaction().write() as write_transaction:
			for index, current_row in df.iterrows():

				department = current_row["dept"]
				course_num = current_row["course_num"]
				terms_offered = current_row["terms_offered"]
				units = current_row["units"]
				course_name = current_row["course_name"]
				concurrent = current_row["concurrent"]
				corequisites = current_row["corequisites"]
				recommended = current_row["recommended"]
				prerequisites = current_row["prerequisites"]
				ge_areas = current_row["ge_areas"]
				description = current_row["desc"]

				queryToInsert = """
								insert $x isa course,
									has department "{}",
									has course_num "{}",
									has terms_offered "{}",
									has units "{}",
									has course_name "{}",
									has concurrent "{}",
									has corequisites "{}",
									has recommended "{}",
									has prerequisites "{}",
									has ge_areas "{}",
									has description "{}";
								""".format(department, course_num, terms_offered, units, course_name, concurrent, corequisites, recommended, prerequisites, ge_areas, description)

				insert_iterator = write_transaction.query(queryToInsert).get()
				concepts = [ans.get("x") for ans in insert_iterator]
				print("Inserted a course with ID: {0}".format(concepts[0].id))
				## to persist changes, write transaction must always be committed (closed)
			write_transaction.commit()