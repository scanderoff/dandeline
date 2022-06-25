function preloadLazyItem(lazyItem) {
    const src = lazyItem.dataset.src;
    const srcset = lazyItem.dataset.srcset;
    const href = lazyItem.dataset.href;
    const bg = lazyItem.dataset.bg;

    if (src) {
        lazyItem.src = src;
        delete lazyItem.dataset.src;
    } else if (srcset) {
        lazyItem.srcset = srcset;
        delete lazyItem.dataset.srcset;
    } else if (href) {
        // lazyItem.href.baseVal = href;
        // delete lazyItem.dataset.href;
    } else if (bg) {
        lazyItem.style.backgroundImage = `url(${bg})`;
        delete lazyItem.dataset.bg;
    }
}


function onIntersect(entries, observer) {
    for (const entry of entries) {
        if (!entry.isIntersecting) {
            continue;
        }

        const lazyItem = entry.target;

        if (lazyItem.dataset.hidden === "") {
            continue;
        }

        preloadLazyItem(lazyItem);

        observer.unobserve(lazyItem);
    }
}




function init() {
    const observer = new IntersectionObserver(onIntersect, {
        root: null,
        rootMargin: "0px 0px 300px",
        threshold: 0,
    });


    const lazyItems = document.querySelectorAll("[data-src], [data-srcset], [data-href], [data-bg]");

    for (const lazyItem of lazyItems) {
        if (lazyItem.matches(".swiper-lazy")) {
            continue;
        }

        observer.observe(lazyItem);
    }
}


export default {init};
