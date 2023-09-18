<template>
  <div class="welcome">
    <div class="container">
      <div class="welcome__content">
        <div class="welcome__title">
          <h1 class="title title_start">Путешествие</h1>
          <p>на красную планету</p>
        </div>
        <img class="welcome__background-mars" src="images/mars.png" alt="">
        <button class="welcome__button">
          Начать путешествие
          <img class="welcome__rectangle" src="images/rectangle.png" alt="">
        </button>
        <div class="welcome__advantages">
          <div class="welcome__advantages-item"
               v-for="adventage in adventages_data"
               :key="adventage.id"
          >
            {{ adventage.adventage_row_1 }}
            <span v-html="adventage.adventage_row_2"></span>
            {{ adventage.adventage_row_3 }}
          </div>
        </div>
        <img class="welcome__figure" src="images/figure.png" alt="">
        <img class="welcome__background-image" src="images/background1.png" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  computed: mapGetters(['adventages_data']),
  mounted() {

    if (!('ontouchstart' in window)) {
      const mars = document.querySelector('.welcome__background-mars');
      const figure = document.querySelector('.welcome__figure');
      const rectangle = document.querySelector('.welcome__button');
      window.addEventListener('mousemove', function (e) {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;

        mars.style.transform = 'translate(calc(-50% - ' + x * 15 + 'px), calc(-50% - ' + y * 15 + 'px))';
        figure.style.transform = 'translate(calc(-100% - ' + x * 15 + 'px), -' + y * 15 + 'px)';
        rectangle.style.transform = 'translate(-' + x * 15 + 'px, -' + y * 15 + 'px)';
      });
    }
  }
}
</script>

<style lang="scss">
.welcome {
  flex: 1 0 auto;
  width: 100%;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.welcome__content {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.welcome__title {
  padding-top: 56px;
  background-color: #fff;
  background-image: linear-gradient(100deg, #fff, #ff440b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;

  p {
    font-size: 25px;
    font-weight: 300;
    text-transform: lowercase;
    background-color: #fff;
    background-image: linear-gradient(110deg, #fff, #ff440b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
}

.welcome__advantages {
  width: 382px;
  height: 382px;
  display: inline-grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}

.welcome__advantages-item {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;

  &:nth-child(4n + 1) {
    background: linear-gradient(to top left, rgba($color: $color_white, $alpha: .04) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
  }

  &:nth-child(4n + 2) {
    background: linear-gradient(to top right, rgba($color: $color_white, $alpha: .04) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
  }

  &:nth-child(4n + 3) {
    background: linear-gradient(to bottom left, rgba($color: $color_white, $alpha: .04) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
  }

  &:nth-child(4n + 4) {
    background: linear-gradient(to bottom right, rgba($color: $color_white, $alpha: .04) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
  }

  span {
    font-size: 60px;
    font-weight: 700;
    margin-top: 20px;

    span {
      font-size: 20px;
    }
  }
}

.welcome__button {
  position: absolute;
  display: block;
  width: 210px;
  height: 65px;
  left: 40px;
  top: 60%;
  background-color: rgba($color: #000, $alpha: 0);
  color: $color_white;
}

.welcome__rectangle {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
}

.welcome__figure {
  width: 406px;
  position: absolute;
  z-index: 1;
  top: 68%;
  left: 50.22%;
  transform: translate(-100%, 0);
}

.welcome__background-image {
  position: absolute;
  z-index: -1;
  top: 50%;
  left: 47.8%;
  transform: translate(-50%, -50%);
  max-width: 985px;
  width: 70%;
}

.welcome__background-mars {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  max-width: 385px;
  width: 30%;
}

@media screen and (hover: hover) {
  .welcome__advantages-item:hover {

    &:nth-child(4n + 1) {
      border: 1px solid;
      border-image-slice: 1;
      border-width: 1px;
      border-image-source: linear-gradient(to top left, rgba($color: $color_white, $alpha: .2) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
      border-top: 0;
      border-left: 0;
      background: linear-gradient(to top left, rgba($color: $color_white, $alpha: .09) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
    }

    &:nth-child(4n + 2) {
      border: 1px solid;
      border-image-slice: 1;
      border-width: 1px;
      border-image-source: linear-gradient(to top right, rgba($color: $color_white, $alpha: .2) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
      border-top: 0;
      border-right: 0;
      background: linear-gradient(to top right, rgba($color: $color_white, $alpha: .09) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
    }

    &:nth-child(4n + 3) {
      border: 1px solid;
      border-image-slice: 1;
      border-width: 1px;
      border-image-source: linear-gradient(to bottom left, rgba($color: $color_white, $alpha: .2) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
      border-bottom: 0;
      border-left: 0;
      background: linear-gradient(to bottom left, rgba($color: $color_white, $alpha: .09) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
    }

    &:nth-child(4n + 4) {
      border: 1px solid;
      border-image-slice: 1;
      border-width: 1px;
      border-image-source: linear-gradient(to bottom right, rgba($color: $color_white, $alpha: .2) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
      border-bottom: 0;
      border-right: 0;
      background: linear-gradient(to bottom right, rgba($color: $color_white, $alpha: .09) 25%, rgba($color: $color_white, $alpha: 0) 50% 100%);
    }
  }
}

@media screen and (max-width: 1280px) {
  .welcome__title {
    padding-top: 50px;
  }
  .welcome__title p {
    font-size: 20px;
  }
  .welcome__advantages {
    width: 292px;
    height: 292px;
  }
  .welcome__advantages-item {
    font-size: 14px;

    span {
      font-size: 46px;
    }
  }
  .welcome__button {
    width: 190px;
    left: 25px;
    top: 58%;
  }
  .welcome__figure {
    width: 300px;
  }
}
@media screen and (max-width: 1000px) {
  .welcome {
    position: relative;
    top: auto;
    left: auto;
    transform: translate(0, 0);
    padding-bottom: 50px;
  }
  .welcome__content {
    flex-direction: column;
    align-items: center;
    gap: 40px;
  }
  .welcome__title {
    padding-top: 30px;
    text-align: center;
    background-image: linear-gradient(to bottom, #fff 40%, #ff440b 90%);

    .title {
      font-size: 60px;
    }
  }
  .welcome__title p {
    font-size: 26px;
    background-image: linear-gradient(to bottom, #fff 40%, #ff440b 90%);
  }
  .welcome__background-mars {
    position: relative;
    top: auto;
    left: auto;
    transform: translate(0, 0);
    width: 370px;
  }
  .welcome__advantages {
    width: 400px;
    height: 400px;
  }
  .welcome__advantages-item {
    font-size: 16px;
  }
  .welcome__advantages-item span {
    font-size: 60px;
    margin-top: 15px;
  }
  .welcome__button {
    top: 385px;
    left: 15px;
    width: 190px;
    font-size: 14px;
  }
  .welcome__figure {
    width: 285px;
    top: 430px;
  }
  .welcome__background-image {
    top: 370px;
    width: 750px;
  }
}
@media screen and (max-width: 800px) {
  .welcome__button {
    width: 260px;
    height: 100px;
    top: 490px;
    left: auto;
    transform: translate(0, 0);
    font-size: 18px;
  }
  .welcome__advantages {
    width: 350px;
    height: 350px;
  }
  .welcome__figure {
    display: none;
  }
}
@media screen and (max-width: 600px) {
  .header__logo {
    width: 180px;
  }
  .welcome__title .title {
    font-size: 40px;
  }
  .welcome__title p {
    font-size: 20px;
  }
  .welcome__advantages {
    width: 300px;
    height: 300px;

    span {
      font-size: 50px;
    }
  }
  .welcome__background-mars {
    width: 330px;
  }
  .welcome__background-image {
    top: 300px;
    width: 750px;
  }
  .welcome__button {
    top: 420px;
    height: 90px;
  }
}
@media screen and (max-width: 400px) {
  .header__logo {
    width: 140px;
    padding: 10px 10px 20px;
  }
  .welcome__title .title {
    font-size: 32px;
  }
  .welcome__title p {
    font-size: 16px;
  }
  .welcome__advantages {
    width: 250px;
    height: 250px;
    font-size: 13px;

    span {
      font-size: 40px;
    }
  }
  .welcome__background-mars {
    width: 280px;
  }
  .welcome__background-image {
    top: 260px;
    width: 670px;
  }
  .welcome__button {
    width: 230px;
    top: 360px;
    height: 80px;
    font-size: 14px;
  }
}
</style>
