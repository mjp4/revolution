var S3Plugin = require('webpack-s3-plugin')
var config = {
}
module.exports = {
  entry: './index.js',

  output: {
    filename: 'bundle.js',
    publicPath: '',
      path: './'
  },

  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader?presets[]=es2015&presets[]=react' }
    ]
  }
}
