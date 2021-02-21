from grakn.client import GraknClient
import pandas as pd

name_of_type = "Professors.csv"

df = pd.read_csv(name_of_type)

with GraknClient(uri="localhost:48555") as client:
	with client.session(keyspace="calpoly") as session:
		## Insert a Person using a WRITE transaction
		with session.transaction().write() as write_transaction:
			for index, current_row in df.iterrows():
				first_name = current_row["first_name"]
				last_name = current_row["last_name"]
				phone_number = current_row["phone_number"]
				research_interests = current_row["research_interests"]
				email = current_row["email"]

				queryToInsert = """
								insert $x isa professor,
									has first_name "{}",
									has last_name "{}",
									has phone_number "{}",
									has research_interests "{}",
									has email "{}";
								""".format(first_name, last_name, phone_number, research_interests, email)

				insert_iterator = write_transaction.query(queryToInsert).get()
				concepts = [ans.get("x") for ans in insert_iterator]
				print("Inserted a professor with ID: {0}".format(concepts[0].id))
				## to persist changes, write transaction must always be committed (closed)
			write_transaction.commit()