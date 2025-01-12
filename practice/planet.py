def myplanet(pos):
    if pos < 1 or pos > 9:
        return 'Invalid position'
    else:
        d = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune', 9: 'Pluto'}
        return d[pos]

print(myplanet(3))