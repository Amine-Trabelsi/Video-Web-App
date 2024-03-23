import {createApp } from 'vue';
import App from './App.vue';

// video player
import VuePlyr from 'vue-plyr';
import 'vue-plyr/dist/vue-plyr.css'; // Import Plyr styles


const app = createApp(App);

// Register vue-plyr globally
app.use(VuePlyr);

app.mount('#app');