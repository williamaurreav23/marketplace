export default [
  {
    path: '/login',
    name: 'login',
    component: resolve => require(['@/auth/pages/Login.vue'], resolve),
  },
  {
    path: '/register',
    name: 'registration',
    component: resolve => require(['@/auth/pages/Registration.vue'], resolve),
  },
  {
    path: '/restore-password/:restorePasswordCode/',
    name: 'restore.password',
    component: resolve => require(['@/auth/pages/RestorePassword.vue'], resolve),
    props: true,
  },
  {
    path: '/forgot',
    name: 'forgot',
    component: resolve => require(['@/auth/pages/Forgot.vue'], resolve),
  },
  {
    path: '/verified/:verificationCode/',
    name: 'verified',
    component: resolve => require(['@/auth/pages/Verified.vue'], resolve),
    props: true,
  },
  // Athletes
  {
    path: '/athlete-profile',
    name: 'athlete.profile',
    component: resolve => require(['@/athletes/pages/AthleteProfile.vue'], resolve),
    meta: {
      auth: true,
    },
  },
  {
    path: '/athletes',
    name: 'athlete.list',
    component: resolve => require(['@/athletes/pages/AthleteList.vue'], resolve),
  },
  {
    path: '/athletes/:athleteId',
    name: 'athlete.details',
    component: resolve => require(['@/athletes/pages/AthleteDetails.vue'], resolve),
    props: true,
  },

  {
    path: '/purchases/:athleteId',
    name: 'athlete.invest',
    component: resolve => require(['@/athletes/pages/AthleteInvest.vue'], resolve),
    meta: {
      auth: true,
    },
  },
  {
    path: '/purchased/:purchaseId',
    name: 'athlete.invested',
    component: resolve => require(['@/athletes/pages/AthleteInvested.vue'], resolve),
    props: true,
    meta: {
      auth: true,
    },
  },

  // Supporters
  {
    path: '/supporter-profile',
    name: 'supporter.profile',
    component: resolve => require(['@/supporters/pages/SupporterProfile.vue'], resolve),
    meta: {
      auth: true,
    },
  },

  {
    path: '/notifications',
    name: 'notifications',
    component: resolve => require(['@/actions/pages/Notifications.vue'], resolve),
  },

  // 404
  {
    path: '/404',
    name: 'not-found',
    component: resolve => require(['@/pages/NotFound.vue'], resolve),
  },
  // Redirects
  {
    path: '/',
    redirect: '/athletes',
  },
  {
    path: '/*',
    redirect: '/404',
  },
]
