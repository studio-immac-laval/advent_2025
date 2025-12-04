import pyxel
from time import time, strftime, localtime

pyxel.init(128, 128)

units = ["0", "9", "8", "7", "6", "5", "4", "3", "2", "1"] 
tens = ["0", "5", "4", "3", "2", "1"] 
tensLimited = ["0", "2", "1", "0", "2", "1"] 

initial = localtime()

delta = [
    18 + ((initial.tm_hour - initial.tm_hour % 10) // 10 * 6), 
    31 + ((initial.tm_hour % 10) * 6) % 60 , 
    18 + ((initial.tm_min - initial.tm_min % 10) // 10 * 6), 
    31 + ((initial.tm_min % 10) * 6) % 60 , 
    18 + ((initial.tm_sec - initial.tm_sec % 10) // 10 * 6), 
    31 + ((initial.tm_sec % 10) * 6) % 60
]
print((initial.tm_min * 1800) + (initial.tm_sec * 30))
def update() :
    global delta, initial

    # Dizaines des heures
    if 1079988 < (pyxel.frame_count + (initial.tm_hour % 10 * 108000) + (initial.tm_min * 1800) + (initial.tm_sec * 30)) % 1080000 < 1079995 :
        delta[0] += 1

    # Unités des heures
    if 107988 < (pyxel.frame_count + (initial.tm_min * 1800) + (initial.tm_sec * 30)) % 108000 < 107995 :
        delta[1] += 1

    # Dizaines des minutes
    if 17988 < (pyxel.frame_count + (initial.tm_min % 10 * 1800) + (initial.tm_sec * 30)) % 18000 < 17995 :
        delta[2] += 1

    # Unités des minutes
    if 1788 < (pyxel.frame_count + (initial.tm_sec * 30)) % 1800 < 1795 :
        delta[3] += 1
    
    # Dizaine des secondes, on démarre un peu avant l'arrivée du 0
    if 288 < (pyxel.frame_count + (initial.tm_sec % 10 * 30)) % 300 < 295 :
        delta[4] += 1
    
    # Unités secondes, ça défile en continu
    if pyxel.frame_count % 5 == 0 :
        delta[5] += 1

def draw() :
    global units, tens, tensLimited, delta, initial

    pyxel.cls(0)
    
    # Ligne du milieu
    pyxel.rect(0, 60, 128, 7, 8)
    
    # Dizaine des heures
    for i in range(6) :
        pyxel.text(48, 43 + (i * 6 + delta[0]) % 36, tensLimited[i], 7)

    # Unités des heures
    for i in range(10) :
        pyxel.text(53, 30 + (i * 6 + delta[1]) % 60, units[i], 7)
    
    # Dizaine des minutes
    for i in range(6) :
        pyxel.text(59, 43 + (i * 6 + delta[2]) % 36, tens[i], 7)

    # Unités des minutes
    for i in range(10) :
        pyxel.text(64, 30 + (i * 6 + delta[3]) % 60, units[i], 7)
    
    # Dizaine des secondes
    for i in range(6) :
        pyxel.text(70, 43 + (i * 6 + delta[4]) % 36, tens[i], 7)
    
    # Unités des secondes
    for i in range(10) :
        pyxel.text(75, 31 + (i * 6 + delta[5]) % 60, units[i], 7)
    
    # Masquage
    pyxel.rectb(46, 47, 34, 33, 8)
    pyxel.rect(0, 0, 128, 47, 0)
    pyxel.rect(0, 80, 128, 47, 0)

pyxel.run(update, draw)