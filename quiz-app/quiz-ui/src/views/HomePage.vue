<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from "@/services/QuizApiService";

const quizInfo = ref({ size: 0, scores: [] });

onMounted(async () => {
  try {
    const response = await quizApiService.getQuizInfo();
    if (response && response.data) {
      quizInfo.value = response.data;
    }
  } catch (error) {
    console.error("Error fetching quiz info:", error);
  }
});
</script>

<template>
  <div class="home-container">
    <h1 class="title">Welcome to the Quiz!</h1>
    <p class="question-count">Total Questions: {{ quizInfo.size }}</p>
    <div class="scores-container">
      <h2 class="scores-title">Top Scores</h2>
      <div v-for="scoreEntry in quizInfo.scores" v-bind:key="scoreEntry.date" class="score-entry">
        <span class="player-name">{{ scoreEntry.playerName }}</span> - <span class="score">{{ scoreEntry.score }}</span>
      </div>
    </div>
    <router-link to="/new-quiz" class="start-quiz-button">Démarrer le quiz !</router-link>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.title {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 20px;
}

.question-count {
  font-size: 1.2rem;
  margin-bottom: 20px;
}

.scores-container {
  width: 100%;
  max-width: 600px;
  margin-bottom: 20px;
}

.scores-title {
  font-size: 1.8rem;
  color: #444;
  margin-bottom: 10px;
}

.score-entry {
  background-color: #fff;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  display: flex;
  justify-content: space-between;
}

.player-name {
  font-weight: bold;
  color: #555;
}

.score {
  color: #888;
}

.start-quiz-button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 1rem;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 5px;
  text-decoration: none;
  cursor: pointer;
}

.start-quiz-button:hover {
  background-color: #0056b3;
}
</style>
