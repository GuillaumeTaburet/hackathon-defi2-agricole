# Hackathon Climat en données

## Défi 2 et 8 - Enjeux des transitions agricoles : Détermination des aires biogéographiques régionales compatibles avec l'implantation d'une culture émergente au sein des climats futurs possibles de la TRACC

### Participant.e.s :

Mathilde HIBON : GIP LIA - ingénieure agronome, indicateurs et visualisations data.  
Aurélien Mure : CEREMA - compétences data.  
Carole PERIGOIS : astrophysique et data.  
Marion HOUDAYER : programmation, manipulation data.  
Guillaume TABURET : SOLAGRO - programmation, manipulation et visualisation data.

---

### Contexte et enjeux généraux du projet

Dans le contexte de l’adaptation au changement climatique, les acteurs des territoires agissant pour l’agriculture (services de l’Etat, animateurs territoriaux, opérateurs agricoles, …) ont besoin d’outils leur permettant d’explorer les possibilités d’adaptation des agricultures de leurs territoires, à diverses échelles pertinentes pour l’action (par exemple un bassin versant, un département, une région agricole).

Il existe divers outils de projections des indicateurs agricoles au regard du changement climatique (ex : Climadiag), mais il est plus difficile de trouver des visuels cartographiques dynamiques qui projettent des données climatiques futures à une échelle territoriale pertinente pour informer les décisions **pratiques et stratégiques** à prendre pour l'avenir de l'agriculture.
En particulier, il paraît utile d’étudier **l'adaptation des cultures et le choix de cultures dites émergentes** (olivier, légumineuses, ...) sur un territoire donné au regard des futurs climats.

Via notre travail, l’idée est d’**outiller les territoires pour explorer l’adaptation d’une culture émergente au changement climatique face à divers stress climatiques** : nous prenons l’exemple de la **culture de l’olivier** dans la région Occitanie.

Pour cela, nous avons tenté de répondre à la problématique suivante : **existe-t-il une ou plusieurs aires biogéographiques compatibles avec la culture de l’olivier en Occitanie, dans les climats futurs de la TRACC ?**

### Les enjeux et usages pour un territoire et ses agricultures : cas de figure du Gers (32)

Les impacts climatiques sont déjà ressentis par les agriculteurs du Gers : sécheresses plus longues et extrêmes, gels tardifs, pluies intenses en hiver, …

Se reposer sur les connaissances empiriques de la météo et des saisons n’est plus suffisamment efficace, et les réflexions sur les rotations sont de plus en plus opportunistes : les agriculteurs, confrontés à une incertitude grandissante, se tournent vers les cultures et les marchés rémunérateurs sur le court-terme, sans pouvoir bien déceler la viabilité de ces paramètres dans le futur.

Néanmoins, tous et toutes pressentent que tout ou partie des cultures - et donc des filières -en place aujourd’hui ne seront plus viables demain, et que trouver des cultures émergentes compatibles avec le climat futur est nécessaire pour que l’agriculture continue d’exister dans le Gers.
Ce travail n’est pas forcément mené par les coopératives agricoles, malgré leurs difficultés économiques actuelles avec les filières en place ; les espaces de discussion des enjeux d’adaptations et d’émergences des filières manquent, mais aussi les supports pour alimenter cette discussion nécessaire.

Parmi les cultures émergentes dont la pertinence pour le Gers est à étudier désormais que le changement climatique se manifeste, il y a l’olivier.

Si on sait que l’olivier n’était pas cultivable dans le Gers jusqu’à maintenant, quid dans le futur ? **La culture de l’olivier est-elle compatible avec les conditions climatiques futures du Gers ?**

Nous avons voulu créer un **outil visuel permettant d’explorer les aires biogéographiques compatibles avec la culture de l’olivier dans toute l’Occitanie**, afin d’explorer les « migrations » de ces aires compatibles au sein de la région et identifier si le Gers est l’une d’elle.
Ces visuels permettraient d’en faire des supports de discussion en faveur ou défaveur de l’introduction de cultures émergentes comme l’olivier avec les acteurs des territoires, et d’ouvrir des discussions stratégiques et pratiques (économiques, sociales, agronomiques, … ) autour de ces nouvelles cultures.

### Approche adoptée

La volonté est de créer des rendus cartographiques en réponse aux différentes trajectoires TRACC qui puissent permettre de déterminer les aires biogéographiques compatibles et, idéalement, les fenêtres temporelles les plus favorables et défavorables à la culture en question.
A partir de la littérature scientifique, quatre indicateurs phénologiques sont sélectionnés. Pour chacun d’entre eux, des seuils phénologiques sont déterminés afin d’identifier les situations de stress abiotiques intenses qui rendraient incompatible la culture de l’olivier dans une aire biogéographique

- Les températures minimales pour étudier les risques liés au **gel** : par période de 20 ans, nombre d’occurrence du dépassement du seuil -12°C ou de + de 5 fois -7°C par hiver
- Les températures maximales pour étudier les risques liés à la **sécheresse intense** : par période de 20 ans, nombre d’occurrence du dépassement du seuil 40°C ou 35°C 3 jours consécutifs entre avril et juin.
- Les précipitations et l’ETP pour déterminer le **déficit hydrique** : par période de 20 ans, nombre d’occurrence du dépassement du seuil -100mm de déficit hydrique sommé sur JJA
- Le **besoin en froid** de la culture : par période de 20 ans, nombre d’années où (Tmin + Tmax)/2 <=12°C pour une période inférieure à 70 jours entre novembre et février.

Pour ce faire, nous mobilisons deux RCM (8 km de résolution) forcés à partir de deux GCM différents.
L’objectif est d’obtenir une carte par indicateur et par modèle, déclinée pour les trois horizons de la TRACC (2°C, 2,7°C et 4°C pour la France métropolitaine). Chaque horizon de la TRACC est présenté en fenêtre de 20 ans.

### Analyse de deux indicateurs : le risque de gel intense et la chaleur extrême

**Pour le risque de gel intense (jours < -12°C)**

_La littérature nous informe qu’un seul jour inférieur à -12°C peut compromettre définitivement la survie de l’olivier._

La période de référence (1960-1979) nous montre que le nombre de jours <-12°C était compris entre 1 et 2j pour pour la majorité du Gers, avec pour quelques zones, plutôt dans le Sud, un nombre compris entre 2 et 3j. Le risque était donc assez important, réduisant grandement la compatibilité de la zone pour la culture de l’olivier au regard de cet indicateur.
En revanche, le pourtour médiétrannéen ne connaissait que très rarement des jours <-12°C (entre 0 et 1 jour par an maximum), ce qui rendait la compatibilité possible : le risque était réduit.
Alors que, sur la période de référence, des contrastes importants existaient concernant le risque de connaître des jours <-12°C, ces contrastes s’effacent peu à peu et disparaissent complètement à l’horizon 2071-2090 (4°C de réchauffement). A cet horizon, l’ensemble de la région Occitanie, à l’exception des zones montagneuses en altitude, connaîtrait entre 0 et 1 jour <-12°C.
Au regard de ce paramètre, la très grande majorité de la région Occitanie devient compatible pour la culture de l’olivier.

**Pour le risque de chaleur intense (jours >40°C)**

_La littérature nous informe qu’un seul jour supérieur à 40°C peut compromettre définitivement la survie de l’olivier._

La période de référence (1960-1979) nous informe qu’aucune zone de l’Occitanie n’était concernée par des journées >40°C.
Concernant les 3 horizons de la TRACC, on constate que des zones concernées par des jours >40°C apparaissent sur toute la région. Pour la période 2032-2051 (2°C de réchauffement), certaines zones se distinguent et notamment toute la partie Est du département du Gers, qui présente entre 1 et 2 jour par an >40°C en moyenne.
Pour la période 2052-2071 (2,7°C de réchauffement), la quasi totalité du département du Gers est concernée par 2 à 3 jours par an >40°C en moyenne, tandis que la partie Est de l’Occitanie est elle aussi globalement concernée par une augmentation des jours >40°C.
A l’horizon 2071-2090 (4°C de réchauffement), de forts contrastes régionaux apparaissent, avec une majorité de l’Occitanie concernée par plus de 4 jours par an >40°C en moyenne. Le Gers compte 5 jours par an en moyenne. Le pourtour méditérannéen, jusque là aire compatible où l’olivier se cultive, connaît le plus de jours par an >40°C, avec en moyenne plus de 5j et jusqu’à 12j par an environ.
Au regard de ce paramètre, on constate que le Gers est une aire plutôt incompatible avec la culture de l’olivier, au même titre que des aires sur lesquelles l’olivier est historiquement cultivé (ex: littoral méditérannéen). Dans le Gers, l’implantation de l’arbre et sa rentrée en pleine production (aux alentours de 20 ans de vie) ne pourraient à priori s’envisager sans risques accrus pour l’arbre après la période 2032-2051.

### Limites et pistes d’amélioration pour l’analyse de la compatibilité du Gers avec la culture de l’olivier

L’ensemble des indicateurs identifiés lors du projet n’ont pas été traités, rendant l’analyse partielle.
L’analyse des deux indicateurs ci-avant permet de montrer le contraste existant entre différents indicateurs (gel et chaleur extrême), qui parfois donnent des informations de compatibilité géographique contradictoires. De plus, il faudrait pour chaque indicateur affiner l’analyse par saison et stades phénologiques de développement de l’olivier (stade juvénile, floraison, etc.) afin de préciser les fenêtres adaptées durant lesquelles l’arbre peut supporter ou non certaines valeurs extrêmes.
Il nous faudrait compléter l’analyse avec les cartes associées aux indicateurs restants, en travaillant aussi les échelles colorimétriques en fonction des seuils phénologiques de l’olivier.
Idéalement, il serait intéressant de pouvoir mener une analyse multicritère à partir de l’ensemble des indicateurs, en proposant un indicateur global qui permette d’apprécier de potentielles aires biogéographiques compatibles pour l’olivier en Occitanie, et identifier si le Gers se démarque ou non.
Pour chaque indicateur mais aussi pour l’indicateur global multicritère, nous suggérons de travailler les formats pour faciliter la comparaison des scénarios entre eux :

- Sous forme d’un affichage multi-cartes sur la même page (tous les horizons TRACC sont présents sur la même page; voir l’exemple “Indicateur gel - ALL”)
  et/ou
- En créant un bouton permettant de faire défiler les scénarios les uns après les autres de manière dynamique.

Le but global serait de fournir un support le plus systémique possible concernant la compatibilité de l’Occitanie en combinant les divers indicateurs, mais aussi de proposer des formats dynamiques que des acteurs territoriaux peuvent s’approprier pour étudier la situation de compatibilité de l’olivier au regard du changement climatique.
