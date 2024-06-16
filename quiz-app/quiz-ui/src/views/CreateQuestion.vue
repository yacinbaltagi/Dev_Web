<template>
  <div class="create-question">
    <div class="create-container">
      <h1 class="create-title">Créer une Nouvelle Question</h1>
      <div>
        <label for="position">Position</label>
        <input type="text" v-model="question.position" placeholder="Position" id="position" />
      </div>
      <div>
        <label for="title">Titre</label>
        <input type="text" v-model="question.title" placeholder="Titre" id="title" />
      </div>
      <div>
        <label for="text">Texte de la question</label>
        <textarea v-model="question.text" placeholder="Texte de la question" id="text"></textarea>
      </div>
      <div>
        <label for="image">Choisir une image</label>
        <input type="file" @change="onFileChange" id="image" />
        <div v-if="question.image">
          <img :src="question.image" alt="Question Image" />
        </div>
      </div>
      <div v-for="(answer, index) in question.possibleAnswers" :key="index">
        <label :for="'answer-' + index">Réponse {{ index + 1 }}</label>
        <input type="text" v-model="answer.text" :placeholder="'Réponse ' + (index + 1)" :id="'answer-' + index" />
        <input type="checkbox" v-model="answer.isCorrect" /> Correct
      </div>
      <button class="save-button" @click="saveQuestion">Sauvegarder</button>
      <button class="cancel-button" @click="cancelCreation">Annuler</button>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'CreateQuestion',
  data() {
    return {
      question: {
        position: '',
        title: '',
        text: '',
        image: '',
        possibleAnswers: [
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false }
        ]
      }
    };
  },
  methods: {
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
        const response = await QuizApiService.addQuestion(this.question);
        if (response.status === 200) {
          this.$router.push('/admin');
        } else {
          console.error('Error saving question:', response.data);
        }
      } catch (error) {
        console.error('Error saving question:', error);
      }
    },
    cancelCreation() {
      this.$router.push('/admin');
    }
  }
};
</script>

<style scoped>
.create-question {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  text-align: center;
}

.create-container {
  background: rgba(0, 0, 0, 0.7);
  padding: 2rem;
  border-radius: 10px;
}

.create-title {
  color: #ffdd57;
}

.create-container div {
  margin-bottom: 1rem;
}

label {
  display: block;
  color: #ffdd57;
  margin-bottom: 0.5rem;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

input[type="file"] {
  margin-bottom: 1rem;
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
