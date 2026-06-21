```vue
<script setup>
import { ref } from "vue"

const role = ref("")

const student = ref({
  fullName: "",
  branch: "",
  cgpa: null,
  graduationYear: null,
  phone: "",
  resume: null
})

const company = ref({
  companyName: "",
  website: "",
  phone: "",
  description: ""
})

function handleResumeUpload(event) {
  student.value.resume = event.target.files[0]
}

function registerStudent() {
  console.log("Student Registration", student.value)
  alert("Student Registration Submitted")
}

function registerCompany() {
  console.log("Company Registration", company.value)
  alert("Company Registration Submitted")
}
</script>

<template>
  <div class="auth-page">
    <div class="card auth-card">
      <h2 class="auth-title">Register</h2>

      <div class="form-group">
        <label>Register As</label>

        <select
          v-model="role"
          class="form-input"
        >
          <option value="">Select Role</option>
          <option value="student">Student</option>
          <option value="company">Company</option>
        </select>
      </div>

      <!-- STUDENT FORM -->
      <form
        v-if="role === 'student'"
        @submit.prevent="registerStudent"
      >
        <div class="form-group">
          <label>Full Name</label>
          <input
            type="text"
            class="form-input"
            v-model="student.fullName"
            placeholder="Enter full name"
            required
          />
        </div>

        <div class="form-group">
          <label>Branch</label>
          <input
            type="text"
            class="form-input"
            v-model="student.branch"
            placeholder="Enter branch"
            required
          />
        </div>

        <div class="form-group">
          <label>CGPA</label>
          <input
            type="number"
            step="0.01"
            class="form-input"
            v-model="student.cgpa"
            placeholder="Enter CGPA"
            required
          />
        </div>

        <div class="form-group">
          <label>Graduation Year</label>
          <input
            type="number"
            class="form-input"
            v-model="student.graduationYear"
            placeholder="Enter graduation year"
            required
          />
        </div>

        <div class="form-group">
          <label>Phone Number</label>
          <input
            type="text"
            class="form-input"
            v-model="student.phone"
            placeholder="Enter phone number"
            required
          />
        </div>

        <div class="form-group">
          <label>Upload Resume</label>
          <input
            type="file"
            class="form-input"
            @change="handleResumeUpload"
          />
        </div>

        <button
          type="submit"
          class="btn btn-primary"
        >
          Register Student
        </button>
      </form>

      <!-- COMPANY FORM -->
      <form
        v-if="role === 'company'"
        @submit.prevent="registerCompany"
      >
        <div class="form-group">
          <label>Company Name</label>
          <input
            type="text"
            class="form-input"
            v-model="company.companyName"
            placeholder="Enter company name"
            required
          />
        </div>

        <div class="form-group">
          <label>Website</label>
          <input
            type="url"
            class="form-input"
            v-model="company.website"
            placeholder="https://company.com"
            required
          />
        </div>

        <div class="form-group">
          <label>Phone Number</label>
          <input
            type="text"
            class="form-input"
            v-model="company.phone"
            placeholder="Enter phone number"
            required
          />
        </div>

        <div class="form-group">
          <label>Description</label>
          <textarea
            rows="4"
            class="form-input"
            v-model="company.description"
            placeholder="Tell us about your company"
            required
          ></textarea>
        </div>

        <button
          type="submit"
          class="btn btn-primary"
        >
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
