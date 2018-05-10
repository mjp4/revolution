var S3Plugin = require('webpack-s3-plugin')
var config = {
    plugins: [
      new S3Plugin({
          // Exclude uploading of html
          exclude: /.*\.html$/,
          // s3Options are required
          s3Options: {
              accessKeyId: 'AKIAJHAQQJCJFN423PDQ',
              secretAccessKey: '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',
              region: 'eu-west-2'
          },
          s3UploadOptions: {
              Bucket: 'revolution-wa'
          },
          cdnizerOptions: {
              defaultCDNBase: 'http://asdf.ca'
          }
      })
    ]
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
