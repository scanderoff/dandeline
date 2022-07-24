const srcDir = "assets";
const buildDir = "backend/src/static";


export default {
    root: buildDir,

    styles: {
        src: `${srcDir}/styles/main.scss`,
        build: `${buildDir}/styles`,
        watch: `${srcDir}/styles/**/*.scss`,
    },

    scripts: {
        src: `${srcDir}/scripts/main.js`,
        build: `${buildDir}/scripts`,
        watch: `${srcDir}/scripts/**/*.js`,
    },

    images: {
        src: `${srcDir}/images/**/*.{jpg,jpeg,png,webp,svg,gif,ico}`,
        build: `${buildDir}/images`,
        watch: `${srcDir}/images/**/*.{jpg,jpeg,png,webp,svg,gif,ico}`,
    },

    fonts: {
        src: `${srcDir}/fonts/**/*.ttf`,
        build: `${buildDir}/fonts`,
        watch: `${srcDir}/fonts/**/*.ttf`,
    },
};
