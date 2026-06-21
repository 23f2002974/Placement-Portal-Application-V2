<script setup>
import { RouterLink } from 'vue-router';

async function logout() {
  const response = await fetch('http://127.0.0.1:5000/api/logout', {
    method: 'POST',
    headers: {
      Authorization: `${localStorage.getItem('token')}`
    }
  });

  if (!response.ok) {
    alert('Logout failed');
    return;
  }

  localStorage.removeItem('token');
  alert('Logged out successfully!');
}
</script>

<template>
  <nav class="navbar">
    <RouterLink to="/" class="logo">
      Placement Portal
    </RouterLink>

    <div class="nav-links">
      <RouterLink to="/login" class="nav-link">
        Login
      </RouterLink>

      <button class="nav-link logout-btn" @click="logout">
        Logout
      </button>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  height: 70px;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 0 32px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  position: sticky;
  top: 0;
  z-index: 100;
}

.logo {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--text-primary);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 24px;
}

.nav-link {
  color: var(--text-secondary);
  font-weight: 500;
  transition: 0.2s;
}

.nav-link:hover {
  color: var(--primary);
}

.logout-btn {
  background: none;
  padding: 0;
  font-size: inherit;
}
</style>