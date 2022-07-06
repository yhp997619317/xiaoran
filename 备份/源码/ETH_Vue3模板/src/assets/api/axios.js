import Axios from 'axios'
import Qs from 'qs'
import overLay from '_components/PackVant/Overlay/VanOverlay.js'

// Axios 配置
Axios.defaults.timeout = 300000
Axios.defaults.withCredentials = false

let API, MOCK
switch (process.env.NODE_ENV) {
	case 'dev':
		/*  开发环境
    ------------------------------------------------ */
		API = {
			baseUrl: 'http://slmtest.joeone.net:8080/Pmt/Api/',
			fileUrl: 'http://slmtest.joeone.net:8080/TempFiles/',
		}
		MOCK = { mockUrl: 'http://127.0.0.1:4523/mock/627299' }
		break
	case 'uat':
		/*  UAT 测试环境
    ------------------------------------------------ */
		API = {
			baseUrl: 'http://120.25.127.15:9991/Pmt/Api/',
			fileUrl: 'http://120.25.127.15:9991/TempFiles/',
		}
		MOCK = { mockUrl: 'http://127.0.0.1:4523/mock/627299' }
		break
	case 'prod':
		/*  生产环境(139.224.119.110:32010)
    ------------------------------------------------ */
		API = {
			baseUrl: 'http://pt.rls.com.cn:58080/Pmt/Api/',
			fileUrl: 'http://pt.rls.com.cn:8988/TempFiles/',
		}
		MOCK = { mockUrl: 'http://127.0.0.1:4523/mock/627299' }
		break
}
const { baseUrl } = API
const { mockUrl } = MOCK

/**
 * axios 请求封装
 * @param {String} url 请求地址
 * @param {String} method 请求方法
 * @param {Object} data 数据
 * @param {Boolean} isOverLay 是否开启遮罩
 * @returns {Promise<unknown>}
 */
export function axiosData(url, method, data, isOverLay = true) {
	let restful = method.toLowerCase()
	return new Promise((resolve, reject) => {
		let json
		if (restful === 'get') {
			json = {
				params: data,
			}
		} else if (restful === 'post') {
			json = Qs.stringify(data)
		}
		if (isOverLay) overLay.show('加载中')
		Axios[restful](baseUrl + url, json)
			.then((res) => {
				if (res.data.Status == 1) {
					resolve(res.data)
				} else {
					throw error(res.data)
				}
				if (isOverLay) overLay.close()
			})
			.catch((res) => {
				reject(res)
				overLay.close()
			})
	})
}

// 模拟接口请求封装
export function axiosData2(url, method, data, config) {
	let restful = method.toLowerCase()
	return new Promise((resolve, reject) => {
		let json
		if (restful === 'get') {
			json = {
				params: data,
			}
		} else if (restful === 'post') {
			json = Qs.stringify(data)
		}
		overLay.open('加载中...')
		Axios[restful](mockUrl + url, json, config)
			.then((res) => {
				resolve(res.data)
				overLay.close()
			})
			.catch((res) => {
				reject(res)
				overLay.close()
			})
	})
}

export let axiosList = {
	
}
