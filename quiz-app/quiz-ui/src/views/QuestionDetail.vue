<template>
  <div class="question-detail">
    <div class="question-container">
      <h1 class="question-title">{{ question.title }}</h1>
      <p>{{ question.text }}</p>
      <ul>
        <li v-for="(answer, index) in question.possibleAnswers" :key="index">
          <input type="radio" :checked="answer.isCorrect" disabled /> {{ answer.text }}
        </li>
      </ul>
      <button class="edit-button" @click="editQuestion">Éditer</button>
      <button class="delete-button" @click="deleteQuestion">Supprimer</button>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'QuestionDetail',
  data() {
    return {
      question: null,
      questionId: this.$route.params.id
    };
  },
  created() {
    this.fetchQuestion();
  },
  methods: {
    async fetchQuestion() {
      try {
        const response = await QuizApiService.getQuestion(this.questionId);
        this.question = response.data;
      } catch (error) {
        console.error('Error fetching question:', error);
      }
    },
    editQuestion() {
      this.$router.push(`/question/edit/${this.questionId}`);
    },
    async deleteQuestion() {
      try {
        const response = await QuizApiService.deleteQuestion(this.questionId);
        if (response.status === 200) {
          this.$router.push('/admin');
        } else {
          console.error('Error deleting question:', response.data);
        }
      } catch (error) {
        console.error('Error deleting question:', error);
      }
    }
  }
};
</script>

<style scoped>
.question-detail {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  text-align: center;
}

.question-container {
  background: rgba(0, 0, 0, 0.7);
  padding: 2rem;
  border-radius: 10px;
}

.question-title {
  color: #ffdd57;
}

.edit-button,
.delete-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  margin: 0.5rem;
  cursor: pointer;
  border-radius: 5px;
}

.edit-button:hover,
.delete-button:hover {
  background-color: #0056b3;
}
</style>
