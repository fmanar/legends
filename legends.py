# Take a look at README.md for more instructions

import random
import sys

legends = [
    'Bloodhound', 'Gibraltar', 'Lifeline', 'Pathfinder', 'Wraith', 'Bangalore', 
    'Caustic', 'Mirage', 'Octane', 'Wattson', 'Crypto', 'Revnant', 
    'Loba', 'Rampart', 'Horizon', 'Fuse', 'Valkyrie',
    ]

if 'Skyler' in sys.argv:
    legends.remove('Crypto')

random.shuffle(legends)

if len(sys.argv) > 1:
    print('Random legends!')
    for player, legend in zip(sys.argv[1:], legends):
        print(f'{player} plays {legend}!')
else:
    print(f'Random legends! {legends[0]}! {legends[1]}! {legends[2]}!')
