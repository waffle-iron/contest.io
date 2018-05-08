import Vue from 'vue'
import App from './App.vue'
import router from './router'

// Import Vuetify
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

// Import Vue Moment
import moment from 'vue-moment'

// Use Vuetify
Vue.use(Vuetify)

// Use Vue-Moment for date formatting
Vue.use(moment)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
