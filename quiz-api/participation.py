 
import dbController as db
import random
import json
import question as Question
from asyncio.windows_events import NULL

def addParticipation(req):
    participationJSON = req.get_json()
    try:
        cur = db.initDbConnection()
        cur.execute("begin")
        playerName = participationJSON["playerName"]
        score = getScore(participationJSON["answers"])
        id = random.randint(1,100)
        if (score != -1):
            query = cur.execute(
            f"INSERT INTO PARTICIPATIONS (playerName, id, score) VALUES"
            f"('{playerName}', {id}, {score})"
            )
            cur.execute("commit")
            return {"playerName": playerName, "score": score}, 200
        else:
            return '', 400
    except Exception as e:
        print(e)
        return '', 401

def removeParticipation(req):
    try:
        cur = db.initDbConnection()
        cur.execute("begin")
        query = cur.execute(
        f"DELETE FROM PARTICIPATIONS;"
        )
        cur.execute("commit")
        return '', 204
    except Exception as e:
        print(e)
        return '', 401

def getScore(data):
    score = 0
    print("calculate score")
    print(data)
    try:
        count = Question.getCountQuestion()
        if (len(data) != count):
            return -1
        #update here
        else:
            for i in range (1,count+1):
                if (data[i-1] == int(Question.getRightAnswer(i))):
                    score = score +1
        return score
    except Exception as e:
        print(e)

    
