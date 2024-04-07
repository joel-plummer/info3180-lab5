<template>
    <h1>Upload Form</h1>
    <form @submit.prevent="saveMovie" id="movieForm">
        <div v-if="result.errors">
            <ul class="alert alert-danger">
                <li v-for="error in result.errors">{{ error }}</li>
            </ul>
        </div>
        <div v-if="result.message">
            <div class="alert alert-success">{{ result.message }}</div>
        </div>
        <div class="form-group">
            <label for="title" class="form-label">Movie Title</label>
            <input name="title" type="text" class="form-control">
        </div>
        <div class="form-group">
            <label for="description" class="form-label">Description</label>
            <textarea row="10" name="description" class="form-control" />
        </div>
        <div class="form-group">
            <label for="poster" class="form-label">Upload file</label>
            <input type="file" name="poster" class="form-control-file">
        </div>
        <input type="submit">
    </form>
</template>

<script setup>

    import {ref, onMounted} from 'vue'
    let csrf_token = ref("")
    let result = ref([])

    const getCsrfToken = () => {
        fetch('/api/v1/csrf-token')
        .then(res => res.json())
        .then(data => {
            // console.log(data)
            csrf_token.value = data.csrf_token
        })
    }

    onMounted(() => {
        getCsrfToken()
    })

    const saveMovie = () => {
        let movieForm = document.getElementById("movieForm")
        let form_data = new FormData(movieForm)
        // console.log(...form_data.entries())
        fetch("/api/v1/movies", {
            method: "POST",
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
        .then(res => res.json())
        .then(data => {
            result.value = data
            console.log(data)
        })
        .catch(err => result.value = err)
    }

</script>


<style>
    form {
        display: flex;
        flex-direction: column;
    }
    .form-group {
        display: flex;
        flex-direction: column;
        margin: 10px 0;
    }

    .form-group > label {
        font-weight: bold;
    }

    input[type="submit"] {
        margin-top: 20px;
        width: 100px;
        border: none;
        background: rgb(76, 120, 240);
        border-radius: 5%;
        color: #fff;
    }

    input[type="submit"]:hover {
        cursor: pointer;
        background: rgb(6, 24, 104);
    }

    .alert {
        padding-left: 50px;
    }

</style>