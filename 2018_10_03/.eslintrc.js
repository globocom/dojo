module.exports = {
  parser: "babel-eslint",
  env: {
    browser: true,
    commonjs: true,
    es6: true,
    jest: true,
  },
  extends: ["eslint:recommended", "plugin:jest/recommended", "prettier"],
  parserOptions: {
    ecmaVersion: 6,
    ecmaFeatures: {
      experimentalObjectRestSpread: true,
      jsx: true,
    },
    sourceType: "module",
    indentSwitchCase: true,
  },
  globals: {
    process: true,
  },
  plugins: ["jest", "prettier"],
  rules: {
    "linebreak-style": ["error", "unix"],
    "prettier/prettier": "error",
    "jest/valid-expect": "warn",
  },
  overrides: [
    {
      files: ["*.test.js"],
    },
  ],
}
