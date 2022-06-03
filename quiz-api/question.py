from asyncio.windows_events import NULL
import os
from re import A
import this
from winreg import QueryInfoKey
import flask
import json
import jwt_utils as jwtU

import questionclass
import random
import dbController as db
import quizinfo

#POST
def CreateQuestion(req):
	#Récupérer le token envoyé en paramètre
    token = req.headers.get('Authorization')
    if (token):
    #createQuestion
        try:
            postQuestion(req)
            quizinfo.updateDB("size","+")
            return {"ok": token},200
        except Exception as e: 
            print(e)
            #print("Exception thrown. x does not exist.")
            return '',401
    else: 
        return '', 401

#GET
def getQuestion(req, index):
    try:
        result = getQuestionsinfos(index)
        if(result != NULL):
            return result , 200
        else: 
            return '',404

    except Exception as e: 
        print(e)
        return '',404

#PUT
def updateQuestion(req, index):
    questionJSON = req.get_json()
    try:
        #ajout question vide
        index= int(index)
        question2 = deserializing(questionJSON)
        question2.title = str(question2.title).replace("'","''")
        question2.texte = str(question2.texte).replace("'","''")
        count = getCountQuestion()
        a = 0
        b = 0
        parcours = 0
        if ( index > question2.position):
            b = question2.position
            a = index
            parcours = -1
        else:
           a = index 
           b = question2.position
           parcours = 1
        for i in range(a, b, parcours):
            questionJSON = json.loads(getQuestionsinfos(i+ parcours))
            question = questionclass.Question(questionJSON['id'], questionJSON['position'], questionJSON['title'], questionJSON['text'], questionJSON['image'],questionJSON['possibleAnswers'])
            try:
                updateInDB(question, i)
            except Exception as e:
                print(e)
                return '', 404
        updateInDB(question2, question2.position)
        return '', 200
    except Exception as e:
            print(e)
            return '', 404

#DELETE
def deleteQuestion(req, index):
	#Récupérer le token envoyé en paramètre
    token = req.headers.get('Authorization')
    count = getCountQuestion()
    index = int(index)
    if (token):
        try:
            if (index == count):
                deleteInDB(req, index)
                quizinfo.updateDB("size","-")
            else:
                deleteInDB(req, index)
                for i in range (index, count):
                    questionJSON = json.loads(getQuestionsinfos(i+1))
                    question = questionclass.Question(questionJSON['id'], questionJSON['position'], questionJSON['title'], questionJSON['text'], questionJSON['image'],questionJSON['possibleAnswers'])
                    postDeleteInDB(question, i)
                quizinfo.updateDB("size","-")
            
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
        question = deserializing(questionJSON)
        #si on ajoute une nouvelle question
        if (question.position > (getCountQuestion())-1):
            print("add new")
            addQuestion(req, question)
        #si on insère
        else:
            question2 = deserializing(questionJSON, question.position )
            print("insert")
            insertQuestion(req, question2)
    except Exception as e: 
        print(e)
        return '',401

def addQuestion(req, question):
    title = str(question.title).replace("'","''")
    texte = str(question.texte).replace("'","''")
    cur = db.initDbConnection()
    query = (
        f"INSERT INTO QUESTIONS (ID, Position, Title, Texte, Image) VALUES"
        f"({question.id},{question.position },'{title}','{texte}', '{question.image}')"
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
    i = 1
    for reponse in question.reponses :
        reponse['text'] = reponse['text'].replace("'","''")
        query = (
        f"INSERT INTO REPONSES (text, isCorrect, posQuestion, position) VALUES"
        f"('{reponse['text']}','{reponse['isCorrect']}', {question.position}, {i})"
        )
        try:
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
        except Exception as e :
            print(e)
            cur.execute('rollback')
            return '',401
        i= i+1
    #in case of exception, rollback the transaction
    #cur.execute('rollback')
    print("end postQuestion")

#convert data from JSON to question class model
def deserializing(questionJSON, id =-1):
    print("deserializing")
    data = questionJSON
    #generate random ID
    if (id == -1):
        id = random.randint(1,100)
    
    title = data["title"]
    position = data["position"]
    texte = data["text"]
    image = data["image"]
    reponses = data["possibleAnswers"]
    question = questionclass.Question(id, position, title, texte, image, reponses)
    try : 
        #question.printAttribute()
        print("affect question ok")
    except Exception as e: 
        print(e)
        return NULL
    return question 

#convert data from SQL to question class model
def serializing(questionSQL):
    print("serializing")
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

def insertQuestion(req, question2):
    
    question2.title = str(question2.title).replace("'","''")
    question2.texte = str(question2.texte).replace("'","''")
    index = question2.position
    count = getCountQuestion()

    try:
        #ajout question vide
        question = questionclass.Question(0, count, "title", "text", "img",[])
        question.position += 1
        addQuestion(req, question)

        for i in range(count+1, index, -1):
            questionJSON = json.loads(getQuestionsinfos(i-1))
            question = questionclass.Question(questionJSON['id'], questionJSON['position'], questionJSON['title'], questionJSON['text'], questionJSON['image'],questionJSON['possibleAnswers'])
            try:
                updateInDB(question, i)
            except Exception as e:
                print(e)
                return '', 404
        updateInDB(question2, index)
        return '', 200
    except Exception as e:
            print(e)
            return '', 404

def getCountQuestion():
    try:
        cur = db.initDbConnection()
        cur.execute("begin")
        query = cur.execute (
            f"SELECT COUNT(*) FROM QUESTIONS"
        )
        count = query.fetchall()[0][0]
        cur.execute("commit")
        return count
    except Exception as e:
        print(e)
        return '',404

def getQuestionsinfos(index):

    reponse = NULL
    try:
        cur = db.initDbConnection()
        cur.execute("begin")
        #serializing(req)
        query = cur.execute(
            f"SELECT * FROM QUESTIONS where Position =="
            f"{index}"
        )
        reponse = serializing(query.fetchall())
        cur.execute("commit")
        try :
            cur = db.initDbConnection()
            cur.execute("begin")
            query = cur.execute(
                f"SELECT * FROM REPONSES where posQuestion =="
                f"{index}"
            )
            getReponse = query.fetchall()
            reponse = reponse.questionToJSON(getReponse)
            cur.execute("commit")
        except Exception as e: 
            print(e)
            return NULL
        return reponse
    except Exception as e: 
        print(e)
        return NULL

def postDeleteInDB(question, index):
    cur = db.initDbConnection()
    
    title = str(question.title).replace("'","''")
    texte = str(question.texte).replace("'","''")
    query = (
    f"UPDATE QUESTIONS "
    f"SET Title = '{title}',"
    f" Texte = '{texte}',"
    f" Image = '{question.image}',"
    f" Position = '{index}',"
    f" ID = '{question.id}'"
    f" WHERE Position= '{index+1}'"
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
        f"WHERE posQuestion = {index+1}"
        )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e :
        print(e)

    i = 1
    for reponse in question.reponses:
        reponse['text'] = reponse['text'].replace("'","''")
        query = (
            f"INSERT INTO REPONSES (text, isCorrect, posQuestion, position) VALUES"
            f"('{reponse['text']}','{reponse['isCorrect']}', {index},{i})"
            )
        try:
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
        except Exception as e :
            print(e)

def updateInDB(question, index):
    cur = db.initDbConnection()
    
    title = str(question.title).replace("'","''")
    texte = str(question.texte).replace("'","''")
    #update questions
    #print(question.printAttribute())
    query = (
    f"UPDATE QUESTIONS "
    f"SET Title = '{title}',"
    f" Texte = '{texte}',"
    f" Image = '{question.image}',"
    f" Position = '{index}',"
    f" ID = '{question.id}'"
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
        f"WHERE posQuestion = {index}"
        )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e :
        print(e)
    i=1
    for reponse in question.reponses:
        reponse['text'] = reponse['text'].replace("'","''")
        query = (
            f"INSERT INTO REPONSES (text, isCorrect, posQuestion, position) VALUES"
            f"('{reponse['text']}','{reponse['isCorrect']}', {index},{i})"
            )
        i = i+1
        try:
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
        except Exception as e :
            print(e)

def deleteInDB(req, index):

    cur = db.initDbConnection()
    query = (
    f"DELETE FROM QUESTIONS "
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
        f"DELETE FROM REPONSES WHERE posQuestion = "
        f"{index}"
        )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e :
        print(e)
        cur.execute('rollback')
        return '',401

def getRightAnswer(index):
    cur = db.initDbConnection()
    
    try:
        cur.execute("begin")
        query = cur.execute(
    f"SELECT position FROM REPONSES WHERE posQuestion = {index} AND isCorrect = \"True\""
    )
        score = query.fetchall()
        cur.execute("commit")
        return score[0][0]
    except Exception as e:
        print(e)
        return '', 401