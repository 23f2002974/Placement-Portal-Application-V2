<template>
<div class="container-fluid">
    <div class="row justify-content-center">
        <div class="col-5">
            <h2 class="text-center mb-3">Login</h2>
            <form v-on:submit.prevent="login">
                <div class="mb-3">
                    <label for="email" class="form-label">Email address</label>
                    <input type="text" class="form-control" id="email" placeholder="Enter email" v-model="email">
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" class="form-control" id="password" placeholder="Password" v-model="password" @input="validatePassword">
                    <div v-if="passwordError" class="text-danger mt-1">{{ passwordError }}</div>
                </div>
                <button type="submit" class="btn btn-primary w-100">Login</button>

                <p class="mt-3">
                Don't have an account?
                <RouterLink to="/register">Register here</RouterLink>
                </p>
            </form>
        </div>
    </div>
</div>
</template>

<script setup>  
import { ref } from 'vue';
import { RouterLink , RouterView} from 'vue-router';
import { useRouter } from 'vue-router';

const router = useRouter();

const email = ref('');
const password = ref('');
const passwordError = ref('');

const validatePassword = () => {
    if (password.value.length < 8) {
        passwordError.value = 'Password must be at least 8 characters long.';
        return false;
    } else {
        passwordError.value = '';
        return true;
    }
};

async function login() {
    if (!validatePassword()) {
        console.log('Invalid Password length');
        return
    }
    if (email.value === '' || password.value === '') {
        console.log('Email and Password cannot be empty');
        return
    }

    const response =  await fetch('http://127.0.0.1:5000/api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email.value,
            password: password.value
        })
    });

    console.log(response);

    if (!response.ok) {
        const errorData = await response.json();
        console.error(errorData);
        alert(`Login failed: ${errorData.message}`);
        return;
        
    } else {
        const data = await response.json();
        alert(`Login successful: ${data.message}`);
        localStorage.setItem('token', data.user.auth_token);
        localStorage.setItem('role', data.user.role[0]);
        localStorage.setItem('email', data.user.email);
        

        const role = data.user.role[0]

        if (role === "admin") {
            await router.push("/admin")
        }
        else if (role === "company") {
            await router.push("/company")
        }
        else if (role === "student") {
            await router.push("/student")
        }
        return;
    }
}
</script>