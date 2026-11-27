def points_by_team(scores, teams):
    result={}
    for i in teams:
        result[i]=0
        for x in teams[i]:
            result[i]+=scores[x]
    return result
teams={}
scores={}
with open("players.txt","r") as file:
    for line in file:
        field=line.rstrip().split(" ")
        scores[field[0]]=int(field[1])
        if field[2] in teams:
            teams[field[2]].append(field[0])
        else:
            teams[field[2]]=[field[0]]
print("Scores:",scores)
print("Teams:",teams)
print("Points by team:",points_by_team(scores, teams))
