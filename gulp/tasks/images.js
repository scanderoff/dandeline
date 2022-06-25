import gulp from "gulp";
import plumber from "gulp-plumber";
import notify from "gulp-notify";
import imagemin from "gulp-imagemin";
import newer from "gulp-newer";
import if_ from "gulp-if";

import app from "../config/app.js";
import globs from "../config/globs.js";
import {browserSync} from "./server.js";


const images = () => {
    return gulp.src(globs.images.src)
        .pipe(
            plumber(notify.onError({
                title: "IMAGES",
                message: "<%= error.message %>",
            }))
        )
        .pipe(newer(globs.images.build))
        .pipe(if_(app.isProd,
            imagemin({
                // verbose: true,
            })
        ))
        .pipe(gulp.dest(globs.images.build))
        .pipe(browserSync.stream())
    ;
};


export default images;
