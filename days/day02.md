# Jour 2

![Défi](../img/day02.gif)

## Défi

Afficher "Vive le vent..." **mot** par **mot** en changeant de **couleur** à chaque fois.

## Démarrer

Encore une fois on compte les itérations de `update()/draw()`.

Les mots sont séparés par des espaces. On peut utiliser la fonction [`str.split(sep)`](https://docs.python.org/3.6/library/stdtypes.html#str.split) qui "explose" une chaîne de caractères délimitée par un séparateur en un tableau de sous-chaînes.

```py
song = [
    "Vive le vent,",
    "Vive le vent,",
    "Vive le vent d'hiver",
    "Qui s'en va sifflant, soufflant,",
    "Dans les grands sapins verts...",
    "Hey !",
    " ",
    "Vive le temps,",
    "Vive le temps,",
    "Vive le temps d'hiver",
    "Boule de neige et jour de l'an,",
    "Et bonne annee grand-mere !"
]
# On éclate chaque ligne en un tableau de mots
songWords = list()
for i in range(len(song)) :
    songWords.append(song[i].split(" "))

print(songWords)
```

Ce qui donne :

```
[['Vive', 'le', 'vent,'], ['Vive', 'le', 'vent,'], ['Vive', 'le', 'vent', "d'hiver"], ['Qui', "s'en", 'va', 'sifflant,', 'soufflant,'], ['Dans', 'les', 'grands', 'sapins', 'verts...'], ['Hey', '!'], ['', ''], ['Vive', 'le', 'temps,'], ['Vive', 'le', 'temps,'], ['Vive', 'le', 'temps', "d'hiver"], ['Boule', 'de', 'neige', 'et', 'jour', 'de', "l'an,"], ['Et', 'bonne', 'annee', 'grand-mere', '!']]
```

Il ne reste "plus qu'à" afficher le texte 😉

## Une solution

🐍 [Voir le fichier](day02.py)

```py
import pyxel

pyxel.init(128, 128)

song = [
    "Vive le vent,",
    "Vive le vent,",
    "Vive le vent d'hiver",
    "Qui s'en va sifflant, soufflant,",
    "Dans les grands sapins verts...",
    "Hey !",
    " ",
    "Vive le temps,",
    "Vive le temps,",
    "Vive le temps d'hiver",
    "Boule de neige et jour de l'an,",
    "Et bonne annee grand-mere !"
]
# On éclate chaque ligne en un tableau de mots
songWords = list()
for i in range(len(song)) :
    songWords.append(song[i].split(" "))

steps = 0

def update() :
    global steps

    # On compte les itérations
    steps += 1 

def draw() :
    global steps, songWords

    # On efface l'écran
    pyxel.cls(2)

    # Pour ralentir l'affichage, on n'affiche 
    # un mot supplémentaire qu'une itération sur 10 !
    remainingWords = steps // 10

    line = 0
    color = 0
    
    while remainingWords > 0 and line < len(songWords) :
        prevWordLength = 0

        # On affiche chaque ligne mot à mot (tant qu'il reste des mots)
        for i in range(len(songWords[line]) if len(songWords[line]) < remainingWords else remainingWords) :
            # Chaque caractère occupe 4 pixels de large
            pyxel.text(1 + prevWordLength * 4, 20 + 6 * line, songWords[line][i], color)
            
            remainingWords -= 1
            prevWordLength += len(songWords[line][i]) + 1       # + 1 espace
            
            # On change la couleur
            color += 1
            if color == 16 :
                color = 0
            if color == 2 :
                color += 1

        line += 1

pyxel.run(update, draw)
```