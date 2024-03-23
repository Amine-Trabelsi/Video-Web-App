<template>
  <div id="app">
    <AppHeader />
    <h1>Video Player</h1>
    <div class="navbar">
      <button v-for="video in videos" :key="video.id" @click="loadVideo(video.id)">
        {{ video.title }}
      </button>
    </div>
    <div v-if="isLoading" class="loading-indicator">Loading...</div>
    <my-video-player :video="videoData" v-else />
  </div>
</template>

<script>
import AppHeader from './components/mainHeader.vue';
import myVideoPlayer from './components/myVideoPlayer.vue';
import axios from 'axios';

export default {
  components: {
    AppHeader,
    myVideoPlayer,
  },
  data() {
    return {
      videos: [],
      videoData: {},
      isLoading: false,
      error: null,
    };
  },
  mounted() {
    this.fetchVideos();
  },
  methods: {
    fetchVideos() {
      this.isLoading = true;
      axios.get('http://localhost:8000/api/videos/')
        .then(response => {
          this.videos = response.data;
          console.log("finished fetching video list");
        })
        .catch(error => {
          console.error('Error fetching video list:', error);
          this.error = 'Failed to fetch videos.';
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
    loadVideo(videoId) {
      this.isLoading = true;
      this.error = null;
      axios.get(`http://localhost:8000/api/videos/${videoId}/`)
        .then(response => {
          this.videoData = response.data;
          console.log("loaded video:", response.data.title);
        })
        .catch(error => {
          console.error('Error loading video:', error);
          this.error = 'Failed to load video.';
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
  },
};
</script>

<style>
#app {
  text-align: center;
  padding: 20px;
}

h1 {
  margin-bottom: 20px;
}

.navbar {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.navbar button {
  padding: 10px 20px;
  margin: 0 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.navbar button:hover {
  background-color: #45a049;
}

.loading-indicator {
  margin-top: 20px;
}
</style>