<template>
  <div class="home">
    <div class="quiz-container">
      <h1 class="quiz-title">Welcome to the Quiz!</h1>
      <button class="start-quiz-button">Démarrer le quiz !</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
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
