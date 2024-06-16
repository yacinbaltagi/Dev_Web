#### `src/views/EditQuestion.vue`

```vue
<template>
  <div class="edit-question">
    <div class="edit-container">
      <h1 class="edit-title">Éditer la Question</h1>
      <input type="text" v-model="question.position" placeholder="Position" />
      <input type="text" v-model="question.title" placeholder="Titre" />
      <textarea v-model="question.text" placeholder="Texte de la question"></textarea>
      <input type="file" @change="onFileChange" />
      <div v-if="question.image">
        <img :src="question.image" alt="Question Image" />
      </div>
      <div v-for="(answer, index) in question.possibleAnswers" :key="index">
        <input type="text" v-model="answer.text" placeholder="Réponse" />
        <input type="checkbox" v-model="answer.isCorrect" /> Correct
      </div>
      <button class="save-button" @click="saveQuestion">Sauvegarder</button>
      <button class="cancel-button" @click="cancelEdit">Annuler</button>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'EditQuestion',
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
    onFileChange(event) {
      const file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = (e) => {
        this.question.image = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async saveQuestion() {
      try {
        const response = await QuizApiService.updateQuestion(this.questionId, this.question);
        if (response.status === 200) {
          this.$router.push('/admin');
        } else {
          console.error('Error saving question:', response.data);
        }
      } catch (error) {
        console.error('Error saving question:', error);
      }
    },
    cancelEdit() {
      this.$router.push('/admin');
    }
  }
};
</script>

<style scoped>
.edit-question {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  text-align: center;
}

.edit-container {
  background: rgba(0, 0, 0, 0.7);
  padding: 2rem;
  border-radius: 10px;
}

.edit-title {
  color: #ffdd57;
}

.save-button,
.cancel-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  margin: 0.5rem;
  cursor: pointer;
  border-radius: 5px;
}

.save-button:hover,
.cancel-button:hover {
  background-color: #0056b3;
}
</style>