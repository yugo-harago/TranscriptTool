<template>
  <div class="text-container" @click="addTextToInput">
    <p v-html="content"></p>
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
  computed: {
    words() {
      const delimiterRegex = /([。、！？\n\{\}\[\]「」])/;
      const splittedText = this.content
        .split(delimiterRegex)
        .filter((chunk) => chunk.trim() !== "");

      return splittedText;
    },
  },
  methods: {
    async fetchText() {
      try {
        const response = await fetch("/DazaiOsamu_Uso.html");
        if (response.ok) {
          this.content = await response.text();
          await this.setFunction()
        } else {
          console.error("Error fetching text file:", response.status);
        }
      } catch (error) {
        console.error("Error fetching text file:", error);
      }
    },
    wordClick(word) {
      console.log(word.target.innerText);
    },
    setFunction() {
    this.$nextTick(() => {
      const elements = this.$el.querySelectorAll(".text-container span");
      for (const element of elements) {
        element.addEventListener("click", this.wordClick);
      }
    });
    }
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
.text-container:deep(span) {
  cursor: pointer;
  text-decoration: none;
}

.text-container:deep(span):hover {
  background-color: coral;
}
</style>
