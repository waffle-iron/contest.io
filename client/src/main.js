import Vue from 'vue'
import App from './App.vue'

// Vue Material
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
// Theme
import 'vue-material/dist/theme/black-green-dark.css' // This line here

// Use Vue Material
Vue.use(VueMaterial)

Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
