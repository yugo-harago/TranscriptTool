<template>
  <div class="mb-1 bg-light fixed-top">
    <div
      class="container-fluid d-xl-flex align-items-xl-center py-1"
      style="height: 205px"
    >
      <AudioPlayer :audioUrl="audioUrl"></AudioPlayer>
    </div>
  </div>
  <section>
    <div class="container" style="margin-top: 205px">
      <div class="col">
        <Text />
      </div>
    </div>
  </section>
</template>

<script>
import AudioPlayer from "./AudioPlayer.vue";
import Text from "./Text.vue";
import audioFile from "../assets/DazaiOsamu_Uso.mp3";

export default {
  components: {
    AudioPlayer,
    Text,
  },
  data() {
    return {
      audioUrl: audioFile,
    };
  },
};
</script>
<style scoped>
.read-the-docs {
  color: #888;
}
</style>
