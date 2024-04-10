<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies(){
    fetch("/api/v1/movies")
    .then(response => {
            if(response.ok){return response.json()}
            else{return Promise.reject('Something was wrong with fetch request!')}
        })
        .then(data => {
            console.log(data);
            movies.value = data["movies"]
        })
        .catch(error => {
            console.log(error);
        })
    }

    onMounted(() => {
        fetchMovies()
    });


</script>

<template>
    <div class="movies-container">
        <h1>Movies</h1>

        <div class="movies">
            <div v-for="movie in movies" class="movie">
                <div class="poster-container">
                    <img :src="movie.poster">
                </div>
                <div class="movie-details">
                    <h2>{{movie.title }}</h2>
                    <p>{{ movie.description }}</p>
                </div>
                
            </div>
        </div>

    </div>
</template>


<style>

    .movies-container{
        margin: auto 80px;
    }

    .movies{
        display: flex;
        flex-wrap: wrap;
    }
    .movie{
        max-width: 550px;
        height: 250px;
        width: 100%;
        overflow: hidden;

        display: grid;
        grid-template-columns: 1fr 2fr;

        margin: 20px;
        border-radius: 5px;
        box-shadow: 0 0 5px rgb(209, 209, 209);
    }
    .movie img{
        width: 100%;
        height: 250px;
        object-fit: contain;
    }
    .movie-details{
        padding: 15px;
    }
</style>