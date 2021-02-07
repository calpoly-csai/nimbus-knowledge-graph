from grakn.client import GraknClient
import pandas as pd
import re, sys
import time
start_time = time.time()

# What is [COURSE] about? 
# [COURSE] is about [COURSE..description]

def findTypeAndModifier(input_question) -> tuple:
	entityType = re.search('\[\w*\]', input_question).group(0)[1:-1].lower()
	modifier = re.search('\.\.\w*\]', input_question).group(0)[2:-1].lower()

	return (entityType, modifier)

def formQuery(entityType, entityIdentifier, modifier) -> str:
	return "match $x isa {}, has {}_name \"{}\", has {} $y; get $y;".format(entityType, entityType, entityIdentifier, modifier)
    #return "match $x isa {}, has attribute \"{}\", has {} $y; get $y;".format(entityType, entityIdentifier, modifier) #takes significantly longer

def queryGrakn(stringToQuery, modifier):
	with GraknClient(uri="localhost:48555") as client:
		with client.session(keyspace="nimbus") as session:
			## Insert a Person using a WRITE transaction
			with session.transaction().read() as read_transaction:
				answer_iterator = read_transaction.query(stringToQuery).get()

				answers = [ans.get("y") for ans in answer_iterator]
				result = [ans.value() for ans in answers]

				return result[0]

				

if __name__ == "__main__":
	input_question = sys.argv[1]

	entityIdentifier = sys.argv[2]

	entityType, modifier = findTypeAndModifier(input_question) 
	query = formQuery(entityType, entityIdentifier, modifier)
	res = queryGrakn(query, modifier)

	filledQuestion = input_question.replace("[{}]".format(entityType.upper()), entityIdentifier).replace("[{}..{}]".format(entityType.upper(), modifier), res)

	print("\n" + filledQuestion + "\n")

	print("--- %s seconds ---" % (time.time() - start_time))