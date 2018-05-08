<template>
  <div id="createcontest">
    <!-- Layout container -->
    <v-container>

      <v-form>
        <v-layout>

          <!-- Add tasks -->
          <v-flex xs10 id="taskselection">
            <!-- TODO: Add Filter and Search options -->
            <div style="width: 100%;">
              <v-text-field style="float: left" prepend-icon="search" v-model="searchtitle" label="Search by name" solo-inverted class="ml-0 search" :clearable="true" flat></v-text-field>
              <v-select style="float: right; width: 50%; margin-bottom: 10px;" v-model="selectedtags" label="Search by tags" chips tags solo prepend-icon="filter_list" append-icon="" clearable>
                <template slot="selection" slot-scope="data">
                  <v-chip :selected="data.selected" close @input="removeSelectedTag(data.item)" >
                    <span>{{ data.item }}</span>&nbsp;
                  </v-chip>
                </template>
              </v-select>
            </div>
            <!-- container for task selection -->
            <div style="height: 320px; overflow: scroll; margin-top: 60px; min-width: 100%;">
              <v-list>

                <template v-for="item in filteredItems">

                   <v-subheader v-if="item.header" :key="item.id">{{ item.header }}</v-subheader>

                   <v-divider :key="item.id"></v-divider>

                   <v-list-tile avatar :key="item.id" @click="alert()">

                     <v-list-tile-action>
                       <!-- <v-btn absolute fab center small color="light-green accent-3"> -->
                         <v-icon @click="addTask(item.id)">add</v-icon>
                       <!-- </v-btn> -->
                     </v-list-tile-action>

                    <v-list-tile-content>
                       <v-list-tile-title v-html="item.title"></v-list-tile-title>
                    </v-list-tile-content>

                    <v-chip :key="tag" small v-for="tag in item.tags.slice(0, 4)" >{{ tag }}</v-chip>

                   </v-list-tile>

                   <v-divider :key="item.id"></v-divider>

                 </template>

             </v-list>
            </div>

            <!-- Task list -->
            <v-subheader style="margin-top: 5%;"> Tasks Selected so far </v-subheader>
            <p v-if="!tasks.length" style="color: red;">No tasks selected! Browse above tasks and click the '+' icon to add them!</p>
            <v-expansion-panel popout>

             <v-expansion-panel-content v-for="item in tasks" :key="item.id">

               <div slot="header">{{ item.title }}</div>

              <v-card>

                <v-card-text>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>

                <!-- Tags -->
                <div class="text-xs-center chiptag">
                  <v-chip small>Bruteforce</v-chip>
                </div>

                <!-- TODO: add link to codeforces -->
                <v-card-actions>
                  <v-btn flat color="red" @click="removeTask(item.id)">Remove</v-btn>
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
            <v-card>
              <v-card-text>
                <v-text v-if="contestdate">Contest End: {{ contestdate | moment("dddd, MMMM Do YYYY") }} (23:59)</v-text>
                <v-btn small="true" color="primary" dark @click.stop="dialog2 = true">Chose a date...</v-btn>

                <v-dialog v-model="dialog2" max-width="500px">
                  <v-card>
                    <v-card-title>
                      Choose an end date for the contest
                    </v-card-title>
                    <v-card-text>
                      <v-date-picker v-model="contestdate" :min="now"></v-date-picker><br>
                      <small>Note: Contests always end at 23:59!</small>
                    </v-card-text>
                    <v-card-actions>
                      <v-btn color="primary" flat @click.stop="dialog2=false">Close</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>

                <br>
                <v-text>Groups:</v-text><br><v-divider></v-divider>
                <v-chip v-for="group in selectedgroups" close @input="unselectGroup(group.name)">   {{ group.name }}</v-chip>
                <v-menu v-if="groups.length">
                  <v-btn small="true" color="primary" dark slot="activator" fab><v-icon>add</v-icon></v-btn>
                  <!-- TODO: Get all groups this person is admin of -->
                  <v-list>
                    <v-list-tile v-if="!groups.length && !selectedgroups.length" style="color: red;">You are not a group admin!</v-list-tile>
                    <v-list-tile v-else v-for="group in groups" :key="group.name" @click="selectGroup(group.name)">
                      <v-list-tile-title><v-icon style="margin-top: -5px;">add</v-icon>  {{ group.name }}</v-list-tile-title>
                    </v-list-tile>
                  </v-list>
                </v-menu>
              </v-card-text>
            </v-card>
          </v-flex>

        </v-layout>
      </v-form>

    </v-container>
  </div>
</template>

<script>
// eslint-disable-next-line
import moment from 'vue-moment'

export default {
  name: 'createcontest',
  components: {

  },
  data () {
    return {
      searchtitle: "",
      searchtags: "",
      contestdate: null,
      dialog2: false,
      first: 0,
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
      selectedtags: ['Bruteforce', 'Binary Trees'],
      tasks: [
        { id: 21, title: 'Task 1: Get your life together', tags: ['Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees'] },
        { id: 22, title: 'Task 2: Procrastinate Task 1 until your life is over', tags: ['Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees', 'Bruteforce', 'Binary Trees'] }
      ],
      groups: [ { name: "Group 1" }, { name: "Group 2" }, { name: "Group 3" }, { name: "Group 4" }, { name: "Group 5" } ],
      selectedgroups: [],
      empty: []
    }
  },
  methods: {
    // This method moves task object from items array to tasks array
    addTask(id) {
      var temp = this.items.find(x => x.id === id)
      this.items.splice(this.items.indexOf(temp), 1);
      this.tasks.push(temp);
    },
    // This method moves task object from tasks array to items array
    removeTask(id) {
      var temp = this.tasks.find(x => x.id === id)
      this.tasks.splice(this.tasks.indexOf(temp), 1);
      this.items.push(temp);
    },
    // Add groups to selection
    selectGroup(name) {
      var temp = this.groups.find(x => x.name === name)
      this.groups.splice(this.groups.indexOf(temp), 1);
      this.selectedgroups.push(temp);
    },
    // Remove groups to selection
    unselectGroup(name) {
      var temp = this.selectedgroups.find(x => x.name === name)
      this.selectedgroups.splice(this.selectedgroups.indexOf(temp), 1);
      this.groups.push(temp);
    },
    removeSelectedTag(item) {
      this.selectedtags.splice(this.selectedtags.indexOf(item), 1)
      this.selectedtags = [...this.selectedtags]
    }
  },
  computed: {
    // This filters tasks by title
    filteredItems() {
      return this.items.filter((i) => {
          if(this.selectedtags && this.searchtitle) {
            for (var tag in this.selectedtags) {
              if(!i.tags.includes(tag))
                return false
            }
            return i.title.includes(this.searchtitle)
          } else if(this.searchtitle){
            return i.title.includes(this.searchtitle)
          }
          else {
            return true
          }
      })
    },
    // Get current date
    now: function () {
      return new Date().toISOString().substring(0, 10)
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
  margin-bottom: -15px;
}
</style>
