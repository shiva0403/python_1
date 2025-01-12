
def invert(input_map):
    output_map = {}
    for key in input_map:
        output_map[input_map[key]] = key
    return output_map

d = {1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune', 9: 'Pluto'}
print(d)
print(invert(d))