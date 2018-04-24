<template>
  <div id="contestdashboard">
    <!-- Layout container -->
    <v-container>

      <v-layout>

        <v-flex xs6>
            <!-- Task LIst -->
            <v-subheader class="display-1" style="margin-top: 2% !important;">Contest 1</v-subheader>

            <v-avatar class="grey lighten-4 avatar" size="35px">
              <img src="https://vuetifyjs.com/static/doc-images/lists/1.jpg" alt="avatar">
              <div><v-subheader style="width: 200px;">Herr Hörner</v-subheader></div>
            </v-avatar>
            <v-expansion-panel>

             <v-expansion-panel-content v-for="item in items" :key="i">

               <div slot="header">{{ item.title }}</div>

              <v-card>

                <v-card-text>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>

                <!-- Tags -->
                <div class="text-xs-center chiptag">
                  <v-chip close small>Bruteforce</v-chip>
                </div>

                <!-- TODO: add link to codeforces -->
                <v-card-actions>
                  <v-btn flat color="orange" to="https://www.codeforces.org">Solve</v-btn>
                </v-card-actions>

              </v-card>

             </v-expansion-panel-content>

           </v-expansion-panel>

        </v-flex>

        <v-flex xs2>
        </v-flex>

        <v-flex xs4>
          <v-card class="cardprogress">

            <v-card-title primary-title>
              <div  style="width: 100% !important">
                <h3 class="headline mb-0">Progress</h3>
                <v-divider></v-divider>
                <div>0 / 4 Tasks completed (0%)</div>
                <div>Time remaining: 5 days, 11 hours</div>
              </div>
            </v-card-title>

          </v-card>
        </v-flex>

      </v-layout>

    </v-container>
  </div>
</template>

<script>

export default {
  name: 'contestdashboard',
  components: {

  },
  data () {
    return {
      items: [
        { title: 'Task 1: Get your life together' },
        { title: 'Task 2: Procrastinate Task 1 until your life is over' },
        { title: 'Task 3: Drink bleech to get over your depression' },
        { title: 'Task 4: Live the good life!' }
      ]
    }
  }
}
</script>

<style scoped>
.cardprogress {
  margin-top: 30% !important;
}

.avatar {
  margin-left: -52% !important;
  margin-bottom: 2%;
  margin-top: 1%;
}

.chiptag {
  margin-left: -70%;
}
</style>
