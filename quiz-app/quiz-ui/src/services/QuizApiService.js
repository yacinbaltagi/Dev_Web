import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
        return { status: error.response.status, data: error.response.data };
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestions() {
    return this.call("get", "questions");
  },
  getQuestion(id) {
    return this.call("get", `questions/${id}`);
  },
  addQuestion(questionData) {
    const token = localStorage.getItem('authToken');
    return this.call("post", "questions", questionData, token);
  },
  updateQuestion(id, questionData) {
    const token = localStorage.getItem('authToken');
    return this.call("put", `questions/${id}`, questionData, token);
  },
  deleteQuestion(id) {
    const token = localStorage.getItem('authToken');
    return this.call("delete", `questions/${id}`, null, token);
  },
  login(password) {
    return this.call("post", "login", { password });
  }
};
