import dbController as db

def getInfo(req):
    try:
        score = getScores()
        size = getInfoDB("QUESTIONS")
        return {"size": size, "scores": score}, 200
    except Exception as e: 
        print(e)
        return '',401


def getInfoDB(info):
    try:
        cur = db.initDbConnection()
        cur.execute("begin")
        #serializing(req)
        query = cur.execute(
            f"SELECT COUNT(*) FROM {info}"
        )
        reponse = query.fetchall()[0][0]
        cur.execute("commit")
        return reponse
       
    except Exception as e: 
        print(e)
        return 0

def getScores():
    try:
        cur = db.initDbConnection()
        cur.execute("begin")
        #serializing(req)
        query = cur.execute(
            f"SELECT * FROM PARTICIPATIONS ORDER BY score DESC"
        )
        scores = query.fetchall()
        scoredict = {}
        dict_reponses = []
        for score in scores :
            dict_reponses.append({'playerName': str(score[0]),'score': score[2]})
      
        cur.execute("commit")
        return dict_reponses

    except Exception as e: 
        print(e)
        return 0


def updateDB(info, sign):
    try:
            cur = db.initDbConnection()
            cur.execute("begin")
            #serializing(req)
            query = cur.execute(
                f"UPDATE quizInfo SET {info} = {info} {sign} 1"
            )
            cur.execute("commit")
        
    except Exception as e: 
        print(e)