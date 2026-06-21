<script setup>
import Navbar from './components/Navbar.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="app-layout">
    <Navbar />
    <main class="main-content">
      <RouterView />
    </main>

    <footer class="footer">
      <div class="links">
        <a>Browse Jobs</a> |
        <a>Companies</a> |
        <a>Salary Insights</a> |
        <a>Career Advice</a>
      </div>

      <p>© 2026 Placement Portal</p>
    </footer>
  </div>
</template>

<style scoped>
.app-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 5px;
}

.footer {
  text-align: center;
  padding: 20px;
  background: var(--surface);
  border-top: 1px solid var(--border);
}
</style>