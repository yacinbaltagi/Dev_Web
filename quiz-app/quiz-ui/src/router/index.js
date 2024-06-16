import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import NewQuizPage from '../views/NewQuizPage.vue';
import QuestionsManager from '../views/QuestionsManager.vue';
import EnterName from '../views/EnterName.vue';

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
    path: '/enter-name',
    name: 'EnterName',
    component: EnterName
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router;
