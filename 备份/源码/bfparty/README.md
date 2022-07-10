# project

## 简介

基于 Vue 3.2 重构门店生命周期系统手机端项目。

#### 项目采用技术:

- [vue3 + composition api](https://staging-cn.vuejs.org/guide/introduction.html)
- [sass (dart sass)](https://www.sass.hk/docs/)

- [element-plus](https://element-plus.gitee.io/zh-CN/component/button.html)
- [vant3](https://vant-contrib.gitee.io/vant/#/zh-CN)
- [vue-router-next](https://router.vuejs.org/installation.html)
- [pinia](https://pinia.vuejs.org/introduction.html)
- [axios](https://www.axios-http.cn/docs/intro)
- [echarts](https://echarts.apache.org/zh/index.html)

## 安装使用

### 环境配置

```powershell
node: 14.18.2
yarn: 1.22.17
vue cli: @vue/cli 4.5.15
```

### 安装依赖

```powershell
yarn install
```

### 运行

```powershell
yarn run serve:dev # 测试
yarn run serve:uat # uat 测试
yarn run serve:prod # 生产
```

### 打包

```powershell
yarn run build:dev # 测试
yarn run build:uat # uat 测试
yarn run build:prod # 生产
```

## 目录结构

```
app
├─ .env.dev           # 开发环境
├─ .env.uat           # 测试环境
├─ .env.prod          # 生产环境
├─ README.md          
├─ dist_dev           # dev打包
├─ dist_uat           # uat打包
├─ dist_prod          # prod打包
├─ public             # 静态资源
├─ src                # 源码
│  ├─ assets          # webpack打包的资源
│  │  ├─ api          # 接口请求
│  │  ├─ css          # 样式
│  │  ├─ data         # 定义变量、数据
│  │  ├─ img          # 图片资源
│  │  ├─ registerUI   # UI按需引入
│  │  ├─ utils        # 公共方法
│  ├─ components      # 公共组件
│  ├─ router          # 路由
│  ├─ store           # 全局store管理
│  └─ views           # 所有业务页面
└─ vue.config.js      # vue-cli 配置
```

