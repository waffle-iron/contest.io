<template>
  <div id="navbar">

    <!-- Toolbar -->
    <v-toolbar>
      <!-- Side Bar Icon -->
      <v-toolbar-side-icon></v-toolbar-side-icon>

      <v-toolbar-title>Contest.io</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn flat>Dashboard</v-btn>
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

</style>
