import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'

// Vue Material
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
// Theme
import 'vue-material/dist/theme/default.css' // This line here

// Use Vue Material
Vue.use(VueMaterial)

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
