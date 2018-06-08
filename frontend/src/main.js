// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { store } from './store/index'
import VueMoment from 'vue-moment'
import VueI18n from 'vue-i18n'
// or import all icons if you don't care about bundle size
import 'vue-awesome/icons'
import './scss/theme.scss'
import { messages } from './translations/translations'

Vue.config.productionTip = false

Vue.use(VueMoment)
Vue.use(VueI18n)

/** Theme & UI **/
import ElementUI from 'element-ui'

Vue.use(ElementUI)

/** Axios **/
import axios from 'axios'
import VueAxios from 'vue-axios'
import Icon from 'vue-awesome/components/Icon'

// globally (in your main .js file)
Vue.component('icon', Icon)

Vue.use(VueAxios, axios)
// csrf settings
Vue.axios.defaults.baseURL = process.env.BASE_URL
Vue.axios.defaults.xsrfCookieName = 'csrftoken'
Vue.axios.defaults.xsrfHeaderName = 'X-CSRFToken'
Vue.axios.defaults.headers.common['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.post['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.put['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.patch['Content-Type'] = 'application/json'

// Create VueI18n instance with options
const i18n = new VueI18n({
  locale: 'en', // set locale
  fallbackLocale: 'en',
  messages, // set locale messages
})

/* eslint-disable no-new */
new Vue({
  i18n,
  el: '#app',
  router,
  store,
  components: {App},
  template: '<App/>'
})
