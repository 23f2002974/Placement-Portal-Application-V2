<template>
<div class="container-fluid p-4" >

    <!-- Header -->
    <div class="d-flex justify-content-between mb-4">
        <h3>Student Dashboard</h3>
        <div>
            <button class="btn btn-outline-secondary btn-sm me-2">Edit Profile</button>
            <button class="btn btn-outline-primary btn-sm me-2">History</button>
            <button class="btn btn-outline-danger btn-sm">Logout</button>
        </div>
    </div>

    <div class="row">

        <!-- LEFT SIDE -->
        <div class="col-md-6">

            <!-- Organizations -->
            <div class="card mb-4">
                <div class="card-header">
                    <strong>Organizations</strong>
                </div>

                <div class="card-body">
                    <div v-for="org in organizations"
                        :key="org.id"
                        class="d-flex justify-content-between border p-2 mb-2">
                        <span>{{ org.id + 1 }}</span>
                        <span>{{ org.name }}</span>

                        <button
                        class="btn btn-primary btn-sm"
                        @click="viewCompany(org)">
                        View Details
                        </button>

                    </div>
                </div>
            </div>


            <!-- Applied Drives -->
            <div class="card">
                <div class="card-header">
                    <strong>Applied Drives</strong>
                </div>

                <table class="table table-bordered mb-0">
                    <thead>
                        <tr>
                            <th>Sr</th>
                            <th>Drive</th>
                            <th>Company</th>
                            <th>Date</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr v-for="(drive,index) in appliedDrives" :key="drive.id">
                            <td>{{ index+1 }}</td>
                            <td>{{ drive.name }}</td>
                            <td>{{ drive.company }}</td>
                            <td>{{ drive.date }}</td>

                            <td>
                                <button
                                class="btn btn-info btn-sm"
                                @click="viewDrive(drive)">
                                View Details
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>

            </div>

        </div>


        <!-- RIGHT SIDE -->
        <div class="col-md-6">

            <!-- Company Overview -->
            <div v-if="selectedCompany" class="card mb-4">

                <div class="card-header d-flex justify-content-between">
                    <strong>{{ selectedCompany.name }}</strong>
                    <button class="btn btn-outline-secondary btn-sm">
                        History
                    </button>
                </div>

                <div class="card-body">

                    <h6>Overview</h6>
                    <p>{{ selectedCompany.description }}</p>

                    <h6 class="mt-3">Current Drives</h6>

                    <div
                    v-for="drive in selectedCompany.drives"
                    :key="drive.id"
                    class="d-flex justify-content-between border p-2 mb-2">

                        <span>{{ drive.name }}</span>

                        <button
                        class="btn btn-primary btn-sm"
                        @click="viewDrive(drive)">
                        View Details
                        </button>

                    </div>

                </div>
            </div>


            <!-- Drive Details -->
            <div v-if="selectedDrive" class="card">

                <div class="card-header">
                    <strong>{{ selectedDrive.name }}</strong>
                </div>

                <div class="card-body">

                    <p><b>Job Title:</b> {{ selectedDrive.job }}</p>
                    <p><b>Location:</b> {{ selectedDrive.location }}</p>
                    <p><b>Salary:</b> {{ selectedDrive.salary }}</p>

                    <p class="mt-3">
                        {{ selectedDrive.description }}
                    </p>

                    <div class="mt-3">
                        <button
                        class="btn btn-success me-2"
                        @click="applyDrive">
                        Apply
                        </button>

                        <button
                        class="btn btn-secondary"
                        @click="selectedDrive=null">
                        Go Back
                        </button>
                    </div>

                </div>
            </div>

        </div>

    </div>


    <!-- Application History Modal -->
    <div v-if="showHistory" class="modal d-block">

        <div class="modal-dialog modal-lg">
            <div class="modal-content">

                <div class="modal-header">
                    <h5>Student Application History</h5>
                    <button
                    class="btn btn-sm btn-outline-secondary"
                    @click="showHistory=false">
                    Back
                    </button>
                </div>

                <div class="modal-body">

                    <table class="table table-bordered">

                        <thead>
                            <tr>
                                <th>Drive</th>
                                <th>Interview</th>
                                <th>Job Title</th>
                                <th>Result</th>
                                <th>Remark</th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr v-for="h in history" :key="h.id">
                                <td>{{ h.drive }}</td>
                                <td>{{ h.interview }}</td>
                                <td>{{ h.job }}</td>
                                <td>{{ h.result }}</td>
                                <td>{{ h.remark }}</td>
                            </tr>
                        </tbody>

                    </table>

                </div>

            </div>
        </div>

    </div>

</div>
</template>


<script setup>
import { ref, onMounted } from "vue"
const organizations = ref([])
onMounted(async () => {
  try {
    const res = await fetch("http://127.0.0.1:5000/api/student/companies")
    const data = await res.json()

    organizations.value = data.companies

  } catch (err) {
    console.error("Error fetching companies:", err)
  }
})

const appliedDrives = ref([
{ id:1,name:"Drive 1",company:"Company 2",date:"24/09/2025"},
{ id:1,name:"Drive 1",company:"Company 2",date:"24/09/2025"}
])

const history = ref([
{ id:1,drive:"Drive 1",interview:"In-person",job:"SDE",result:"Shortlisted",remark:"None"},
{ id:2,drive:"Drive 2",interview:"Online",job:"SWE",result:"Rejected",remark:"None"},
{ id:3,drive:"Drive 3",interview:"In-person",job:"SDE",result:"Applied",remark:"None"}
])

const selectedCompany = ref(null)
const selectedDrive = ref(null)
const showHistory = ref(false)

async function viewCompany(org){
  try {
    const res = await fetch(
      `http://127.0.0.1:5000/api/student/companies/${org.id}/drives`
    )

    console.log("API status:", res.status)

    const data = await res.json()
    console.log("Drives data:", data)

    selectedCompany.value = {
      name: org.name,
      description: org.description,
      website: org.website,
      drives: data.drives || []
    }

  } catch (err) {
    console.error("Error fetching drives:", err)
  }
}

function viewDrive(drive){
selectedDrive.value={
name:drive.name,
job:"Senior Software Developer",
location:"Chennai",
salary:"₹6,00,000",
description:"Design scalable systems and build backend services."
}
}

function applyDrive(){
alert("Application submitted!")
}
</script>