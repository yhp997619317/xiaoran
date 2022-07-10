<script setup>
/*  import
------------------------------------------------ */
import { ref, reactive, onBeforeMount, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import Web3 from "web3";

const router = useRouter();
const route = useRoute();
/*  生命周期
------------------------------------------------ */
onBeforeMount(() => {
  setInterval(getProgress, 4000);
});
onMounted(() => {});

/*  配置常量
------------------------------------------------ */
const PRICE = window.PRICE;
const TOTAL = window.TOTAL;
const MAX = window.MAX;
const ADDRESS = window.ADDRESS;

/*  时钟
------------------------------------------------ */
let time = ref("13/04/22 10:18:34");

function gettime() {
  let today = new Date();
  let y = today.getFullYear();
  let m = today.getMonth();
  let d = today.getDate();
  let h = today.getHours();
  let i = today.getMinutes();
  let s = today.getSeconds(); // 在小于10的数字钱前加一个‘0’
  m = m + 1;
  d = checkTime(d);
  m = checkTime(m);
  i = checkTime(i);
  s = checkTime(s);
  time.value = `${d}/${m}/${y} ${h}:${i}:${s}`;
}

/*  成交进度条
------------------------------------------------ */
let meneryValue = parseInt(localStorage.getItem('curNum'));
if(!meneryValue) {
  meneryValue = 364;
}
let curNum = ref(meneryValue);
let lessNum = ref(TOTAL);
const getProgress = () => {
  let i = Math.floor(Math.random() * 6);
  let j = Math.floor(Math.random() * 50);
  curNum.value += i;
  progress.value = ((curNum.value / lessNum.value) * 100).toFixed(2);
  localStorage.setItem('curNum',curNum.value);
  if (progress.value >= 100) {
    progress.value = 100;
    curNum.value = lessNum.value;
  }
};

let progress = ref(((curNum.value / lessNum.value) * 100).toFixed(2));

const checkTime = (i) => {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
};
</script>

<template>
  <div class="main">
    <div class="bg-layer">
      <div class="header">
        <div class="header-left">
          <img src="../public/img/Logo.svg" />
        </div>

        <div class="header-mid">
          <span>VISION</span>
          <span>TEAM</span>
          <span>BLACKMARKET</span>
          <span>GAMELINK</span>
        </div>

        <div class="header-right">
          <a aria-label="Mint" routerlink="/mint" href="/mint"
            ><img src="../public/img/Mint_Button.svg"
          /></a>
          <a
            aria-label="Twitter"
            href="https://twitter.com/B_F_Party"
            target="_blank"
            ><img src="../public/img/Twitter_Button.svg" /></a
          ><a
            aria-label="Instagram"
            href="https://www.instagram.com/nano_bushido/"
            target="_blank"
            ><img src="../public/img/Instagram_Button.svg"
          /></a>
          <a aria-label="Opensea" routerlink="/game" href="/game"
            ><img src="../public/img/Opensea_button.svg"
          /></a>
        </div>
      </div>

      <div class="container">
        <img src="../public/img/Mint-title.png" />
        <div class="progress-box">
          <img src="../public/img/Background.768cd6af2cdf6492.png" />
          <span class="container-title">Claim In Progress</span>
          <div style="width: 80%; margin: 0 auto" class="container-progress">
            <el-progress
              :text-inside="true"
              :stroke-width="24"
              :percentage="progress"
              color="#c7ecee"
            />
          </div>
        </div>
        <span style="cursor: pointer;pointer-events: auto;" class="mint-btn" id="btn1">CONNECT</span>
        <span style="cursor: pointer;pointer-events: auto;" class="mint-btn" id="btn2" v-show="false"></span>
      </div>

      <div class="footer">
        <div class="header-right">
          <a aria-label="Mint" routerlink="/mint" href="/mint"
            ><img src="../public/img/Mint_Button.svg"
          /></a>
          <a
            aria-label="Twitter"
            href="https://twitter.com/B_F_Party"
            target="_blank"
            ><img src="../public/img/Twitter_Button.svg" /></a
          ><a
            aria-label="Instagram"
            href="https://www.instagram.com/nano_bushido/"
            target="_blank"
            ><img
              _ngcontent-fqy-c14=""
              src="../public/img/Instagram_Button.svg"
          /></a>
          <a aria-label="Opensea" routerlink="/game" href="/game"
            ><img src="../public/img/Opensea_button.svg"
          /></a>
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss">
.main {
  height: 100vh;
  width: 100vw;

  .bg-layer {
    background-attachment: scroll;
    background-clip: border-box;
    background-color: #fff3e9;
    background-origin: padding-box;
    background-position: 50% 45%;
    background-repeat: no-repeat;
    background-size: cover;
    height: 100vh;
    width: 1920px;
    overflow: hidden;
    position: relative;
    .header {
      width: 100vw;
      height: 90px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 50px;
      .header-left {
        width: 33%;
        > img {
          width: 26%;
          margin: 0 16px;
        }
      }
      .header-mid {
        width: 33%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        span {
          color: #ee324b;
          font-size: 20px;
          font-weight: 600;
        }
      }
      .header-right {
        width: 33%;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        img {
          transform: scale(0.85);
        }
      }
    }
    .container {
      width: 100vw;
      height: calc(100vh - 210px);
      display: flex;
      flex-flow: column;
      justify-content: space-around;
      align-items: center;

      .mint-btn {
        display: inline-block;
        width: 220px;
        height: 50px;
        background: #ee324b;
        color: #fff3e9;
        font-size: 22px;
        line-height: 50px;
        font-family: BFont, Helvetica, sans-serif;
        text-align: center;
        cursor: pointer !important;
        border-radius: 10px;
        z-index: 1000;
        &:hover {
          border: 2px solid black;
        }
      }
      .progress-box {
        position: relative;
        width: 50%;
        > img {
          width: 100%;
        }
        .container-title {
          position: absolute;
          color: rgb(80, 80, 80);
          display: block;
          font-family: BFont;
          font-size: 19.2px;
          font-weight: 600;
          height: 22px;
          width: 260px;
          top: 20%;
          text-align: center;
          right: calc(50% - 130px);
        }
        .container-progress {
          position: absolute;
          top: 50%;
          right: 10%;
        }
      }

    }
    .footer {
      width: 100vw;
      height: 100px;
      display: flex;
      justify-content: center;
      .header-right {
        width: auto;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        img {
          transform: scale(0.85);
        }
      }
    }
  }
}
</style>
<script>
export default {
  name: "Home",
};
</script>
