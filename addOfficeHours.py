from grakn.client import GraknClient
import pandas as pd

name_of_type = "OfficeHours.csv"

df = pd.read_csv(name_of_type)

with GraknClient(uri="localhost:48555") as client:
	with client.session(keyspace="nimbus") as session:
		## Insert a Person using a WRITE transaction
		with session.transaction().write() as write_transaction:
			for index, current_row in df.iterrows():

				office = current_row["office"]
				email = current_row["email"]
				office_hours = current_row["office_hours"]
				monday = current_row["monday"]
				tuesday = current_row["tuesday"]
				wednesday = current_row["wednesday"]
				thursday = current_row["thursday"]
				friday = current_row["friday"]
				phone = current_row["phone"]
				platform = current_row["platform"]
				latest_quarter = current_row["latest_quarter"]
				

				queryToInsert = """
								insert $x isa officeHours,
									has office "{}",
									has	email "{}",
									has	office_hours "{}",
									has	monday "{}",
									has	tuesday "{}",
									has	wednesday "{}",
									has	thursday "{}",
									has	friday "{}",
									has	phone "{}",
									has platform "{}",
									has	latest_quarter "{}";
								""".format(office, email, office_hours, monday, tuesday, wednesday, thursday, friday, phone, platform, latest_quarter)

				insert_iterator = write_transaction.query(queryToInsert).get()
				concepts = [ans.get("x") for ans in insert_iterator]
				print("Inserted an officeHours item with ID: {0}".format(concepts[0].id))
				## to persist changes, write transaction must always be committed (closed)
			write_transaction.commit()