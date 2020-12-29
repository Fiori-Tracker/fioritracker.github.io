"use strict";

module.exports = {
    open: false,
    browser: ["chrome", "iexplore"],
    watchTask: false,
    reloadOnRestart: false,
    files: ['.html'],
    watch: false,
    injectChanges: false,
    reloadDelay: 1000,
    reloadDebounce: 3000,
    reloadThrottle: 3000,
    plugins: [],
    notify: false,
    cors: false,
    online: false,
    port: 8012,
    server: {
        baseDir: ".",
    }
};