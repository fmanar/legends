"""Random Legend Picker

This script chooses random legends for a whole squad. Player names can be
supplied as command line arguments, and legends will be matched to them.

Invocation:
    python legends.py [PLAYER]...

Example:
    Without arguments the script picks three legends:

        $ python legends.py
        Random legends! Loba! Horizon! Octane!
        
    With arguments the script picks legends for each player supplied:

        $ python legends.py Frodo Sam
        Random legends!
        Frodo plays Mirage!
        Sam plays Gibraltar!

Notes:
    If Skyler is playing, Crypto is removed from the legend pool.
    

"""
import random
import sys

legends = ['Bloodhound', 'Gibraltar', 'Lifeline', 'Pathfinder', 'Wraith',
    'Bangalore', 'Caustic', 'Mirage', 'Octane', 'Wattson',
    'Crypto', 'Revnant', 'Loba', 'Rampart', 'Horizon']

if 'Skyler' in sys.argv:
    legends.remove('Crypto')

random.shuffle(legends)

if len(sys.argv) > 1:
    print('Random legends!')
    for player, legend in zip(sys.argv[1:], legends):
        print(f'{player} plays {legend}!')
else:
    print(f'Random legends! {legends[0]}! {legends[1]}! {legends[2]}!')
