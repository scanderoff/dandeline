function onIntersect(entries, observer) {
    for (const entry of entries) {
        if (!entry.isIntersecting) {
            continue;
        }

        const item = entry.target;
        const always = (item.dataset.scrollimAlways === "");

        if (always) {
            item.classList.remove("scrollim");
        }

        item.classList.add("scrollim");

        observer.unobserve(item);
    }
}


function init() {
    const observer = new IntersectionObserver(onIntersect, {
        root: null,
        rootMargin: "0px",
        threshold: 0.0,
    });


    const items = document.querySelectorAll("[data-scrollim]");

    for (const item of items) {
        observer.observe(item);
    }
}


export default {init};
