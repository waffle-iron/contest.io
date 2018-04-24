<template>
  <div id="navbar">

    <!-- Toolbar -->
    <v-toolbar>
      <!-- Side Bar Icon -->
      <v-toolbar-side-icon></v-toolbar-side-icon>

      <router-link to="/" tag="v-toolbar-title" class="titlenavbar">Contest.io</router-link>

      <v-spacer></v-spacer>

      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn to="/contest/1" flat>Dashboard</v-btn>
        <v-btn flat>Login</v-btn>
      </v-toolbar-items>

    </v-toolbar>

  </div>
</template>

<script>

export default {
  name: 'navbar',
  components: {

  }
}
</script>

<style scoped>
.titlenavbar:hover {
  cursor: pointer;
}
</style>
