<template>
<div class="container-fluid p-4">

    <!-- Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h3>Company Dashboard</h3>
        <button class="btn btn-outline-danger btn-sm">Logout</button>
    </div>

    <div class="row">

        <!-- LEFT SIDE -->
        <div class="col-md-7">

            <!-- Upcoming Drives -->
            <div class="card mb-4">
                <div class="card-header d-flex justify-content-between">
                    <strong>Upcoming Drives</strong>
                    <button class="btn btn-success btn-sm">Create Drive</button>
                </div>

                <div class="card-body p-0">
                    <table class="table table-bordered mb-0">
                        <thead>
                            <tr>
                                <th>Sr No</th>
                                <th>Drive Name</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(drive,index) in upcomingDrives" :key="drive.id">
                                <td>{{ index + 1 }}</td>
                                <td>{{ drive.name }}</td>
                                <td>
                                    <button class="btn btn-primary btn-sm me-2">
                                        View Details
                                    </button>
                                    <button class="btn btn-success btn-sm">
                                        Mark Complete
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Closed Drives -->
            <div class="card">
                <div class="card-header">
                    <strong>Closed Drives</strong>
                </div>

                <div class="card-body p-0">
                    <table class="table table-bordered mb-0">
                        <thead>
                            <tr>
                                <th>Sr No</th>
                                <th>Drive Name</th>
                                <th>Actions</th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr v-for="(drive,index) in closedDrives" :key="drive.id">
                                <td>{{ index + 1 }}</td>
                                <td>{{ drive.name }}</td>
                                <td>
                                    <button class="btn btn-secondary btn-sm">
                                        Update
                                    </button>
                                </td>
                            </tr>
                        </tbody>

                    </table>
                </div>
            </div>

        </div>


        <!-- RIGHT SIDE -->
        <div class="col-md-5">

            <!-- Applications Panel -->
            <div class="card mb-4">
                <div class="card-header">
                    <strong>Applications</strong>
                </div>

                <div class="card-body">

                    <div v-for="student in students" :key="student.id"
                        class="d-flex justify-content-between align-items-center border p-2 mb-2">

                        <span>{{ student.name }}</span>

                        <button class="btn btn-info btn-sm">
                            Review Application
                        </button>

                    </div>

                    <button class="btn btn-success w-100 mt-3">
                        Save
                    </button>

                </div>
            </div>


            <!-- Student Profile Preview -->
            <div class="card">
                <div class="card-header">
                    <strong>Student Application</strong>
                </div>

                <div class="card-body">

                    <p><b>Name:</b> {{ selectedStudent.name }}</p>
                    <p><b>Department:</b> {{ selectedStudent.department }}</p>
                    <p><b>Drive:</b> {{ selectedStudent.drive }}</p>
                    <p><b>Job Title:</b> {{ selectedStudent.job }}</p>

                    <button class="btn btn-primary btn-sm me-2">
                        View Resume
                    </button>

                    <button class="btn btn-success btn-sm me-2">
                        Shortlist
                    </button>

                    <button class="btn btn-danger btn-sm">
                        Reject
                    </button>

                </div>
            </div>

        </div>

    </div>
</div>
</template>

<script setup>
import { ref } from 'vue'

const upcomingDrives = ref([
    {id:1,name:"Drive 1"},
    {id:2,name:"Drive 2"},
    {id:3,name:"Drive 3"}
])

const closedDrives = ref([
    {id:1,name:"Drive A"},
    {id:2,name:"Drive B"}
])

const students = ref([
    {id:1,name:"Student 1"},
    {id:2,name:"Student 2"},
    {id:3,name:"Student 3"},
    {id:4,name:"Student 4"}
])

const selectedStudent = ref({
    name:"Student Name",
    department:"Computer Science",
    drive:"Drive 3",
    job:"Data Scientist"
})
</script>