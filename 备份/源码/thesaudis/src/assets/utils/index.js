// rem 适配，根字体计算
function rem() {
  // 理想视口下，dip与布局视口相等，因此获取布局视口就可以拿到dip
  const dip = document.documentElement.clientWidth
  // 计算根字体大小
  const rootFontSize = dip / 10
  // 设置根字体
  document.documentElement.setAttribute('style', 'font-size: ' + rootFontSize + 'px !important');
};

// sessionStorage 加密解密
function sessionStorageMD5() {

}

export default {
  rem
}