<template>
  <div class="text-container">
    {{ content }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      content: "",
    };
  },
  async created() {
    await this.fetchText();
  },
  methods: {
    async fetchText() {
      try {
        const response = await fetch("/DazaiOsamu_Uso.txt");
        if (response.ok) {
          this.content = await response.text();
        } else {
          console.error("Error fetching text file:", response.status);
        }
      } catch (error) {
        console.error("Error fetching text file:", error);
      }
    },
  },
};
</script>

<style scoped>
.text-container {
  column-count: auto;
  column-gap: 2rem;
  max-width: 100%;
  overflow-x: auto;
  white-space: pre-wrap;
}
</style>
