import gulp from "gulp";
import plumber from "gulp-plumber";
import notify from "gulp-notify";
import newer from "gulp-newer";
import ttf2woff2 from "gulp-ttf2woff2";

import globs from "../config/globs.js";
import {browserSync} from "./server.js";


const fonts = () => {
    return gulp.src(globs.fonts.src)
        // .pipe(
        //     plumber(notify.onError({
        //         title: "FONTS",
        //         message: "<%= error.message %>",
        //     }))
        // )
        .pipe(newer(globs.fonts.build))
        .pipe(ttf2woff2())
        .pipe(gulp.dest(globs.fonts.build))
        .pipe(browserSync.stream())
    ;
};


export default fonts;
