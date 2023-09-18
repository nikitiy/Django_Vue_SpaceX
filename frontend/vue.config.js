const { defineConfig } = require('@vue/cli-service')
const static_dir = '../backend/static'
const template_path = '../apps/home_page/templates/home_page/home_page.html'

module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: process.env.NODE_ENV === 'production' ? static_dir : 'dist/',
  indexPath: process.env.NODE_ENV === 'production' ? template_path : 'index.html',
  publicPath: process.env.NODE_ENV === 'production' ? '/static' : '/',
  assetsDir: '',
  css: {
    loaderOptions: {
      scss: {
        additionalData: `@import "@/assets/styles/variables.scss";`
      }
    }
  },
  devServer: {
    proxy: {
      'api/': {
        'target': 'http://localhost:8000/',
      },
    }
  }
})
