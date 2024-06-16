<template>
  <div :class="['container', { 'no-background': quizStarted }]">
    <div class="enter-name" v-if="!quizStarted && !quizSubmitted">
      <div class="quiz-container">
        <h1 class="quiz-title">Saisissez votre nom</h1>
        <input type="text" v-model="name" placeholder="Username" />
        <button class="start-quiz-button" @click="startQuiz">GO!</button>
      </div>
    </div>
    <div class="quiz" v-if="quizStarted">
      <div class="quiz-container">
        <h1 class="quiz-title">Quiz</h1>
        <div v-if="questions.length">
          <div v-for="(question, index) in questions" :key="index" class="question">
            <h3>{{ question.title }}</h3>
            <p>{{ question.text }}</p>
            <ul>
              <li v-for="(answer, ansIndex) in question.possibleAnswers" :key="ansIndex">
                <input type="radio" :name="'question-' + index" :value="answer.text" v-model="answers[index]" />
                {{ answer.text }}
              </li>
            </ul>
          </div>
          <button class="submit-quiz-button" @click="submitQuiz">Submit Quiz</button>
        </div>
        <div v-else>
          <p>Loading questions...</p>
        </div>
      </div>
    </div>
    <div class="quiz-result" v-if="quizSubmitted">
      <div class="quiz-container">
        <h1 class="quiz-title">Résultat</h1>
        <p>Nom : {{ name }}</p>
        <p>Score : {{ score }} / {{ questions.length }}</p>
        <button class="start-quiz-button" @click="restartQuiz">Recommencer</button>
      </div>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'EnterName',
  data() {
    return {
      name: '',
      quizStarted: false,
      quizSubmitted: false,
      questions: [],
      answers: [],
      score: 0
    };
  },
  methods: {
    async startQuiz() {
      if (this.name.trim() !== '') {
        try {
          const response = await QuizApiService.getQuestions();
          console.log('Questions:', response.data);  // Ajouter des logs pour vérifier les données
          this.questions = response.data;
          this.answers = Array(response.data.length).fill(null);
          this.quizStarted = true;
        } catch (error) {
          console.error('Error fetching questions:', error);
        }
      } else {
        alert('Please enter your name');
      }
    },
    submitQuiz() {
      this.calculateScore();
      this.quizStarted = false;
      this.quizSubmitted = true;
    },
    calculateScore() {
      let score = 0;
      this.questions.forEach((question, index) => {
        const userAnswer = this.answers[index];
        const correctAnswer = question.possibleAnswers.find(answer => answer.isCorrect).text;
        if (userAnswer === correctAnswer) {
          score++;
        }
      });
      this.score = score;
    },
    restartQuiz() {
      this.name = '';
      this.quizStarted = false;
      this.quizSubmitted = false;
      this.questions = [];
      this.answers = [];
      this.score = 0;
    }
  }
}
</script>

<style scoped>
.container {
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

.no-background {
  background-image: none;
}

.quiz-container {
  background: rgba(0, 0, 0, 0.7);
  padding: 2rem;
  border-radius: 10px;
}

.quiz-title {
  color: #ffdd57;
}

.start-quiz-button,
.submit-quiz-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  margin-top: 1rem;
  cursor: pointer;
  border-radius: 5px;
}

.start-quiz-button:hover,
.submit-quiz-button:hover {
  background-color: #0056b3;
}

.question {
  margin-bottom: 2rem;
}

.question h3 {
  margin-bottom: 1rem;
}

.question ul {
  list-style-type: none;
  padding: 0;
}

.question li {
  margin-bottom: 0.5rem;
}
</style>
