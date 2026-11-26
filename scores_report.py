with open("scores.txt","r") as file:
    count=0
    for contastant in file:
        field=contastant.split(",")
        name=field[0]
        score=field[1]
        if type.score == int or float:
            score=int(score)
            count+=1
        else:
            score=score
        if name == "Karim":
            print(score)
    try:
        with open("scores.txt") as file:
            file.readlines()
    except FileNotFoundError:
        print("File not found.")
scores={}
with open("scores.txt","w") as file:
    for row in file:
        field=contastant.split(",")
        contastant=field[0]
        grade=field[1]      
        if field[0] == "Maya":
            scores[contastant]=88
        elif contastant != "Nour" and type.grade == int or float:
            scores[contastant]=int(grade)
    for i in scores:
        file.write(i,scores[i],sep=",")
        with open ("pass.txt","w") as files:
            if scores[i] >60:
                files.write(i,scores[i],sep=",")
