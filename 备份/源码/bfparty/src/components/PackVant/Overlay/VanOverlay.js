import {createApp} from 'vue'
import Overlay from './Overlay.vue'

/**
 * 1) 创建 Overlay 组件的构造函数
 * 2) 生成 Overlay 组件实例
 * 3) 实例 DOM 插入页面
 */
let construct = null;
let el = document.createElement('div');
let selfOverlay = null;
document.body.appendChild(el);
/**
 * 展示遮罩
 */
function show(title = "") {
  if (!selfOverlay) {
    construct = createApp(Overlay, {
      title,
      show:true
    });
    selfOverlay = construct.mount(el);
  } else {
    selfOverlay = construct.mount(el);
  }
};

/**
 * 关闭遮罩
 */
function close() {
  if (selfOverlay) {
    selfOverlay = construct.unmount(el);
  }
};

export default {
  show,
  close,
}