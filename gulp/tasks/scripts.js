import webpack from "webpack-stream";

import gulp from "gulp";
import plumber from "gulp-plumber";
import notify from "gulp-notify";
// import rename from "gulp-rename";
import babel from "gulp-babel";

import app from "../config/app.js";
import globs from "../config/globs.js";
import {browserSync} from "./server.js";


const scripts = () => {
    return gulp.src(globs.scripts.src, {sourcemaps: app.isDev})
        .pipe(
            plumber(notify.onError({
                title: "JS",
                message: "<%= error.message %>",
            }))
        )
        .pipe(babel())
        .pipe(
            webpack({
                mode: app.isProd ? "production" : "development",
                output: {
                    filename: "main.min.js",
                },
            })
        )
        .pipe(gulp.dest(globs.scripts.build, {sourcemaps: app.isDev}))
        .pipe(browserSync.stream())
    ;
};


export default scripts;
