<template>
<div>

    <!-- Header -->

    <div class="mb-4">
        <h1 class="fw-bold">Dashboard</h1>
        <p class="text-muted">
            Welcome back to your placement dashboard.
        </p>
    </div>

    <!-- Stats -->

    <div class="row g-4 mb-4">

        <div class="col-md-3">
            <div class="card stat-card">
                <h2>{{ organizations.length }}</h2>
                <span>Total Companies</span>
            </div>
        </div>

        <div class="col-md-3">
            <div class="card stat-card">
                <h2>{{ appliedDrives.length }}</h2>
                <span>Applied</span>
            </div>
        </div>

        <div class="col-md-3">
            <div class="card stat-card">
                <h2>2</h2>
                <span>Selected</span>
            </div>
        </div>

        <div class="col-md-3">
            <div class="card stat-card">
                <h2>5</h2>
                <span>Upcoming</span>
            </div>
        </div>

    </div>

    <div class="row">

        <!-- LEFT -->

        <div class="col-lg-6">

            <div class="card shadow-sm mb-4">

                <div class="card-header">
                    <strong>Organizations</strong>
                </div>

                <div class="card-body">

                    <div
                    v-for="org in organizations"
                    :key="org.id"
                    class="company-row">

                        <div>
                            {{ org.name }}
                        </div>

                        <button
                        class="btn btn-primary btn-sm"
                        @click="viewCompany(org)">
                            View
                        </button>

                    </div>

                </div>

            </div>

            <div class="card shadow-sm">

                <div class="card-header">
                    <strong>Applied Drives</strong>
                </div>

                <div class="card-body p-0">

                    <table class="table mb-0">

                        <thead>

                            <tr>
                                <th>#</th>
                                <th>Drive</th>
                                <th>Company</th>
                                <th>Date</th>
                            </tr>

                        </thead>

                        <tbody>

                            <tr
                            v-for="(drive,index) in appliedDrives"
                            :key="drive.id">

                                <td>{{ index+1 }}</td>
                                <td>{{ drive.name }}</td>
                                <td>{{ drive.company }}</td>
                                <td>{{ drive.date }}</td>

                            </tr>

                        </tbody>

                    </table>

                </div>

            </div>

        </div>

        <!-- RIGHT -->

        <div class="col-lg-6">

            <div
            v-if="selectedCompany"
            class="card shadow-sm mb-4">

                <div class="card-header">
                    <strong>
                        {{ selectedCompany.name }}
                    </strong>
                </div>

                <div class="card-body">

                    <p>
                        {{ selectedCompany.description }}
                    </p>

                    <h6 class="mt-4">
                        Available Drives
                    </h6>

                    <div
                    v-for="drive in selectedCompany.drives"
                    :key="drive.id"
                    class="company-row">

                        <span>
                            {{ drive.name }}
                        </span>

                        <button
                        class="btn btn-primary btn-sm"
                        @click="viewDrive(drive)">
                            Details
                        </button>

                    </div>

                </div>

            </div>

            <div
            v-if="selectedDrive"
            class="card shadow-sm">

                <div class="card-header">
                    <strong>
                        {{ selectedDrive.name }}
                    </strong>
                </div>

                <div class="card-body">

                    <p>
                        <b>Role:</b>
                        {{ selectedDrive.job }}
                    </p>

                    <p>
                        <b>Location:</b>
                        {{ selectedDrive.location }}
                    </p>

                    <p>
                        <b>Salary:</b>
                        {{ selectedDrive.salary }}
                    </p>

                    <p>
                        {{ selectedDrive.description }}
                    </p>

                    <button
                    class="btn btn-success"
                    @click="applyDrive">
                        Apply Now
                    </button>

                </div>

            </div>

        </div>

    </div>

</div>
</template>

<script setup>
import { ref,onMounted } from "vue"

const organizations = ref([])
const selectedCompany = ref(null)
const selectedDrive = ref(null)

const appliedDrives = ref([
{
id:1,
name:"Software Engineer",
company:"Infosys",
date:"24/09/2025"
},
{
id:2,
name:"Data Analyst",
company:"TCS",
date:"30/09/2025"
}
])

onMounted(async()=>{

    try{

        const res = await fetch(
        "http://127.0.0.1:5000/api/student/companies"
        )

        const data = await res.json()

        organizations.value =
        data.companies || []
        console.log(organizations.value)

    }

    catch(err){
        console.log(err)
    }

})

async function viewCompany(org){

    try{

        const res = await fetch(
        `http://127.0.0.1:5000/api/student/companies/${org.id}/drives`
        )

        const data = await res.json()

        selectedCompany.value = {

            name:org.name,
            description:org.description,
            drives:data.drives || []

        }

    }

    catch(err){

        console.log(err)

    }

}

function viewDrive(drive){

    selectedDrive.value = {

        name:drive.name,
        job:"Software Engineer",
        location:"Bangalore",
        salary:"₹8 LPA",
        description:
        "Build scalable backend systems."

    }

}

function applyDrive(){

    alert("Application Submitted")

}
</script>

<style scoped>
.stat-card{
    padding:20px;
    text-align:center;
}

.stat-card h2{
    margin-bottom:10px;
}

.company-row{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:12px;
    border:1px solid #e5e7eb;
    border-radius:10px;
    margin-bottom:10px;
}
</style>