<template>
  <div class="login">
    <div class="login-container">
      <h1 class="login-title">Connexion</h1>
      <input type="password" v-model="password" placeholder="Mot de passe" />
      <button class="login-button" @click="login">Connexion</button>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
  name: 'Login',
  data() {
    return {
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await QuizApiService.login(this.password);
        if (response.status === 200) {
          // Stocker le token pour l'utiliser dans les requêtes suivantes
          localStorage.setItem('authToken', response.data.token);
          this.$router.push('/admin');
        } else {
          this.errorMessage = 'Mauvais mot de passe';
        }
      } catch (error) {
        this.errorMessage = 'Mauvais mot de passe';
      }
    }
  }
};
</script>

<style scoped>
.login {
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

.login-container {
  background: rgba(0, 0, 0, 0.7);
  padding: 2rem;
  border-radius: 10px;
}

.login-title {
  color: #ffdd57;
}

.login-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  margin-top: 1rem;
  cursor: pointer;
  border-radius: 5px;
}

.login-button:hover {
  background-color: #0056b3;
}

.error-message {
  color: red;
  margin-top: 1rem;
}
</style>
