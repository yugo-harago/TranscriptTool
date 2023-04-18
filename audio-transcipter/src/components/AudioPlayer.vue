<!-- src/components/AudioPlayer.vue -->
<template>
    <div class="audio-player">
      <div ref="waveform" class="waveform"></div>
      <div class="controls">
        <button @click="playPause">{{ isPlaying ? 'Pause' : 'Play' }}</button>
        <div class="progress">
          <div class="progress-bar" :style="{ width: progress + '%' }"></div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import WaveSurfer from 'wavesurfer.js';

  export default {
    props: ['audioUrl'],
    data() {
  return {
    wavesurfer: null,
    isPlaying: false,
    progress: 0,
    initialized: false,
  };
},
mounted() {
  this.wavesurfer = WaveSurfer.create({
    container: this.$refs.waveform,
    waveColor: 'violet',
    progressColor: 'purple',
    barWidth: 2,
    partialRender: true,
  });

  this.wavesurfer.on('play', () => (this.isPlaying = true));
  this.wavesurfer.on('pause', () => (this.isPlaying = false));
  this.wavesurfer.on('finish', () => (this.isPlaying = false));
  this.wavesurfer.on('audioprocess', this.updateProgress);
},
methods: {
    async initialize() {
        if (!this.initialized) {
            await this.wavesurfer.load(this.audioUrl);
            this.initialized = true;
        }
    },
    async playPause() {
        await this.initialize();
        this.wavesurfer.playPause();
    },
    updateProgress() {
        this.progress = (this.wavesurfer.getCurrentTime() / this.wavesurfer.getDuration()) * 100;
    },
},
  }
  </script>
  
  <style scoped>
  .audio-player {
    position: relative;
    width: 100%;
  }
  
  .waveform {
    height: 100px;
  }
  
  .controls {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .progress {
    position: relative;
    flex-grow: 1;
    height: 5px;
    background-color: #eee;
    margin-left: 10px;
  }
  
  .progress-bar {
    position: absolute;
    height: 100%;
    background-color: violet;
  }
  </style>
  