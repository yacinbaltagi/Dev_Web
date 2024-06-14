<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  question: Object
});

const emit = defineEmits(['question-answered']);

const answerQuestion = (answer) => {
  emit('question-answered', answer);
};
</script>

<template>
  <div>
    <h2>{{ question.title }}</h2>
    <p>{{ question.text }}</p>
    <div v-for="answer in question.possibleAnswers" :key="answer.text">
      <button @click="answerQuestion(answer)">
        {{ answer.text }}
      </button>
    </div>
  </div>
</template>

<style scoped>
button {
  display: block;
  margin: 10px 0;
  padding: 10px;
  width: 100%;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
