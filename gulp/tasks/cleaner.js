import del from "del";

import globs from "../config/globs.js";


const cleaner = () => {
    return del(globs.root);
};


export default cleaner;
