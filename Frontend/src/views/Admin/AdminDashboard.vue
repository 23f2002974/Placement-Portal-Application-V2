<template>

<div class="admin-container">

  <h1 class="title">Admin Dashboard</h1>

  <!-- Search -->
  <div class="search-box">
    <input v-model="search" placeholder="Search students or organizations..." />
    <button class="primary">Search</button>
  </div>


  <!-- Registered Companies -->
  <div class="card">
    <h3>Registered Companies</h3>

    <div v-for="company in companies" :key="company.id" class="row-item">
      <span>{{ company.name }}</span>

      <button class="danger" @click="blacklistCompany(company.id)">
        Blacklist
      </button>
    </div>
  </div>


  <!-- Registered Students -->
  <div class="card">
    <h3>Registered Students</h3>

    <div v-for="student in students" :key="student.id" class="row-item">
      <span>{{ student.name }}</span>

      <button class="danger" @click="blacklistStudent(student.id)">
        Blacklist
      </button>
    </div>
  </div>


  <!-- Company Applications -->
  <div class="card">
    <h3>Company Applications</h3>

    <div v-for="app in companyApplications" :key="app.id" class="row-item">
      <span>{{ app.name }}</span>

      <button class="success" @click="approveCompany(app.id)">
        Approve
      </button>
    </div>
  </div>


  <!-- Ongoing Drives -->
  <div class="card">

    <h3>Ongoing Drives</h3>

    <table class="styled-table">

      <thead>
        <tr>
          <th>Sr No</th>
          <th>Drive Name</th>
          <th>Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="drive in drives" :key="drive.id">

          <td>{{ drive.id }}</td>
          <td>{{ drive.name }}</td>

          <td class="actions">
            <button @click="viewDrive(drive)">View</button>

            <button class="success" @click="markComplete(drive.id)">
              Complete
            </button>
          </td>

        </tr>
      </tbody>

    </table>

  </div>


  <!-- Student Applications -->
  <div class="card">

    <h3>Student Applications</h3>

    <table class="styled-table">

      <thead>
        <tr>
          <th>Sr No</th>
          <th>Name</th>
          <th>Drive</th>
          <th>Company</th>
          <th>Date</th>
          <th>Action</th>
        </tr>
      </thead>

      <tbody>

        <tr v-for="app in studentApplications" :key="app.id">

          <td>{{ app.id }}</td>
          <td>{{ app.student }}</td>
          <td>{{ app.drive }}</td>
          <td>{{ app.company }}</td>
          <td>{{ app.date }}</td>

          <td>
            <button @click="viewApplication(app)">
              View
            </button>
          </td>

        </tr>

      </tbody>

    </table>

  </div>

</div>

</template>


<script>
export default {

  name: "AdminDashboard",

  data() {

    return {

      search: "",

      companies: [
        { id:1, name:"Company 1"},
        { id:2, name:"Company 2"}
      ],

      students: [
        { id:1, name:"Mr. abcde"},
        { id:2, name:"Miss. Pqrst"}
      ],

      companyApplications: [
        { id:3, name:"Company 3"},
        { id:4, name:"Company 4"}
      ],

      drives: [
        { id:1001, name:"Drive 1"}
      ],

      studentApplications: [
        {
          id:1,
          student:"Mr. abcde",
          drive:"Drive 2",
          company:"Company 2",
          date:"24/09/2025"
        }
      ]

    }

  },

  methods: {

    blacklistCompany(id){
      alert("Company blacklisted " + id)
    },

    blacklistStudent(id){
      alert("Student blacklisted " + id)
    },

    approveCompany(id){
      alert("Company approved " + id)
    },

    markComplete(id){
      alert("Drive completed " + id)
    },

    viewDrive(drive){
      console.log(drive)
    },

    viewApplication(app){
      console.log(app)
    }

  }

}
</script>


<style scoped>
.admin-container{
  max-width: 1100px;
  margin: auto;
  padding: 40px;
  font-family: Arial, Helvetica, sans-serif;
}

.title{
  text-align:center;
  margin-bottom:30px;
}

.search-box{
  display:flex;
  gap:10px;
  margin-bottom:30px;
}

.search-box input{
  flex:1;
  padding:10px;
  border-radius:6px;
  border:1px solid #ccc;
}

.card{
  background:white;
  padding:20px;
  border-radius:10px;
  margin-bottom:25px;
  box-shadow:0 2px 8px rgba(0,0,0,0.08);
}

.row-item{
  display:flex;
  justify-content:space-between;
  align-items:center;
  padding:10px 0;
  border-bottom:1px solid #eee;
}

.row-item:last-child{
  border-bottom:none;
}

button{
  padding:6px 12px;
  border:none;
  border-radius:6px;
  cursor:pointer;
  background:#eee;
}

button:hover{
  opacity:0.9;
}

.primary{
  background:#4f46e5;
  color:white;
}

.success{
  background:#22c55e;
  color:white;
}

.danger{
  background:#ef4444;
  color:white;
}

.styled-table{
  width:100%;
  border-collapse:collapse;
}

.styled-table th{
  text-align:left;
  padding:10px;
  background:#f5f5f5;
}

.styled-table td{
  padding:10px;
  border-bottom:1px solid #eee;
}

.actions{
  display:flex;
  gap:10px;
}
.admin-container{
  width:900px;
  margin:auto;
}

.card{
  border:1px solid #ddd;
  padding:20px;
  margin-top:20px;
}

.row{
  display:flex;
  justify-content:space-between;
  margin-bottom:10px;
}

button{
  padding:6px 10px;
}

.danger{
  background:#ff5b5b;
  color:white;
}

.success{
  background:#4caf50;
  color:white;
}

table{
  width:100%;
  border-collapse: collapse;
}

td,th{
  border:1px solid #ddd;
  padding:8px;
}

</style>