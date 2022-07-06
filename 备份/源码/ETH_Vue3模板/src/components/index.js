/*  组件自动化全局注册
------------------------------------------------ */
const components = require.context('./', true, /\.vue$/);
export default (app) => {
  components.keys().forEach(fileName => {
    let config = components(fileName);
    // console.log(config);
    if(!!config.default.name) {
      app.component(config.default.name, config.default);
    }
  });
}