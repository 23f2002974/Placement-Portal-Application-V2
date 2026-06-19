import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),

  routes: [
    {
      path: '/',
      name: 'Landing',
      component: () => import('../views/LandingPage.vue')
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
    },

    {
      path: '/register',
      name: 'Register',
      component: () => import('../views/RegisterView.vue')
    },

    {
      path: '/admin',
      name: 'AdminDashboard',
      component: () => import('../views/Admin/AdminDashboard.vue')
    },

    {
      path: '/company',
      name: 'CompanyDashboard',
      component: () => import('../views/Company/CompanyDashboard.vue')
    },

    {
      path: '/student',
      name: 'StudentDashboard',
      component: () => import('../views/Student/StudentDashboard.vue')
    }
  ]

})

export default router