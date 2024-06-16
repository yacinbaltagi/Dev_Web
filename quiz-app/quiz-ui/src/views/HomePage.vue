<template>
  <div class="home">
    <div class="quiz-container">
      <h1 class="quiz-title">Welcome to the Quiz!</h1>
      <p>Top Scores</p>
      <button class="start-quiz-button" @click="goToEnterName">Démarrer le quiz !</button>
      <div v-if="quizInfo">
        <p>Number of Questions: {{ quizInfo.size }}</p>
        <p>Top Scores: {{ quizInfo.scores.join(', ') }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'HomePage',
  data() {
    return {
      quizInfo: null
    };
  },
  methods: {
    async fetchQuizInfo() {
      try {
        const { data } = await QuizApiService.getQuizInfo();
        this.quizInfo = data;
      } catch (error) {
        console.error('Error fetching quiz info:', error);
      }
    },
    goToEnterName() {
      this.$router.push({ name: 'EnterName' });
    }
  },
  created() {
    this.fetchQuizInfo();
  }
}
</script>

<style scoped>
.home {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  text-align: center;
  background-image: url('../assets/background.jpg');
  background-size: cover;
  background-position: center;
}

.quiz-container {
  background: rgba(0, 0, 0, 0.7);
  padding: 2rem;
  border-radius: 10px;
}

.quiz-title {
  color: #ffdd57;
  /* Modifier cette couleur selon tes besoins */
}

.start-quiz-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  margin-top: 1rem;
  cursor: pointer;
  border-radius: 5px;
}

.start-quiz-button:hover {
  background-color: #0056b3;
}
</style>
