module.exports = {
  presets: [
    '@vue/cli-plugin-babel/preset'
  ],
  plugins: [
    [
      "import",
      {
        "libraryName": "vant", // Vant UI 3.4.5 按需引入
        "libraryDirectory": "es",
        "style": true
      },
    ],
  ]
}
