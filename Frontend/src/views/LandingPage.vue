<script setup>
import { useRouter } from 'vue-router'
import { RouterLink , RouterView} from 'vue-router';

const router = useRouter()

function goToLogin(){
  router.push('/login')
}
</script>

<template>

<div class="landing">

  <div class="hero">

    <h1 class="logo">Placement Portal</h1>

    <h2>Your next job starts here</h2>

    <p>
      Create an account or sign in to see your personalised job recommendations.
    </p>

    <RouterLink to="/login" class="start-btn">Get Started →</RouterLink>

  </div>

</div>

</template>

<style scoped>

.landing{
  height:80vh;
  display:flex;
  justify-content:center;
  align-items:center;
  background:#f4f6f8;
}

.hero{
  text-align:center;
}

.logo{
  font-size:60px;
  color:#1a73e8;
}

.start-btn{
  background:#1a73e8;
  color:white;
  border:none;
  padding:14px 30px;
  font-size:18px;
  border-radius:8px;
  cursor:pointer;
}

</style>