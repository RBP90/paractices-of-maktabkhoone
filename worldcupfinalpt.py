teams = [
    {'name': 'Iran', 'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
    {'name': 'Spain', 'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
    {'name': 'Portugal', 'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0},
    {'name': 'Morocco', 'wins': 0, 'loses': 0, 'draws': 0, 'goal difference': 0, 'points': 0}
]

def natije(team1_index, team2_index, team1_score, team2_score):
    team1 = teams[team1_index]
    team2 = teams[team2_index]
    
    if team1_score > team2_score:
        team1['points'] += 3
        team1['goal difference'] += (team1_score - team2_score)
        team1['wins'] += 1
        team2['goal difference'] += (team2_score - team1_score)
        team2['loses'] += 1
    elif team1_score == team2_score:
        team1['points'] += 1
        team1['draws'] += 1
        team2['points'] += 1
        team2['draws'] += 1
    else:
        team2['points'] += 3
        team2['goal difference'] += (team2_score - team1_score)
        team2['wins'] += 1
        team1['goal difference'] += (team1_score - team2_score)
        team1['loses'] += 1

for i in range(4):
    for j in range(i+1, 4):
        #print(f"Enter score for {teams[i]['name']} vs {teams[j]['name']}:")
        score_input = input().strip().replace(" ","-")
        team1_score, team2_score = map(int, score_input.split("-"))
        #print (i , j , team1_score , team2_score)
        natije(i, j, team1_score, team2_score)

def sort_teams(team):
    return (-team['points'], -team['wins'], team['name'])

sorted_teams = sorted(teams, key=sort_teams)

for team in sorted_teams:
    print(f"{team['name']}  wins:{team['wins']} , loses:{team['loses']} , draws:{team['draws']} , goal difference:{team['goal difference']} , points:{team['points']}")

