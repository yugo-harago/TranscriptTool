

<template>
  <!-- <div class="p-2 mb-1 bg-light">
      <div class="container-fluid d-xl-flex align-items-xl-center py-1" style="height: 205px;">
          <div style="height: 92px;background: #ffe39a;width: 100%;"></div>
      </div>
  </div> -->
  <AudioPlayer :audioUrl="audioUrl"></AudioPlayer>
  <section>
      <div class="container">
          <div class="col">
              <p><span style="color: rgb(102, 102, 102);">「戦争が終ったら、こんどはまた急に何々主義だの、何々主義だの、あさましく騒ぎまわって、演説なんかしているけれども、私は何一つ信用できない気持です。主義も、思想も、へったくれも要らない。男は嘘をつく事をやめて、女は慾を捨てたら、それでもう日本の新しい建設が出来ると思う。」</span><br><span style="color: rgb(102, 102, 102);">　私は焼け出されて津軽の生家の居候になり、鬱々として楽しまず、ひょっこり訪ねて来た小学時代の同級生でいまはこの町の名誉職の人に向って、そのような八つ当りの愚論を吐いた。名誉職は笑って、</span><br><span style="color: rgb(102, 102, 102);">「いや、ごもっとも。しかし、それは、逆じゃありませんか。男が慾を捨て、女が嘘をつく事をやめる、とこう来なくてはいけません。」といやにはっきり反対する。</span><br><span style="color: rgb(102, 102, 102);">　私はたじろぎ、</span><br><br></p>
          </div>
      </div>
  </section>
</template>

<script>
import AudioPlayer from './AudioPlayer.vue';
import audioFile from '../assets/rd480.mp3';

export default {
  components: {
    AudioPlayer,
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
