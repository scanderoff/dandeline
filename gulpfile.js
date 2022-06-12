import gulp from "gulp";

import app from "./gulp/config/app.js";
import globs from "./gulp/config/globs.js";

import cleaner from "./gulp/tasks/cleaner.js";
import styles from "./gulp/tasks/styles.js";
import scripts from "./gulp/tasks/scripts.js";
import images from "./gulp/tasks/images.js";
import fonts from "./gulp/tasks/fonts.js";


const watch = () => {
    gulp.watch(globs.styles.watch, styles);
    gulp.watch(globs.scripts.watch, scripts);
    gulp.watch(globs.images.watch, images);
    gulp.watch(globs.fonts.watch, fonts);
};


const build = gulp.series(
    cleaner,
    gulp.parallel(styles, scripts, images, fonts),
);

const dev = gulp.series(
    build,
    watch,
);


export {
    styles,
    scripts,
    images,
    fonts,
};

export default app.isProd ? build : dev;
