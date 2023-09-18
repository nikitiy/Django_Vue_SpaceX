<template>
  <div class="burger"
       :class="{burger_active: getBurgerStatus, burger_closing: burgerStatusClose}"
       @click.stop="closeBurger"
  >
    <div class="burger__block"
         :class="{burger__block_active: getBurgerStatus,burger__block_closing: burgerStatusClose}"
         @click.stop
    >
      <div class="burger__cross" @click="closeBurger">
        <span></span>
      </div>
      <div class="burger__content">
        <nav class="burger__navigation">
          <ul>
            <li
                v-for="link in header_navigations_data"
                :key="link.id"
            >
              <a class="burger__navigation-item" @click="closeBurger">{{ link.title }}</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  data() {
    return {
      burgerStatusClose: false,
    }
  },
  computed: {
    ...mapGetters(['getBurgerStatus', 'header_navigations_data']),
  },
  methods: {
    ...mapActions(['ChangeBurgerStatus']),
    closeBurger() {
      this.burgerStatusClose = true;
      setTimeout(() => {
        this.ChangeBurgerStatus(false);
        this.burgerStatusClose = false;
      }, 200);
    },
  },
}
</script>

<style lang="scss">
.burger {
  visibility: hidden;
  position: fixed;
  z-index: 3;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba($color: #000, $alpha: .0);
  transition: background-color .5s, visibility .1s;

  &_active {
    visibility: visible;
    background-color: rgba($color: #000, $alpha: .7);
  }

  &_closing {
    background-color: rgba($color: #000, $alpha: .0);
  }
}

.burger__block {
  background-color: #000;
  height: 100vh;
  width: 300px;
  border-left: 1px solid rgba($color: $color_white, $alpha: .17);
  position: absolute;
  right: -100%;
  overflow: scroll;
  transition: right .4s;

  &_active {
    right: 0;
  }

  &_closing {
    right: -100%;
  }
}

.burger__content {
  min-height: auto;
  position: relative;
  top: 50%;
  transform: translate(0, -50%);
}

.burger__navigation {
  text-align: center;

  ul {
    display: flex;
    flex-direction: column;
    gap: 35px;

    li {

      .burger__navigation-item {
        font-size: 20px;
      }
    }
  }
}

.burger__cross {
  width: 35px;
  height: 35px;
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  justify-content: center;
  align-items: center;

  span {
    rotate: 45deg;

    &, &:before {
      width: 100%;
      height: 2px;
      background-color: $color_white;
      display: block;
    }

    &:before {
      content: "";
      rotate: 90deg;
    }
  }
}
</style>