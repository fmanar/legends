import random

legends = ['Bloodhound', 'Gibraltar', 'Lifeline', 'Pathfinder', 'Wraith',
    'Bangalore', 'Caustic', 'Mirage', 'Octane', 'Wattson',
    'Crypto', 'Revnant', 'Loba', 'Rampart', 'Horizon']

legends.remove('Crypto')
random.shuffle(legends)
print(f'Random legends! {legends[0]}! {legends[1]}! {legends[2]}!')