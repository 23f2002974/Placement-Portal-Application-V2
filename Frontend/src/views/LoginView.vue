<template>
  <div class="auth-page">
    <div class="card auth-card">
      <h2 class="auth-title">Login</h2>

      <form @submit.prevent="login">

        <div class="form-group">
          <label for="email">Email Address</label>

          <input
            id="email"
            type="email"
            placeholder="Enter email"
            v-model="email"
          />
        </div>

        <div class="form-group">
          <label for="password">Password</label>

          <input
            id="password"
            type="password"
            placeholder="Enter password"
            v-model="password"
            @input="validatePassword"
          />

          <p
            v-if="passwordError"
            class="error-text"
          >
            {{ passwordError }}
          </p>
        </div>

        <button
          type="submit"
          class="btn btn-primary"
          :disabled="loading"
        >
          {{ loading ? 'Logging In...' : 'Login' }}
        </button>

        <p class="auth-footer">
          Don't have an account?
          <RouterLink to="/register" class="link">
            Register here
          </RouterLink>
        </p>

      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const password = ref('')
const passwordError = ref('')
const loading = ref(false)

const validatePassword = () => {
  if (password.value.length < 8) {
    passwordError.value =
      'Password must be at least 8 characters long'
    return false
  }

  passwordError.value = ''
  return true
}

async function login() {
  if (!validatePassword()) return

  if (!email.value || !password.value) {
    alert('Please fill all fields')
    return
  }

  loading.value = true

  try {
    const response = await fetch(
      'http://127.0.0.1:5000/api/login',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: email.value,
          password: password.value
        })
      }
    )

    const data = await response.json()

    if (!response.ok) {
      alert(data.message || 'Login failed')
      return
    }

    localStorage.setItem(
      'token',
      data.user.auth_token
    )

    localStorage.setItem(
      'role',
      data.user.role[0]
    )

    localStorage.setItem(
      'email',
      data.user.email
    )

    alert(data.message)

    const role = data.user.role[0]

    if (role === 'admin') {
      router.push('/admin')
    } else if (role === 'company') {
      router.push('/company')
    } else if (role === 'student') {
      router.push('/student')
    }

  } catch (error) {
    console.error(error)
    alert('Server error. Please try again.')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.auth-page {
  min-height: calc(100vh - 140px);

  display: flex;
  justify-content: center;
  align-items: center;

  padding: 24px;
}

.auth-card {
  width: 100%;
  max-width: 450px;
}

.auth-title {
  text-align: center;
  margin-bottom: 24px;
  font-size: 2rem;
  font-weight: 700;
}

.form-group {
  margin-bottom: 18px;
}

.error-text {
  color: #ef4444;
  margin-top: 6px;
  font-size: 0.9rem;
}

.btn {
  width: 100%;
}

.auth-footer {
  text-align: center;
  margin-top: 18px;
}

.link {
  color: var(--primary);
  font-weight: 600;
}

.link:hover {
  text-decoration: underline;
}
</style>