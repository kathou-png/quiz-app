from flask import Flask, request
import login, question, participation, quizinfo

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return quizinfo.getInfo(request)

@app.route('/login', methods=['POST'])
def LoginTest():
	return login.PostLogin(request)

@app.route('/questions', methods=['POST'])
def Question():
	return question.CreateQuestion(request)

@app.route('/questions/<index>', methods=['GET'])
def getQuestion(index):
	return question.getQuestion(request, index)

@app.route('/questions/<index>', methods=['PUT'])
def updateQuestion(index):
	return question.updateQuestion(request, index)

@app.route('/questions/<index>', methods=['DELETE'])
def deleteQuestion(index):
	return question.deleteQuestion(request, index)

@app.route('/participations', methods=['POST'])
def addParticipation():
	return participation.addParticipation(request)

@app.route('/participations', methods=['DELETE'])
def removeParticipation():
	return participation.removeParticipation(request)

if __name__ == "__main__":
    app.run(ssl_context='adhoc')