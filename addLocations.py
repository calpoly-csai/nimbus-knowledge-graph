from grakn.client import GraknClient
import pandas as pd

name_of_type = "Locations.csv"

df = pd.read_csv(name_of_type)

with GraknClient(uri="localhost:48555") as client:
	with client.session(keyspace="calpoly") as session:
		## Insert a Person using a WRITE transaction
		with session.transaction().write() as write_transaction:
			for index, current_row in df.iterrows():

				# Gather location data				
				building_number = current_row['BUILDING_NUMBER']
				building_name = current_row['NAME']
				longitude = current_row['LONGITUDE']
				latitude = current_row['LATITUDE']
				
				# TODO: I have this entity set as building for now because
				# calling it "location" created conflicts with the "location"
				# attribute for sections
				locationQuery = """
								insert $x isa building,
									has building_number "{}",
									has building_name "{}",
									has	longitude "{}",
									has	latitude "{}";
								""".format(building_number, building_name,
									longitude, latitude)

				insert_iterator = write_transaction.query(locationQuery).get()
				concepts = [ans.get("x") for ans in insert_iterator]
				print("Inserted a location with ID: {0}".format(concepts[0].id))
				## to persist changes, write transaction must always be committed (closed)
			write_transaction.commit()