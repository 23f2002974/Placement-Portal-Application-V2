<script setup>
import { ref } from 'vue'

const role = ref('')
const student = ref({
    fullName: '',
    branch: '',
    cgpa: null,
    graduationYear: null,
    phone: '',
    resume: null
})
const company = ref({
    companyName: '',
    website: '',
    phone: '',
    description: ''
})

function handleResumeUpload(event){
  student.resume = event.target.files[0]
  console.log(student.resume)
}
</script>

<template>

<div class="container mt-4">

<div class="mb-3">
<label class="form-label">Register As</label>

<select v-model="role" class="form-select">
<option value="">Select</option>
<option value="student">Student</option>
<option value="company">Company</option>
</select>

</div>

<!-- STUDENT FORM -->
<div v-if="role === 'student'">

<div class="mb-3">
<label>Full Name</label>
<input type="text" class="form-control" v-model="student.fullName">
</div>

<div class="mb-3">
<label>Branch</label>
<input type="text" class="form-control" v-model="student.branch">
</div>

<div class="mb-3">
<label>CGPA</label>
<input type="number" step="0.01" class="form-control" v-model="student.cgpa">
</div>

<div class="mb-3">
<label>Graduation Year</label>
<input type="number" class="form-control" v-model="student.graduationYear">
</div>

<div class="mb-3">
<label>Phone</label>
<input type="text" class="form-control" v-model="student.phone">
</div>

<div class="mb-3">
<label>Upload Resume</label>
<input type="file"  class="form-control" @change="handleResumeUpload"/>
</div>

</div>

<!-- COMPANY FORM -->
<div v-if="role === 'company'">

<div class="mb-3">
<label>Company Name</label>
<input type="text" class="form-control" v-model="company.companyName">
</div>

<div class="mb-3">
<label>Website</label>
<input type="text" class="form-control" v-model="company.website">
</div>

<div class="mb-3">
<label>Phone</label>
<input type="text" class="form-control" v-model="company.phone">
</div>

<div class="mb-3">
<label>Description</label>
<textarea class="form-control" v-model="company.description"></textarea>
</div>

</div>

</div>

</template>