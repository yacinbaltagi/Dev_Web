<script setup>
import { ref, onMounted } from 'vue';
import participationStorageService from '@/services/ParticipationStorageService';
import quizApiService from '@/services/QuizApiService';
import QuestionDisplay from '@/components/QuestionDisplay.vue';

const currentQuestion = ref(null);
const currentQuestionPosition = ref(0);
const questions = ref([]);

onMounted(async () => {
  const response = await quizApiService.getQuestions();
  if (response && response.data) {
    questions.value = response.data;
    loadQuestionByPosition(currentQuestionPosition.value);
  }
});

const loadQuestionByPosition = (position) => {
  currentQuestion.value = questions.value[position];
};

const answerClickedHandler = (answer) => {
  console.log('Question answered:', answer);
  if (currentQuestionPosition.value < questions.value.length - 1) {
    currentQuestionPosition.value++;
    loadQuestionByPosition(currentQuestionPosition.value);
  } else {
    endQuiz();
  }
};

const endQuiz = () => {
  console.log('Quiz completed');
  // Navigate to result page or show score
};
</script>

<template>
  <div class="container mt-5">
    <h1 class="text-center">Quiz</h1>
    <QuestionDisplay v-if="currentQuestion" :question="currentQuestion" @question-answered="answerClickedHandler" />
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
