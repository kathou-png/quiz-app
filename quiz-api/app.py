from flask import Flask, request
import login, question

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

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
	print(request)
	return question.deleteQuestion(request, index)

if __name__ == "__main__":
    app.run(ssl_context='adhoc')