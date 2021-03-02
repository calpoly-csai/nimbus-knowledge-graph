# calpoly-knowledge-graph

## Docker Setup
1. Make sure you have Docker and docker-compose setup on your machine:
```
snekiam:~/calpoly-knowledge-graph$ docker --version
Docker version 19.03.8, build afacb8b7f0

snekiam:~/calpoly-knowledge-graph$ docker-compose --version
docker-compose version 1.27.4, build 40524192
```
2. `cd` to ./docker, and run `docker-compose up` (yours may have more output, I had packages cached on my system already):
```
snekiam:~/calpoly-knowledge-graph/docker$ docker-compose up
Starting grakn ... done
Attaching to grakn
grakn    | ====================================================================================================
grakn    |       ________  _____     _______  __    __  __    __      _______  _______  _____     _______
grakn    |      |   __   ||   _  \  |   _   ||  |  /  /|  \  |  |    |   _   ||   _   ||   _  \  |   ____|
grakn    |      |  |  |__||  | |  | |  | |  ||  | /  / |   \ |  |    |  | |__||  | |  ||  | |  | |  |
grakn    |      |  | ____ |  |_| /  |  |_|  ||  |/  /  |    \|  |    |  |     |  | |  ||  |_| /  |  |____
grakn    |      |  ||_   ||   _  \  |   _   ||   _  \  |   _    |    |  |  __ |  | |  ||   _  \  |   ____|
grakn    |      |  |__|  ||  | \  \ |  | |  ||  | \  \ |  | \   |    |  |_|  ||  |_|  ||  | \  \ |  |____
grakn    |      |________||__|  \__\|__| |__||__|  \__\|__|  \__|    |_______||_______||__|  \__\|_______|
grakn    |
grakn    |                                          THE KNOWLEDGE GRAPH
grakn    | ====================================================================================================
grakn    |                                                                                       Version:  1.8.4
grakn    | Starting Storage..................SUCCESS
grakn    | Starting Grakn Core Server.....SUCCESS
```
This may take a minute. If you get the following output:
```
snekiam:~/calpoly-knowledge-graph/docker$ docker-compose up
Creating docker_grakn_1 ... done
Attaching to grakn
grakn    | ====================================================================================================
grakn    |       ________  _____     _______  __    __  __    __      _______  _______  _____     _______
grakn    |      |   __   ||   _  \  |   _   ||  |  /  /|  \  |  |    |   _   ||   _   ||   _  \  |   ____|
grakn    |      |  |  |__||  | |  | |  | |  ||  | /  / |   \ |  |    |  | |__||  | |  ||  | |  | |  |
grakn    |      |  | ____ |  |_| /  |  |_|  ||  |/  /  |    \|  |    |  |     |  | |  ||  |_| /  |  |____
grakn    |      |  ||_   ||   _  \  |   _   ||   _  \  |   _    |    |  |  __ |  | |  ||   _  \  |   ____|
grakn    |      |  |__|  ||  | \  \ |  | |  ||  | \  \ |  | \   |    |  |_|  ||  |_|  ||  | \  \ |  |____
grakn    |      |________||__|  \__\|__| |__||__|  \__\|__|  \__|    |_______||_______||__|  \__\|_______|
grakn    |
grakn    |                                          THE KNOWLEDGE GRAPH
grakn    | ====================================================================================================
grakn    |                                                                                       Version:  1.8.4
grakn    | Starting Storage.......................Unable to start Storage.
grakn    | FAILED!
```
simply hit `ctrl+c`, and re-run `docker-compose up`. I noticed this on every first start, but I think it has to do with my system specifically

3. If this is your first time running the CalPoly Knowledge Graph (it probably is if you're reading this guide), or if you've wiped the docker/grakn_data folder, run:
```
snekiam:~/calpoly-knowledge-graph/docker$ ./setup_schema.sh
Loading: /grakn-core-all-linux/server/db/schema.gql
...
{}
Successful commit: schema.gql
```
4. You're done! You can populate the knowledge graph with data, and it will live at calpoly-knowledge-graph/docker/grakn_data. This should be persistant, and survive restarts of docker containers.
The knowledge graph is operating at localhost:48555.
