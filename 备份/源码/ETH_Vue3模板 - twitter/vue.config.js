const path = require('path');
const AutoImport = require('unplugin-auto-import/webpack')
const Components = require('unplugin-vue-components/webpack')
const { ElementPlusResolver } = require('unplugin-vue-components/resolvers')
module.exports = {
	outputDir:`dist_${process.env.NODE_ENV}`, // 设置不同环境的打包输出地址
	publicPath: '/',
	pluginOptions: {
		/*  使用[data-xx]声明区分，将globalVar.scss样式文件复制到每个组件
		------------------------------------------------ */
		'style-resources-loader': {
			preProcessor: 'scss',
			patterns: [
				// 这个是绝对路径,不能使用别名路径，如@表示的src
				path.resolve(__dirname, './src/assets/css/global/index.scss')
			]
		}
	},
	chainWebpack: (config) => {
		/*  element plus CSS按需引入
		------------------------------------------------ */
		config
			.plugin('AutoImport')
			.use(AutoImport({ resolvers: [ElementPlusResolver()] }))
		config
			.plugin('Components')
			.use(Components({ resolvers: [ElementPlusResolver()] }))
		/*  标题
		------------------------------------------------ */
		config
			.plugin('html')
			.tap(args => {
				args[0].title= 'Ailoverse'
				return args
			})
	},
	devServer: {
		open: true, // 热编译完成自动打开浏览器
	},
	configureWebpack: {
		resolve: {
			/*  路径别名设置
			------------------------------------------------ */
			alias: {
				_components: "@/components",
				_assets: "@/assets",
				_views: "@/views",
				_store: "@/store"
			},
		},
	}
}