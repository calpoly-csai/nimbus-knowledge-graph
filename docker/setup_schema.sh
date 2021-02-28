#!/bin/bash
cp ../schema.gql ./grakn_data/
docker exec -it grakn bash -c '/grakn-core-all-linux/grakn console -keyspace calpoly --file /grakn-core-all-linux/server/db/schema.gql'