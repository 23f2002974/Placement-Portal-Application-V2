```vue
<script setup>
import { ref } from "vue"

const role = ref("")

const student = ref({
  email: "",
  password: "",
  fullName: "",
  branch: "",
  cgpa: null,
  graduationYear: null,
  phone: "",
  resume: null
})

const company = ref({
  email: "",
  password: "",
  companyName: "",
  website: "",
  phone: "",
  description: ""
})

function handleResumeUpload(event) {
  student.value.resume = event.target.files[0]
}

async function registerStudent() {
  try {
    const formData = new FormData()

    formData.append("email", student.value.email)
    formData.append("password", student.value.password)

    formData.append("full_name", student.value.fullName)
    formData.append("branch", student.value.branch)
    formData.append("cgpa", student.value.cgpa)
    formData.append("graduation_year", student.value.graduationYear)
    formData.append("phone", student.value.phone)

    if (student.value.resume) {
      formData.append("resume", student.value.resume)
    }

    const response = await fetch(
      "http://127.0.0.1:5000/api/students/register",
      {
        method: "POST",
        body: formData
      }
    )

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || data.message || "Registration failed")
    }

    alert("Student Registration Successful")
    console.log(data)

  } catch (error) {
    console.error(error)
    alert(error.message)
  }
}

async function registerCompany() {
  try {
    const response = await fetch(
      "http://127.0.0.1:5000/api/companies/register",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(company.value)
      }
    )

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.message || "Registration failed")
    }

    alert("Company Registration Successful")
    console.log(data)

  } catch (error) {
    console.error(error)
    alert(error.message)
  }
}
</script>

<template>
  <div class="auth-page">
    <div class="card auth-card">
      <h2 class="auth-title">Register</h2>

      <div class="form-group">
        <label>Register As</label>

        <select v-model="role" class="form-input">
          <option value="">Select Role</option>
          <option value="student">Student</option>
          <option value="company">Company</option>
        </select>
      </div>

      <form v-if="role === 'student'" @submit.prevent="registerStudent">
        <div class="form-group">
          <label>Email</label>
          <input type="email" class="form-input" v-model="student.email" placeholder="Enter email" required />
        </div>

        <div class="form-group">
          <label>Password</label>
          <input type="password" class="form-input" v-model="student.password" placeholder="Enter password" required />
        </div>

        <div class="form-group">
          <label>Full Name</label>
          <input type="text" class="form-input" v-model="student.fullName" placeholder="Enter full name" required />
        </div>

        <div class="form-group">
          <label>Branch</label>
          <input type="text" class="form-input" v-model="student.branch" placeholder="Enter branch" required />
        </div>

        <div class="form-group">
          <label>CGPA</label>
          <input type="number" step="0.01" min="0" max="10" class="form-input" v-model="student.cgpa"
            placeholder="Enter CGPA" required />
        </div>

        <div class="form-group">
          <label>Graduation Year</label>
          <input type="number" class="form-input" v-model="student.graduationYear" placeholder="Enter graduation year"
            required />
        </div>

        <div class="form-group">
          <label>Phone Number</label>
          <input type="text" class="form-input" v-model="student.phone" placeholder="Enter phone number" required />
        </div>

        <div class="form-group">
          <label>Upload Resume (PDF)</label>
          <input type="file" class="form-input" accept=".pdf,.doc,.docx" @change="handleResumeUpload" />
        </div>

        <button type="submit" class="btn btn-primary">
          Register Student
        </button>
      </form>

      <!-- COMPANY FORM -->
      <form v-if="role === 'company'" @submit.prevent="registerCompany">
        <div class="form-group">
          <label>Email</label>
          <input type="email" class="form-input" v-model="company.email" placeholder="Enter company email" required />
        </div>

        <div class="form-group">
          <label>Password</label>
          <input type="password" class="form-input" v-model="company.password" placeholder="Create password" required />
        </div>

        <div class="form-group">
          <label>Company Name</label>
          <input type="text" class="form-input" v-model="company.companyName" placeholder="Enter company name"
            required />
        </div>

        <div class="form-group">
          <label>Website</label>
          <input type="url" class="form-input" v-model="company.website" placeholder="https://company.com" required />
        </div>

        <div class="form-group">
          <label>Phone Number</label>
          <input type="text" class="form-input" v-model="company.phone" placeholder="Enter phone number" required />
        </div>

        <div class="form-group">
          <label>Description</label>
          <textarea rows="4" class="form-input" v-model="company.description" placeholder="Tell us about your company"
            required></textarea>
        </div>

        <button type="submit" class="btn btn-primary">
          Register Company
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.auth-page {
  min-height: calc(100vh - 80px);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 24px;
}

.auth-card {
  width: 100%;
  max-width: 650px;
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

.form-group label {
  display: block;
  margin-bottom: 6px;
  font-weight: 500;
}

.form-input {
  width: 100%;
}

.btn {
  width: 100%;
  margin-top: 10px;

}

.btn-primary {
  background-color: black;
  border: none;
}
</style>
```
