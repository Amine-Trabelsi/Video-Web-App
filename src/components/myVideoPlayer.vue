<template>
  <div class="video-container">
    <h2>{{ video.title }}</h2>

    <vue-plyr :options="plyrOptions" @ready="onPlyrReady">
      <video :src="videoUrl" type="video/mp4">
        <!--source /-->
      </video>
    </vue-plyr>
  </div>
</template>

<script>
import VuePlyr from 'vue-plyr';
import 'vue-plyr/dist/vue-plyr.css'; // Import VuePlyr styles

export default {
  components: {
    VuePlyr,
  },
  props: {
    video: Object, // Prop to receive video data from parent component
  },
  data() {
    return {
      loaded: false,
      plyrInstance: null, // Store the VuePlyr instance
    };
  },
  computed: {
    videoUrl() {
      return this.video.file; // Use the file property from the API response
    },
    plyrOptions() {
      return {
        controls: ['play', // 'fast-forward',
           'current-time',
            'progress',  'mute', 'volume', 'fullscreen'],
          seekTime: 10,
          invertTime: false,
          toggleInvert: true,
        keyboard: { focused: true, global: true }
      };
    },
  },
  methods: {
    onPlyrReady(player) {
      this.plyrInstance = player; // Save the Plyr instance
      this.loaded = true; // Set loaded to true once Plyr is initialized
    },
  },
};
</script>

<style scoped>
.video-container {
  position: relative;
  overflow: hidden;
  margin-left: 10%;
  width: 80%;
}
</style>