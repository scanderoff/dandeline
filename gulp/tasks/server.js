import browserSync from "browser-sync";
import globs from "../config/globs.js";


const server = () => {
    browserSync.init({
        notify: false,
        port: 8080,
        server: {
            baseDir: globs.root,
        },
    });
};


export {server, browserSync};
