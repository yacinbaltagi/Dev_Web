import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import NewQuizPage from '../views/NewQuizPage.vue';
import QuestionsManager from '../views/QuestionsManager.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/new-quiz',
    name: 'NewQuizPage',
    component: NewQuizPage
  },
  {
    path: '/questions',
    name: 'QuestionsManager',
    component: QuestionsManager
  },
  {
    path: '/login',  // Ajouter une route pour la page de login
    name: 'LoginPage',
    component: { template: '<div>Login Page</div>' }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router;
