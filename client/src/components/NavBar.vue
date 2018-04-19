<template>
  <div id="navbar">

    <!-- Toolbar -->
    <md-toolbar>

      <!-- Title -->
      <h3 class="md-title" style="flex: 1">Title</h3>

      <!-- Dropdown -->
      <md-menu>
        <md-button class="md-icon-button" md-menu-trigger>
          <md-icon>more_vert</md-icon>
        </md-button>
        <!-- Dropdown content -->

        <md-menu-content>
          <md-menu-item>
            <router-link :to="{ name: '', params: {} }">Login</router-link>
          </md-menu-item>
        </md-menu-content>

      </md-menu>

    </md-toolbar>

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
  .md-toolbar {
    margin-top: 16px;
  }
</style>
