import random

groceryList = {
    'high grade flour': 9.42,
    'sugar': 5.67, 
    'instant yeast': 3.25, 
    'salt': 13.40,
    'water': 7.50,
    'oil': 10.30
}

random_key = random.choice(list(groceryList.keys()))
if groceryList[random_key] > 10:
    print(f'{random_key} is only gonna be 10$ today!')
    groceryList[random_key] = 10

print('Shopping list:')
for item in groceryList:
    if item is groceryList['water']:
        item.value *= 5
    print(f'{item}: {groceryList[item]}')

print(len('blood-oxygenation-level-dependent functional magnetic resonance imaging'))

