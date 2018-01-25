const path = require('path');
const webpack = require("webpack")

module.exports = {
  entry: {
    'bundle:':'./src/app.js',
    'bundle.min':'./src/app.js',
  },
  module:{
      loaders: [
          {
            test: /\.js$/,
            loader: 'babel-loader',
            exclude: /node_modules/
          }
        ]
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, '../symptoms/static/gen')
  },
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      include: /\.min\.js$/,
      minimize: true
    })
  ]
};