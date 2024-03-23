<template>
  <header>
    <nav>
      <ul>
        <li v-for="(tab, index) in tabs" :key="index" @click="selectTab(tab)">
          {{ tab.label }}
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  data() {
    return {
      tabs: [
        { label: 'Action', category: 'action' },
        { label: 'Comedy', category: 'comedy' },
        { label: 'Drama', category: 'drama' },
        // Add more tabs/categories as needed
      ],
      selectedTab: null, // Currently selected tab
    };
  },
  methods: {
    selectTab(tab) {
      // Update selectedTab when a tab is clicked
      this.selectedTab = tab.category;
      // Emit an event to notify the parent component (e.g., App.vue) about the selected tab
      this.$emit('tab-selected', tab.category);
    },
  },
};
</script>

<style scoped>
/* Add styling for tabs as needed */
nav ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

nav ul li {
  display: inline-block;
  margin-right: 20px;
  cursor: pointer;
}

nav ul li:hover {
  text-decoration: underline;
}
</style>