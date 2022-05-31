from asyncio.windows_events import NULL
import os
import this
from winreg import QueryInfoKey
import flask
import json
import jwt_utils as jwtU
import sqlite3
import questionclass
import random

#used to interact with db
def initDbConnection():
    db_conn=sqlite3.connect("..\\bdd.db")
    db_conn.isolation_level = None
    #créée le curseur
    cur = db_conn.cursor()
    return cur

#POST
def CreateQuestion(req):
	#Récupérer le token envoyé en paramètre
    token = req.headers.get('Authorization')
    if (token):
    #createQuestion
        try:
            postQuestion(req)
        except Exception as e: 
            print(e)
            #print("Exception thrown. x does not exist.")
            return '',401
        finally:
            return {"ok": token},200
    else: 
        return '', 401

#GET
def getQuestion(req, index):
    reponse = NULL
    try:
        cur = initDbConnection()
        cur.execute("begin")
        #serializing(req)
        query = cur.execute(
            f"SELECT * FROM QUESTIONS where Position =="
            f"{index}"
        )
        reponse = serializing(query.fetchall())
        if reponse == NULL :
            print("return 404")
            return '', 404
        else:
            cur.execute("commit")
            try :
                cur = initDbConnection()
                cur.execute("begin")
                query = cur.execute(
                    f"SELECT * FROM REPONSES where idQuestion =="
                    f"{reponse.id}"
                )
                getReponse = query.fetchall()
                reponse = reponse.questionToJSON(getReponse)
                cur.execute("commit")
            except Exception as e: 
                print(e)
                return '', 404
            return reponse , 200
    except Exception as e: 
        print(e)
        return '',404

#PUT
def updateQuestion(req, index):
    #Récupérer le token envoyé en paramètre
    token = req.headers.get('Authorization')
    if (token):
    #createQuestion
        try:
            return updateInDB(req, index)
        except Exception as e: 
            print(e)
            #print("Exception thrown. x does not exist.")
            return '',404
    else: 
        return '', 404

#DELETE
def deleteQuestion(req, index):
	#Récupérer le token envoyé en paramètre
    token = req.headers.get('Authorization')
    if (token):
        try:
            deleteInDB(req, index)
            return {"delete status": "success"},204
        except Exception as e : 
            print(e)
            return '', 401
    else:
        return '', 401
#Enregistre la question 
def postQuestion(req):
    questionJSON = req.get_json()
    try:
        cur = initDbConnection()

        question = deserializing(questionJSON)
        print("post question")
        query = (
        f"INSERT INTO QUESTIONS (ID, Position, Title, Texte, Image) VALUES"
        f"({question.id},{question.position},'{question.title}','{question.texte}', '{question.image}')"
        )
        try:
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
        except Exception as e :
            print(e)
            cur.execute('rollback')
            return '',401

        #reponses in DB

        for reponse in question.reponses :
            print(reponse)
            query = (
            f"INSERT INTO REPONSES (text, isCorrect, IDQuestion) VALUES"
            f"('{reponse['text']}','{reponse['isCorrect']}', {question.id})"
            )
            try:
                cur.execute("begin")
                cur.execute(query)
                cur.execute("commit")
            except Exception as e :
                print(e)
                cur.execute('rollback')
                return '',401
        #in case of exception, rollback the transaction
        #cur.execute('rollback')
        print("end postQuestion")

    except Exception as e: 
        print(e)
        return '',401

#convert data from JSON to question class model
def deserializing(questionJSON):
    print("unserializing")
    data = questionJSON
    #generate random ID
    id = random.randint(1,100)
    position = data["position"]
    title = data["title"]
    texte = data["text"]
    image = data["image"]
    reponses = data["possibleAnswers"]
    question = questionclass.Question(id, position, title, texte, image, reponses)
    try : 
        question.printAttribute()
        print("affect question ok")
    except Exception as e: 
        print(e)
        return NULL
    return question 

#convert data from SQL to question class model
def serializing(questionSQL):
    print("serializing")
    print(questionSQL)
    if(len(questionSQL) > 0):
        #ID
        id = (questionSQL[0][0])
        #position
        position = (questionSQL[0][1])
        #title
        title = (questionSQL[0][2])
        #texte
        texte = (questionSQL[0][3])
        #reponses
        image = (questionSQL[0][4])
        
        return questionclass.Question(id, position, title,texte, image, NULL)
    else:
        print("return null")
        return NULL

def updateInDB(req, index):
    cur = initDbConnection()
    questionJSON = req.get_json()
    question = deserializing(questionJSON)
    #update questions
    print(question.printAttribute())
    query = (
    f"UPDATE QUESTIONS "
    f"SET Title = '{question.title}',"
    f" Texte = '{question.texte}',"
    f" Image = '{question.image}'"
    f"WHERE Position = "
    f"{index};"
    )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e:
        print(e)
        return '', 404
    
    #update reponses
    
    query = (
        f"DELETE FROM REPONSES "
        f"WHERE idQuestion = {question.id}"
        )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e :
        print(e)
        cur.execute('rollback')
        return '',401
    for reponse in question.reponses:
        query = (
            f"INSERT INTO REPONSES (text, isCorrect, IDQuestion) VALUES"
            f"('{reponse['text']}','{reponse['isCorrect']}', {question.id})"
            )
        try:
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
        except Exception as e :
            print(e)
            cur.execute('rollback')
            return '',401
    return '', 200

def deleteInDB(req, index):
    print("deleteinDB")
    cur = initDbConnection()
    questionJSON = req.get_json()
    question = deserializing(questionJSON)
    #update questions
    print(question.printAttribute())
    query = (
    f"DELETE QUESTIONS "
    f"WHERE Position = "
    f"{index}"
    )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e:
        print(e)
        return '', 401
    
    #update reponses
    
    query = (
        f"DELETE FROM REPONSES WHERE Position = "
        f"{question.id}"
        )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e :
        print(e)
        cur.execute('rollback')
        return '',401