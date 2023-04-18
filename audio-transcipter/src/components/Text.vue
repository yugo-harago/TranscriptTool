<template>
  <div>
    <pre>{{ content }}</pre>
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
