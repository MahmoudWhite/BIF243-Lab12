with open("scores.txt","r") as file:
    count=0
    for lines in file:
        field=lines.rstrip().split(",")
        name=field[0]
        score=field[1]
        try:
            score=int(float(score))
            count+=1
        except ValueError:
            score=score
        if name == "Karim":
            print(score)
    print(count)
    try:
        with open("scores.txt","r") as filee:
            filee.readlines()
    except FileNotFoundError:
        print("File not found.")
scores={}
with open("scores.txt","r") as files:
    for row in files:
        field=row.split(",")
        contastant=field[0]
        grade=field[1]  
        try:
            grade=int(float(grade))
            count+=1
        except ValueError:
            grade=grade
        if field[0] == "Maya":
            scores[contastant]=88
        elif contastant != "Nour" and (type(grade) == int or type(grade)==float):
            scores[contastant]=int(grade)
with open("scores.txt","w") as filess:
    for i in scores:
        filess.write(i + "," + str(scores[i]) + "\n")
        with open ("pass.txt","a") as filesss:
            if scores[i] >= 60:
                filesss.write(i)
