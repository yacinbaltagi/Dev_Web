<template>
  <div class="admin">
    <div class="admin-container">
      <h1 class="admin-title">Liste des Questions</h1>
      <button class="logout-button" @click="logout">Déconnexion</button>
      <button class="create-question-button" @click="createQuestion">Créer une question</button>
      <ul>
        <li v-for="question in questions" :key="question.id">
          <router-link :to="'/question/' + question.id">{{ question.title }}</router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'QuestionsManager',
  data() {
    return {
      questions: []
    };
  },
  created() {
    this.fetchQuestions();
  },
  methods: {
    async fetchQuestions() {
      try {
        const response = await QuizApiService.getQuestions();
        this.questions = response.data;
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
    },
    logout() {
      localStorage.removeItem('authToken');
      this.$router.push('/login');
    },
    createQuestion() {
      this.$router.push('/new-question');
    }
  }
};
</script>

<style scoped>
.admin {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  text-align: center;
}

.admin-container {
  background: rgba(0, 0, 0, 0.7);
  padding: 2rem;
  border-radius: 10px;
}

.admin-title {
  color: #ffdd57;
}

.logout-button,
.create-question-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  margin: 0.5rem;
  cursor: pointer;
  border-radius: 5px;
}

.logout-button:hover,
.create-question-button:hover {
  background-color: #0056b3;
}
</style>
