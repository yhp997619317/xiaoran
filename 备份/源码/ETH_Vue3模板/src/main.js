import {createApp, readonly} from 'vue'
import App from './App.vue'
import router from './router'
import {createPinia} from 'pinia'; // 全局状态管理
import registerVant from './assets/registerUI/vant.js'; // vant 按需加载
import vanOverlay from './components/PackVant/Overlay/VanOverlay.js'; // 加载遮罩函数化调用
import {axiosList} from './assets/api/axios.js'; // api 封装
import './assets/css/public/index.scss'; //公共样式
import globalComponents from  './components/index'; // 全局组件
import './assets/img/icon/iconfont.js'
import './assets/img/icon/iconfont.css'

const app = createApp(App);
registerVant(app); // Vant3 按需注册
globalComponents(app); // 全局组件自动化注册
app.use(router).use(createPinia()).mount('#app');
app.provide('vanOverlay', readonly(vanOverlay));
app.provide('axios', readonly(axiosList));


