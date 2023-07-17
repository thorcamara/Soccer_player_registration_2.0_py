team = list()
player = dict()
matches = list()

while True:
    player.clear()
    player['Name'] = str(input('Name of the player: '))
    total = int(input(f'How many matches {player["Name"]} played? '))
    matches.clear()
    for c in range(0, total):
        matches.append(int(input(f'     How many goals in match {c+1}? ')))
    player['Goals'] = matches[:]
    player['Total'] = sum(matches)
    team.append(player.copy())
    while True:
        answer = str(input('Do you want to continue? [\033[1;32mY\033[m/\033[1;31mN\033[m] '))
        if answer in 'YN':
            break
        print('ERROR! Answer only Y or N.')
    if answer == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    search = int(input('Show data from which player? (\033[1;31m999\033[m stops) '))
    if search == 999:
        break
    if search >= len(team):
        print(f'ERRO! Player with code {search} DO NOT EXIST!')
    else:
        print(f' ----- SURVEY OF PLAYER \033[1;32m{team[search]["Name"]}\033[m -----')
        for i, g in enumerate(team[search]['Goals']):
            print(f'    In game \033[1;32m{i+1}\033[m made \033[1;32m{g}\033[m goals.')
        print('-' * 40)
print('\033[1;31m<< WELCOME >>\033[m')
