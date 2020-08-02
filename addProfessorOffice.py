from grakn.client import GraknClient
import pandas as pd
import re

dfProf = pd.read_csv("Professors.csv")
dfOffice = pd.read_csv("OfficeHours.csv")

with GraknClient(uri="localhost:48555") as client:
	with client.session(keyspace="nimbus") as session:
		## Insert a Person using a WRITE transaction
		with session.transaction().write() as write_transaction:

			matches = []

			for index, prof_row in dfProf.iterrows():
				if not (isinstance(prof_row["email"], str)):
					continue
				for index, office_row in dfOffice.iterrows():
					#print(prof_row["email"], office_row["email"])
					if (re.search('.*\@', prof_row["email"]).group(0) == office_row["email"]):
						matches.append((prof_row["email"], office_row["email"]))

			for match in matches:

				queryToInsert = """
								match 
									$p isa professor, has email "{}";
									$o isa officeHours, has email "{}";
								insert $x (professorOfOffice: $p, officeOfProfessor: $o) isa professorOffice;
								""".format(*match)


				insert_iterator = write_transaction.query(queryToInsert).get()
				concepts = [ans.get("x") for ans in insert_iterator]
				print("Inserted a professor-office relation with ID: {0}".format(concepts[0].id))
				## to persist changes, write transaction must always be committed (closed)
			write_transaction.commit()