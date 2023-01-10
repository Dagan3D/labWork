import csv
from functools import total_ordering


@total_ordering
class Player:
    players = set()

    def __init__(self, name: str, wins: int, point: int):
        self.name = name
        self.wins = wins
        self.point = point
        self.players.add(self.name)

    def __init__(self, player_list: list):
        self.name = player_list[0]
        self.wins = int(player_list[1])
        self.point = int(player_list[2])
        self.players.add(self)

    def __lt__(self, obj):
        if self.wins == obj.wins:
            return self.point < obj.point
        else:
            return self.wins < obj.wins

    def __gt__(self, obj):
        if self.wins == obj.wins:
            return self.point > obj.point
        else:
            return self.wins > obj.wins

    def __le__(self, obj):
        if self.wins == obj.wins:
            return self.point <= obj.point
        else:
            return self.wins <= obj.wins

    def __ge__(self, obj):
        if self.wins == obj.wins:
            return self.point >= obj.point
        else:
            return self.wins >= obj.wins

    def __str__(self):
        return str(self.name) + ": " + str(self.wins) + "/" + str(self.point)

    def __repr__(self):
        return str(self.name) + ": " + str(self.wins) + "/" + str(self.point)


with open('players.csv', "r", newline='', encoding="utf8") as File:
    reader = csv.reader(File, delimiter=';')
    next(reader)
    for row in reader:
        Player(row)

win_list = sorted(Player.players, reverse=True)
with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=';')
    column_name = ["Спортсмен", "Место"]
    writer.writerow(column_name)
    for i, player in enumerate(win_list):
        writer.writerow([player.name, i+1])
