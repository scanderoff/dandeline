import gulp from "gulp";
import plumber from "gulp-plumber";
import notify from "gulp-notify";
import gulpSass from "gulp-sass";
import dartSass from "sass";
import autoprefixer from "gulp-autoprefixer";
import cleanCss from "gulp-clean-css";
import rename from "gulp-rename";
import shorthand from "gulp-shorthand";
import groupCssMediaQueries from "gulp-group-css-media-queries";
import beautify from "gulp-beautify";

import app from "../config/app.js";
import globs from "../config/globs.js";
import {browserSync} from "./server.js";


const sass = gulpSass(dartSass);

const styles = () => {
    return gulp.src(globs.styles.src, {sourcemaps: app.isDev})
        .pipe(
            plumber(notify.onError({
                title: "SCSS",
                message: "<%= error.message %>",
            }))
        )
        .pipe(sass())
        .pipe(autoprefixer())
        .pipe(shorthand())
        .pipe(groupCssMediaQueries())
        .pipe(beautify.css())
        .pipe(gulp.dest(globs.styles.build, {sourcemaps: app.isDev}))
        .pipe(
            rename({
                suffix: ".min",
                extname: ".css",
            })
        )
        .pipe(cleanCss())
        .pipe(gulp.dest(globs.styles.build, {sourcemaps: app.isDev}))
        .pipe(browserSync.stream())
    ;
};


export default styles;
