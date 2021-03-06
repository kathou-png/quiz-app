import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json"
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  async getQuizInfo() {
    return this.call("get", "quiz-info")
  },
  async getQuestion(position) {
    return this.call("get", "questions/" + position.toString())
  },
  async postScore(player){
    return this.call("post", "participations", player)
  },
  async loginAdmin(password){
    return this.call("post", "login", password)
  },
  async deleteQuestion(index, token){
    return this.call("delete", "questions/" + index.toString(), null, token)
  },
  async deleteParticipation(token){
    return this.call("delete", "participations", null, token );
  },
  async createQuestion(token, body){
    return this.call("post", "questions", body, token);
  }
};