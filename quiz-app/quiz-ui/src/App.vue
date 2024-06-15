<script setup>
import { RouterLink, RouterView } from 'vue-router'
import './assets/main.css'
</script>

<template>
  <header>
    <nav class="navbar">
      <div class="navbar-logo">
        <RouterLink to="/">Quiz Télétravail</RouterLink>
      </div>
      <div class="navbar-links">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
      </div>
    </nav>
  </header>

  <main class="main-content">
    <RouterView />
  </main>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: #333;
  color: #fff;
}

.navbar-logo a {
  color: #fff;
  text-decoration: none;
  font-size: 1.5rem;
}

.navbar-links a {
  color: #fff;
  text-decoration: none;
  margin-left: 1rem;
}

.navbar-links a:hover {
  text-decoration: underline;
}
</style>
