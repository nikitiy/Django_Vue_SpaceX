<template>
  <div class="header">
    <div class="container">
      <div class="header__content">
        <div class="header__logo">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <img src="images/logo.png">
        </div>
        <nav class="header__navigation">
          <ul>
            <li
                v-for="link in header_navigations_data"
                :key="link.id"
            >
              <a :href="link.link">{{ link.title }}</a>
            </li>
          </ul>
        </nav>
        <div class="header__burger" @click="openBurger">
          <span></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  computed: mapGetters(['header_navigations_data']),
  methods: {
    ...mapActions(['ChangeBurgerStatus']),
    openBurger() {
      this.ChangeBurgerStatus(true);
    }
  }
}
</script>

<style lang="scss">
.header {
  position: relative;
  z-index: 1;
  background-color: rgba($color: #000, $alpha: .3);
  border-bottom: 1px solid rgba($color: #fff, $alpha: .1);
}

.header__content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header__logo {
  width: 325px;
  padding: 25px 25px 40px;
  border-left: 1px solid rgba($color: $color_white, $alpha: .1);
  border-right: 1px solid rgba($color: $color_white, $alpha: .1);
  position: relative;

  img {
    width: 100%;
  }
  span {
    position: absolute;
    display: block;
    width: 7px;
    height: 7px;

    &:nth-child(1){
      top: 0;
      left: 0;
      border-top: 1px solid $color_white;
      border-left: 1px solid $color_white;
    }
    &:nth-child(2){
      top: 0;
      right: 0;
      border-top: 1px solid $color_white;
      border-right: 1px solid $color_white;
    }
    &:nth-child(3){
      bottom: 0;
      left: 0;
      border-bottom: 1px solid $color_white;
      border-left: 1px solid $color_white;
    }
    &:nth-child(4){
      bottom: 0;
      right: 0;
      border-bottom: 1px solid $color_white;
      border-right: 1px solid $color_white;
    }
  }
}
.header__navigation {

  ul {
    display: flex;
    gap: 40px;

    li a {
      font-weight: 300;
    }
  }
}
.header__burger {
  display: none;
  width: 35px;
  height: 20px;
  position: relative;

  span {
    top: 10px;

    &, &:before, &:after {
      position: absolute;
      display: block;
      width: 100%;
      height: 2px;
      background: $color_white;
      border-radius: 2px
    }
    &:before {
      content: "";
      top: -10px;
    }
    &:after {
      content: "";
      bottom: -10px;
    }
  }
}

@media screen and (hover: hover) {
  .header__navigation ul li:hover {
    position: relative;

    &:after {
      content: "";
      position: absolute;
      left: 0;
      bottom: -9px;
      width: 100%;
      height: 1px;
      background-color: rgba($color: $color_white, $alpha: .5);
    }
    a {
      color: rgba($color: $color_white, $alpha: .5);
    }
  }
}

@media screen and (max-width: 1280px) {
  .header__logo {
    width: 230px;
    padding: 15px 15px 25px;
  }
  .header__navigation {
    font-size: 14px;
  }
  .header__navigation ul {
    gap: 30px;
  }
}
@media screen and (max-width: 1000px) {
  .header__navigation {
    display: none;
  }
  .header__burger {
    display: block;
  }
}
</style>