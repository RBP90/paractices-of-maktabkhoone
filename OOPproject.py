import random

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

class Footballist(Person):
    def __init__(self, name):
        super().__init__(name)
        self.team = None

players_names = [
    'hossein', 'maziar', 'akbar', 'nima', 'mehdi', 'farhad', 'mohammad', 'khashayar',
    'milad', 'mostafa', 'amin', 'saeid', 'pouya', 'pouria', 'reza', 'ali', 'behzad',
    'soheil', 'behrooz', 'shahrooz', 'saman', 'mohsen'
]

players = [Footballist(name) for name in players_names]

team_a = set(random.sample(players, 11))
team_b = set(players) - team_a

for player in players:
    if player in team_a:
        player.team = "A"
    else:
        player.team = "B"

for player in players:
    print(f"{player.name} {player.team}")