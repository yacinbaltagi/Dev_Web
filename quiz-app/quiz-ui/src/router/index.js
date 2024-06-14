import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import NewQuizPage from '../views/NewQuizPage.vue';
import QuestionPage from '../views/QuestionPage.vue';

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
    name: 'QuestionPage',
    component: QuestionPage
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router;
