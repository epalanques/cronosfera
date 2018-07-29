Aquest és un projecte amb el que traçar l'història utilitzant el sistema de classes amb Python.

Originalment l'estic pensant per fer l'història la Terra, pero es podria utilizar també a escala humana.

El sistema d'entitats l'imagino així:


Tens la línia del temps. En aquesta línia tens events puntuals (ex: separació de Pangea) i events que duren (ex: Pangea).

Quan busques info has de poder situar-te dins de la línea temporal. Això vol dir que selecciones un any i has de poder
veure com és el món en el any que has agafat. Així, en èpoques de la terra has de poder saber quin és l'estat dels continents i
dels animals (a part de més altre coses que ara no se m'ocurreixen).

La busqueda d'informació s'ha de poder fer al nivell de zoom que es vulgui: tant en un any complet, com en una era, època,
etc.
S'entén que a mesura que es tira enrere, els events puntuals es tornen duraders, ja que no es sap exactament l'any, ni
el sigle sinó més aviat es te una precisió de millons d'anys. Així, els events puntuals es tornen duraders en periode aprox
de ±10% (arbitrari). No obstant, l'usuari ha de poder fixar-se en un any concret i obtenir una imatge del món, així que
obtindrá com a info: "S'está format Pangea, els animals són".

La búsqueda d'informació es fa en 3 dimensions: geografia, biologia i temps.
L'usuari pot seleccionar una o dos dimensions i veure com están les demés. Així, per exemple, pot seleccionar un any/era
i mirar com era la geografia (supercontinents, etc) i biologia (dinosaures, etc). O bé, seleccionar una era i geografia
i veure quins eren els animals en aquell moment en aquella zona (Espanya - 10.000 anys: ossos).
Cada dimensió te nivells de zoom i l'usuari pot buscar en el nivell de zoom que vulgui. Els nivells de zoom són:
Les èpoques del temps són:

TEMPS
- Eons: Les grupacions més grans en la història de la terra
    - Eras: contingudes com a atribut de l'eon
        - Periodes: continguts com a atribut de les eres
            - Época: continguda com a atrubut dels periodes
                - Edat: continguda com a atribut de la Època

Event temporal: Un any és un argument que entra un usuari com a input.

BIOLOGIA

- Dominio
    - Reino
        -Filo
            - Clase
                -Orden
                    -Familia
                        -Género
                            - Especie


GEOGRAFÍA

- (Super)continente
    - Accidente geográfico
    - Zona política aproximada actual