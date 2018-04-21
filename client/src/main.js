import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'

// Import Vuetify
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

// Use Vuetify
Vue.use(Vuetify)

// router
Vue.use(Router)

Vue.config.productionTip = false

// Setup all routes
const router = new Router({
  routes: [
    // dynamic segments start with a colon
    { path: '/', component: null }
  ]
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
