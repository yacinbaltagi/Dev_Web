<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import participationStorageService from '@/services/ParticipationStorageService';

const username = ref('');
const router = useRouter();

const launchNewQuiz = () => {
  console.log("Launch new quiz with", username.value);
  if (username.value.trim()) {
    participationStorageService.savePlayerName(username.value);
    router.push('/questions');
  }
};
</script>

<template>
  <div class="container mt-5">
    <h1 class="text-center">Saisissez votre nom :</h1>
    <form @submit.prevent="launchNewQuiz" class="text-center mt-3">
      <div class="mb-3">
        <input type="text" class="form-control" id="username" v-model="username" placeholder="Username" required />
      </div>
      <button type="submit" class="btn btn-danger">GO!</button>
    </form>
    <p>{{ username }}</p> <!-- Interpolation temporaire pour vérifier le binding -->
  </div>
</template>

<style scoped>
.container {
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

button {
  width: 100%;
  padding: 10px;
  font-size: 1.2rem;
}
</style>
