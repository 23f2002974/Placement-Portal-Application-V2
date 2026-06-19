<script setup>
import { RouterLink , RouterView} from 'vue-router';

async function logout() {
    const response = await fetch('http://127.0.0.1:5000/api/logout', {
        method: 'POST',
        headers: {
            'Authorization': `${localStorage.getItem('token')}`
        }
    });
    if (!response.ok) {
        const text = await response.text();
        console.log("Server returned:", text);
        alert("Logout failed");
        return;
    }
    const data = await response.json();
    localStorage.removeItem('token');
    console.log(data.message);
    alert('Logged out successfully!');
}
</script>

<template>
  <div class="container-fluid">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/">Placmenet Portal</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
          <li class="nav-item">
            <RouterLink class="nav-link active" aria-current="page" to="/login">Login</RouterLink>
          </li>
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" v-on:click="logout" href="#">Logout </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  
    <RouterView/>
    <footer class="footer">

    <div class="links">
      <a>Browse Jobs</a> | <a>Companies</a> | <a>Salary Insights</a> | <a>Career Advice</a> |
    </div>

    <p>© 2026 Placement Portal</p>

  </footer>
  </div>
</template>

<style scoped>
.container {
  width: 2000px;
}

.footer{
  margin-top:88vh;
  text-align:center;
  padding:20px;
  background:#f7f7f7;
}

</style>
