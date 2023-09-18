<template>
  <section class="main">
    <header-block/>
    <welcome-block/>
  </section>
  <burger-menu/>
</template>

<script>

import HeaderBlock from "@/components/HeaderBlock.vue";
import WelcomeBlock from "@/components/WelcomeBlock.vue";
import {mapActions} from "vuex";
import BurgerMenu from "@/components/BurgerMenu.vue";

export default {
  name: 'App',
  components: {
    BurgerMenu,
    WelcomeBlock,
    HeaderBlock
  },
  methods: mapActions(['getPageData']),
  beforeMount() {
    this.getPageData();
  }
}
</script>

<style lang="scss">
.main {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  position: relative;
  background: url("@/assets/images/space.png") no-repeat center center;
  background-size: cover;
}
</style>
