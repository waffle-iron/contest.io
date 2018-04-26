<template>
  <div id="createcontest">
    <!-- Layout container -->
    <v-container>

      <v-form>
        <v-layout>

          <!-- Add tasks -->
          <v-flex xs10 id="taskselection">
            <!-- TODO: Add Filter and Search options -->
            <v-text-field prepend-icon="search" v-model="searchtitle" label="Search by name" solo-inverted class="mx-0 search" clearable="true" flat></v-text-field>
            <!-- container for task selection -->
            <div style="height: 320px; overflow: scroll;">
              <v-list>

                <template v-for="item in filteredItems">

                   <v-subheader v-if="item.header" :key="item.id">{{ item.header }}</v-subheader>

                   <v-divider></v-divider>

                   <v-list-tile avatar :key="item.id" @click="">

                     <v-list-tile-action>
                       <!-- <v-btn absolute fab center small color="light-green accent-3"> -->
                         <v-icon>add</v-icon>
                       <!-- </v-btn> -->
                     </v-list-tile-action>

                    <v-list-tile-content>
                       <v-list-tile-title v-html="item.title"></v-list-tile-title>
                    </v-list-tile-content>

                    <v-chip small v-for="tag in item.tags.slice(0, 4)" >{{ tag }}</v-chip>

                   </v-list-tile>

                   <v-divider></v-divider>

                 </template>

             </v-list>
            </div>

            <!-- Task list -->
            <v-subheader style="margin-top: 5%;"> Tasks Selected so far </v-subheader>
            <v-expansion-panel popout>

             <v-expansion-panel-content v-for="item in tasks" :key="item.title">

               <div slot="header">{{ item.title }}</div>

              <v-card>

                <v-card-text>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>

                <!-- Tags -->
                <div class="text-xs-center chiptag">
                  <v-chip small>Bruteforce</v-chip>
                </div>

                <!-- TODO: add link to codeforces -->
                <v-card-actions>
                  <v-btn flat color="red" to="https://www.codeforces.org">Remove</v-btn>
                  <v-btn flat color="orange" to="https://www.codeforces.org">Solve</v-btn>
                </v-card-actions>

              </v-card>

             </v-expansion-panel-content>

           </v-expansion-panel>
          </v-flex>

          <!-- Divider -->
          <v-flex xs1></v-flex>

          <!-- Misc Setup (Start / End time), Groups, etc. -->
          <v-flex xs4>

          </v-flex>

        </v-layout>
      </v-form>

    </v-container>
  </div>
</template>

<script>

export default {
  name: 'createcontest',
  components: {

  },
  data () {
    return {
      searchtitle: "",
      items: [
        { id: 1, title: 'Task 1: Get your life together', tags: ['Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees'] },
        { id: 2, title: 'Task 2: Procrastinate Task 1 until your life is over', tags: ['Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees'] },
        { id: 3, title: 'Task 3: Drink bleech to get over your depression', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 4, title: 'Task 4: Live the good life!', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 5, title: 'Task 1: Get your life together', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 6, title: 'Task 2: Procrastinate Task 1 until your life is over', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 7, title: 'Task 3: Drink bleech to get over your depression', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 8, title: 'Task 4: Live the good life!', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 9, title: 'Task 1: Get your life together', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 10, title: 'Task 2: Procrastinate Task 1 until your life is over', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 11, title: 'Task 3: Drink bleech to get over your depression', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 12, title: 'Task 4: Live the good life!', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 13, title: 'Task 1: Get your life together', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 14, title: 'Task 2: Procrastinate Task 1 until your life is over', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 15, title: 'Task 3: Drink bleech to get over your depression', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 16, title: 'Task 4: Live the good life!', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 17, title: 'Task 1: Get your life together', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 18, title: 'Task 2: Procrastinate Task 1 until your life is over', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 19, title: 'Task 3: Drink bleech to get over your depression', tags: ['Bruteforce', 'Binary Trees'] },
        { id: 20, title: 'Task 4: Live the good life!', tags: ['Bruteforce', 'Binary Trees'] }
      ],
    tasks: [
      { title: 'Task 1: Get your life together', tags: ['Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees'] },
      { title: 'Task 2: Procrastinate Task 1 until your life is over', tags: ['Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees'] },
      { title: 'Task 3: Drink bleech to get over your depression', tags: ['Bruteforce', 'Binary Trees'] }
    ]
    }
  },
  computed: {
    filteredItems() {
      return this.items.filter((i) => {
        if(this.searchtitle)
          return i.title.includes(this.searchtitle)
        else
          return true
      })
    }
  }
}
</script>

<style scoped>

.vlink {
  cursor: pointer;
}

#taskselection {
  margin-left: -10%;
}

.search {
  width: 45%;
  margin-bottom: 5px;
}
</style>
