import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import NewQuizPage from '../views/NewQuizPage.vue';
import QuestionsManager from '../views/QuestionsManager.vue';
import EnterName from '../views/EnterName.vue';
import Login from '../views/Login.vue';
import QuestionDetail from '../views/QuestionDetail.vue';
import EditQuestion from '../views/EditQuestion.vue';
import CreateQuestion from '../views/CreateQuestion.vue';

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
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/admin',
    name: 'Admin',
    component: QuestionsManager
  },
  {
    path: '/question/:id',
    name: 'QuestionDetail',
    component: QuestionDetail
  },
  {
    path: '/question/edit/:id',
    name: 'EditQuestion',
    component: EditQuestion
  },
  {
    path: '/new-question',
    name: 'CreateQuestion',
    component: CreateQuestion
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;
