# PythonI3-PR2
#User Guide 
Installer anaconda sur votre machine
Via anaconda prompt taper: 
Pip install pandas
Pip installplotly
Pip install dash
Pip install plotly_express
•  Télécharger le projet (sous forme de zip) et l’extraire dans un répertoire
•  Aller dans la console de commande et placer vous dans ce répertoire
•  Faire la commande "python main.py"
•  Taper l'adresse "http://127.0.0.1:8050/" dans la barre de recherche de votre navigateur
•  Ne pas fermez la console de commande pendant la visualisation du site
Vous pouvez désormais voir le  Dashboard ! 

#Developper Guide
Le projet contient un seul fichier python (.py) séparé avec  des commentaires :
On trouve dans  le  code : 
Les imports, et l’import du .csv, les remplissages des data frames, la création de data séries,  Création du dash et des figures. 
Afin de  rajouter des graphiques (et ou amélioration tel qu’un slider), il faut rajouter dans la partie #création du Dash le code nécessaire. Pour le slider il faudra aussi créer de nouvelle  Data Frames dans  la partie dédié !

#Rapport d'analyse
Les données appartiennent à : http://www.worldbank.org
Le sujet traité est la population de réfugiés dans  le monde à l’aide de Population de réfugiés par pays ou par territoire d’asile
Définition : Les réfugiés sont des personnes qui sont reconnues comme réfugiés en vertu de la Convention Relative au Statut des Réfugiés ou à son Protocole de 1967, la Convention de l'Organisation de l'Unité africaine de 1969 régissant les Aspects spécifiques des problèmes des réfugiés en Afrique, les personnes reconnues comme réfugiés selon le statut de l'UNHCR, les personnes auxquelles on a accordé un statut humanitaire de réfugié et les personnes bénéficiant d'une protection temporaire. Les demandeurs d'asile (personnes qui ont fait une demande d'asile ou du statut de réfugié et qui n'ont pas encore reçu une décision ou qui sont enregistrées comme demandeurs d'asile) sont exclus. Les réfugiés palestiniens sont des personnes (et leurs descendants) dont le pays de résidence était la Palestine entre juin 1946 et mai 1948 et qui ont perdu leur maison et leur moyens de subsistance suite au conflit arabo-israélien de 1948. Pays d'asile est le pays où une demande d'asile a été déposé et accordé.
Il est intéressant de montrer à l’aide d’outil notamment un Dashboard, les évolutions sociogéographiques dans  le monde. Ce sujet me semble donc pertinent a traité. 
Tout d’abord la base de données récupérée comprend plus de 200 territoires. Uniquement les pays ont étés traités dans le sujet. L’étude commence à partir de 1960 jusqu’en 2019. Certaines données anciennes peuvent  donc manquer et créer des erreurs dans l’analyse.
L’histogramme : 
On peut voir sur cet histogramme l’évolution de la population de réfugiés dans le monde. En 1960, il y a seulement 2.6 millions de   réfugiés dans le monde. On peut noter dès 1976 une évolution croissante des réfugiés jusqu’aux années 1990 où l’on observe un pic à presque 21 millions de réfugiés en 1992. Ce chiffre baissera jusqu’à 2005 où l’on tombera à 13.3 millions de réfugiés. Ce chiffre grimpera jusqu’à 26 millions en 2019 avec une hausse constante  dès 2013. L’écart entre les pays dans les années  1970 se creuse et se ressent donc dans l’évolution  des réfugiés. En  effet, la période d’après-guerre permet aux grandes puissances de  se développer très rapidement. L’instabilité dans le tiers-monde pour des raisons économiques, politiques pousse alors les gens à se réfugier dans les pays riches. 

La carte : 
Il n’y a pas d’échelle logarithmique sur la carte, donc il se peut que les pays avec une couleur bleu (très présente) puissent tout de même avoir jusqu’à 200 000 réfugiés. 
Il faut donc savoir qu’un pays avec une couleur qui commence à teindre au violet a déjà un certains nombres de réfugiés dans leur pays. 
On peut voir assez aisément   que la Turquie, le Pakistan,  l’Iran, Palestine, Liban, Jordanie, l’Allemagne et le Soudan accueille le plus de réfugiés. On peut donc comprendre par la zone géographique les différentes raisons de cette migration. 
Ces accueille principalement des réfugiés pour des raisons sociopolitiques.  
On peut aussi vite observer que le continent avec le moins de réfugiés est l’Amérique. 

Pour conclure une carte avec un slider (une  carte par année) et avec une échelle logarithmique aurait permis de mieux analyser l’évolution dans le monde, mais aussi de mieux remarqué les pays ayant moins de réfugiés.
