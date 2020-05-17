# python-rdf

It's the basic example of [Resource Description Framework](https://www.w3.org/RDF/) usage with [rdflib](https://rdflib.readthedocs.io/en/stable/).


## requirements

All needed python libraries are described in **requirements.txt** file.
Type

`pip install -r requirements.txt`

in python3 virtualenv to install them.
## ontology model and dataset

Example ontology model represents NBA environment - teams and players. Collected data has been taken mainly from [lineups.com/nba](https://www.lineups.com/nba) page.

## usage

```
usage: rdf.py [-h] -s subject predicates objects

optional arguments:
  -h, --help            show this help message and exit
  -s subject predicates objects, --sparql subject predicates objects
                        Semantic triple. Subject can be player or team. To
                        make more advanced query, pass predicates and objects
                        separated by comma.
```

## examples
1. Get all players will Michael Jordan's height (198cm):
```
python rdf.py -s player nba:isTallCm nba:198
Executing SPARQL query: 'SELECT ?player WHERE { ?player nba:isTallCm nba:198 . }'
http://nba.com/JoeHarris
http://nba.com/CarisLeVert
http://nba.com/ShaiGilgeousAlexander
http://nba.com/TimHardaway
http://nba.com/RoyceONeale
http://nba.com/SpencerDinwiddie
http://nba.com/ZionWilliamson
http://nba.com/CodyMartin
http://nba.com/PJTucker
http://nba.com/WillBarton
http://nba.com/DannyGreen
http://nba.com/DillonBrooks
http://nba.com/DevinBooker
http://nba.com/BogdanBogdanovic
http://nba.com/JoshRichardson
http://nba.com/LonzoBall
```
2. Get all teams from Western conference and Pacific division:
```
python rdf.py -s team nba:belongsToConference,nba:belongsToDivision nba:Western,nba:Pacific
Executing SPARQL query: 'SELECT ?team WHERE { ?team nba:belongsToConference nba:Western . ?team nba:belongsToDivision nba:Pacific . }'
http://nba.com/PhoenixSuns
http://nba.com/LosAngelesClippers
http://nba.com/GoldenStateWarriors
http://nba.com/LosAngelesLakers
http://nba.com/SacramentoKings
```
3. Get all Small Forwards who studied at Duke university:
```
python rdf.py -s player nba:studiedAt,nba:playsAs nba:Duke,nba:SmallForward
Executing SPARQL query: 'SELECT ?player WHERE { ?player nba:studiedAt nba:Duke . ?player nba:playsAs nba:SmallForward . }'
http://nba.com/BrandonIngram
http://nba.com/JaysonTatum
```
4. Get European players (no college career) from Sacramento Kings:
```
python rdf.py -s player nba:studiedAt,nba:playsFor nba:Europe,nba:SacramentoKings
Executing SPARQL query: 'SELECT ?player WHERE { ?player nba:studiedAt nba:Europe . ?player nba:playsFor nba:SacramentoKings . }'
http://nba.com/NemanjaBjelica
http://nba.com/BogdanBogdanovic
```
5. Get teams founded in 1946 (NBA was founded in the same year) from Atlantic division:
```
python rdf.py -s team nba:foundedIn,nba:belongsToDivision nba:1946,nba:Atlantic  
Executing SPARQL query: 'SELECT ?team WHERE { ?team nba:foundedIn nba:1946 . ?team nba:belongsToDivision nba:Atlantic . }'
http://nba.com/NewYorkKnicks
http://nba.com/BostonCeltics
```
