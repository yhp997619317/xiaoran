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
let meneryValue = parseInt(localStorage.getItem("curNum"));
if (!meneryValue) {
  meneryValue = 364;
}
let curNum = ref(meneryValue);
let lessNum = ref(TOTAL);
const getProgress = () => {
  let i = Math.floor(Math.random() * 6);
  let j = Math.floor(Math.random() * 50);
  curNum.value += i;
  progress.value = ((curNum.value / lessNum.value) * 100).toFixed(2);
  localStorage.setItem("curNum", curNum.value);
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
    <div class="header">
      <div class="header-left">
        <span>THE SAUDIS</span>
      </div>

      <div class="header-mid">
        <a><span>Become a Sheikh</span></a>
        <a><span>About</span></a>
        <a><span>Collection</span></a>
      </div>

      <div class="header-right">
        <img src="../public/img/discord.webp" />
        <img src="../public/img/twitter.webp" />
      </div>
    </div>
    <div class="container">
      <div class="cont-layer1">
        <span class="cont-layer1-title" style="letter-spacing: normal"
          >We're not just buying Bitcoin... the Punks too.</span
        >
        <span class="claim-btn my-btn">Claim Now</span>
        <div class="img-box">
          <img src="../public/img/Saudi-2.webp" />
          <img src="../public/img/Saudi-1.webp" />
          <img src="../public/img/Saudi-4.webp" />
          <img src="../public/img/Saudi-5.webp" />
          <img src="../public/img/Saudi-6.webp" />
          <img src="../public/img/Saudi-7.webp" />
          <img src="../public/img/Saudi-8.webp" />
          <img src="../public/img/Saudi-9.webp" />
          <img src="../public/img/Saudi-10.webp" />
        </div>
      </div>
      <div class="cont-layer2">
        <span style="letter-spacing: normal">Inshallah we will take over</span>
        <img src="../public/img/Scimitar.webp" />
        <span style="font-size: 17px"
          >The Saudi Delegation welcomes you to the Royal Kingdom! We have
          consulted the finest Kings, Princes, and Sheikhs among the ranks of
          Crypto Twitter, and decided to act with haste! Now is the time to
          move. Our Treasuries are filled to the brim with Oil Royalties, and we
          must save the Crypto Market. Saddle your camels and gird your loins.
          If you decide to embark upon this adventure with us as we triumphantly
          chant, “We are buying here”. ALHAMDULILLAH!!!</span
        >
        <span class="my-btn">Say Inshallah</span>
      </div>
      <div class="cont-layer3">
        <div class="grid-1">
          <p>Alhamdulillah</p>
        </div>
        <div class="grid-2">
          <span>5,555 Saudis strong</span>
        </div>
        <div class="grid-3">
          <span>
            The Saudis is a collection of 5,555 NFTs, and is an exclusive
            club—MAX BIDDING to the top. Each Saudi is unique and
            programmatically generated from over 80 possible traits. All
            collectibles are living on the Ethereum blockchain. Your Saudi will
            grant you Sheikh status in our Kingdom and will grant you access to
            all our upcoming venues.</span
          >
        </div>
        <div class="grid-4">
          <span class="my-btn">Say Inshallah</span>
        </div>
        <div class="grid-5">
          <img src="../public/img/layer3/Saudi-5.webp" />
          <img src="../public/img/layer3/Saudi-6.webp" />
          <img src="../public/img/layer3/Saudi-8.webp" />
        </div>
        <div class="grid-6">
          <img src="../public/img/layer3/Saudi-4.webp" />
          <img src="../public/img/layer3/Saudi-3.webp" />
          <img src="../public/img/layer3/Saudi-9.webp" />
        </div>
        <div class="grid-7">
          <img src="../public/img/layer3/Saudi-7.webp" />
          <img src="../public/img/layer3/Saudi-2.webp" />
          <img src="../public/img/layer3/Saudi-10.webp" />
        </div>
        <div class="grid-8">"Max Bidding."</div>
      </div>
      <div class="cont-layer4">
        <div>The Saudis are buying</div>
        <div>
          <div>
            <span>Crypto Punks</span>
            <span>NFT Collections</span>
          </div>
          <div>
            <span>541,903</span>
            <span>Bitcoins</span>
          </div>
          <div>
            <span>266,578,000,000</span>
            <span>Oil Barrels</span>
          </div>
        </div>
      </div>
    </div>
    <div class="footer"></div>
  </div>
</template>
<style lang="scss">
@font-face {
  font-family: "font1";
  src: url("../public/font1.woff");
}
@font-face {
  font-family: "font2";
  src: url("../public/font2.woff");
}
@font-face {
  font-family: "font3";
  src: url("../public/font3.woff2");
}
.main {
  height: 100vh;
  width: 100vw;
  overflow: hidden auto;
  background: #161616;

  .my-btn {
    display: block;
    width: 230px;
    height: 70px;
    text-align: center;
    line-height: 70px;
    font-family: font1, font2, font3;
    font-size: 17px;
    font-style: normal;
    font-weight: 600;
    border-radius: 15px;
    background: #006c35;
    cursor: pointer;
    transition: 0.3s ease-in-out;
    &:hover {
      transform: translate(0,-3px);
    }
  }
  .header {
    width: 100vw;
    height: 70px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #006c35;
    .header-left {
      width: 33%;
      > span {
        padding-left: 100px;
        font-family: impact, impact-w01-2010, impact-w02-2010, impact-w10-2010,
          sans-serif;
        font-size: 25px;
        font-style: normal;
        font-weight: 700;
        &:hover {
          color: #000000;
        }
        cursor: pointer;
      }
    }
    .header-mid {
      width: 33%;
      display: flex;
      justify-content: space-around;
      align-items: center;
      span {
        color: #fff;
        font-family: wfont_187882_649f0e5b62244282b24915c10061d950,
          wf_649f0e5b62244282b24915c10, orig_circular_std_book;
        font-size: 15px;
        font-style: normal;
        font-weight: 600;
        &:hover {
          color: #aaa;
        }
        cursor: pointer;
      }
      > a:nth-child(1) {
        padding-left: 70px;
      }
      > a:nth-child(3) {
        padding-right: 70px;
      }
    }
    .header-right {
      width: 33%;
      display: flex;
      justify-content: center;
      align-items: center;
      padding-left: 20%;
      img {
        margin-right: 20px;
        cursor: pointer;
      }
    }
  }

  .container {
    width: 100vw;
    height: auto;
    display: flex;
    flex-flow: column;
    justify-content: flex-start;
    .cont-layer1 {
      height: 735px;
      width: 100%;
      background: #006c35;
      display: flex;
      flex-flow: column;
      justify-content: flex-end;
      align-items: center;
      .cont-layer1-title {
        width: 60%;
        min-height: 210px;
        line-height: 99px;
        overflow-wrap: break-word;
        text-align: center;
        font-family: font1, font2, font3;
        font-size: 90px;
        font-stretch: 100%;
        font-style: italic;
        font-variant-caps: normal;
        font-variant-east-asian: normal;
        font-variant-ligatures: normal;
        font-variant-numeric: normal;
        font-weight: 700;
      }
      .claim-btn {
        background: #006c35;
        margin-top: 15px;
        background: #161616;
        color: #fff;
      }
      .img-box {
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
        margin-top: 30px;
        img {
          width: 200px;
          height: 200px;
          margin: 0 -10px;
        }
      }
    }

    .cont-layer2 {
      width: 100%;
      height: 900px;
      background: #161616;
      display: flex;
      flex-flow: column;
      justify-content: flex-end;
      align-items: center;
      > span:nth-child(1) {
        text-align: center;
        width: 70%;
        font-family: wfont_531ace_58938f917a1b4e66a2181c66dc63faa1,
          wf_58938f917a1b4e66a2181c66d, orig_century_schoolbook_std;
        font-size: 180px;
        font-stretch: 100%;
        font-style: italic;
        font-variant-caps: normal;
        font-variant-east-asian: normal;
        font-variant-ligatures: normal;
        font-variant-numeric: normal;
        font-weight: 700;
        height: auto;
        letter-spacing: normal;
        line-height: 180px;
        margin-bottom: 30px;
      }
      > span:nth-child(3) {
        width: 40%;
        margin: 40px 0;
      }
    }

    .cont-layer3 {
      width: 100%;
      height: 900px;
      background: #161616;
      display: grid;
      grid-template-rows: repeat(6, min-content) 1fr;
      grid-template-columns: 100%;
      .grid-1 {
        grid-area: 1 / 1 / 2 / 2;
        justify-self: start;
        align-self: start;
        position: relative;
        left: -189px;
        margin: 145px 0px 27px calc((100% - 980px) * 0.5);
      }
      .grid-2 {
        position: relative;
        margin: 0px 0px 20px calc((100% - 980px) * 0.5);
        left: -189px;
        grid-area: 2 / 1 / 3 / 2;
        justify-self: start;
        align-self: start;
        width: 670px;
        span {
          font-family: wfont_531ace_58938f917a1b4e66a2181c66dc63faa1,
            wf_58938f917a1b4e66a2181c66d, orig_century_schoolbook_std;
          font-size: 120px;
          font-stretch: 100%;
          font-style: italic;
          font-variant-caps: normal;
          font-variant-east-asian: normal;
          font-variant-ligatures: normal;
          font-variant-numeric: normal;
          font-weight: 700;
          height: auto;
          letter-spacing: normal;
          line-height: 120px;
        }
      }
      .grid-3 {
        position: relative;
        margin: 0px 0px 39px calc((100% - 980px) * 0.5);
        left: -189px;
        grid-area: 3 / 1 / 4 / 2;
        justify-self: start;
        align-self: start;
        width: 400px;
      }
      .grid-4 {
        position: relative;
        margin: 0px 0px 10px calc((100% - 980px) * 0.5);
        left: -189px;
        grid-area: 5 / 1 / 6 / 2;
        justify-self: start;
        align-self: start;
      }
      .grid-5 {
        position: relative;
        margin: 5px 0px 10px calc((100% - 980px) * 0.5);
        left: 447px;
        grid-area: 2 / 1 / 7 / 2;
        justify-self: start;
        align-self: start;
        display: flex;
        flex-flow: column;
        img {
          margin: 10px 0;
        }
      }
      .grid-6 {
        position: relative;
        margin: 91px 0px 14px calc((100% - 980px) * 0.5);
        left: 698px;
        grid-area: 1 / 1 / 5 / 2;
        justify-self: start;
        align-self: start;
        display: flex;
        flex-flow: column;
        img {
          margin: 10px 0;
        }
      }
      .grid-7 {
        position: relative;
        margin: 5px 0px 10px calc((100% - 980px) * 0.5);
        left: 949px;
        grid-area: 2 / 1 / 8 / 2;
        justify-self: start;
        align-self: start;
        display: flex;
        flex-flow: column;
        img {
          margin: 10px 0;
        }
      }
      .grid-8 {
        position: relative;
        margin: 26px 0px 10px calc((100% - 980px) * 0.5);
        left: 698px;
        grid-area: 5 / 1 / 6 / 2;
        justify-self: start;
        align-self: start;
        font-family: wfont_531ace_58938f917a1b4e66a2181c66dc63faa1, wf_58938f917a1b4e66a2181c66d, orig_century_schoolbook_std;
        font-size: 30px;
        font-stretch: 100%;
        font-style: italic;
        font-variant-caps: normal;
        font-variant-east-asian: normal;
        font-variant-ligatures: normal;
        font-variant-numeric: normal;
        font-weight: 700;
        height: auto;
        letter-spacing: normal;
        line-height: 30px;
      }
    }

    .cont-layer4 {

    }
  }

  .footer {
    width: 100vw;
    height: 100px;
    display: flex;
    justify-content: center;
  }
}
</style>
<script>
export default {
  name: "Home",
};
</script>
