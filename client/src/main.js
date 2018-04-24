import Vue from 'vue'
import App from './App.vue'
import router from './router'

// Import Vuetify
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

// Use Vuetify
Vue.use(Vuetify)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
