
const $productList = document.querySelector(".product-sorter + .products__list");
const $footer = document.querySelector(".footer");
let page = 1;
let block_request = false;

if ($productList) {
    const observer = new IntersectionObserver(onIntersect, {
        root: null,
        rootMargin: "0px",
        threshold: 0,
    });

    observer.observe($footer)

    function onIntersect(entries, observer) {
        const entry = entries[0];

        if (!entry.isIntersecting) {
            block_request = false;
            return;
        }

        const $target = entry.target;

        page += 1;
        block_request = true;

        const url = new URL(location);
        url.searchParams.append("page", page);

        fetch(url, {
            method: "GET",

            headers: {
                "X-Requested-With": "XMLHttpRequest"
            },
        })
            .then(response => response.text())
            .then(html => {
                if (!html) {
                    observer.unobserve($target);

                    return;
                }

                $productList.insertAdjacentHTML("beforeend", html);
                block_request = false;
            })
        ;
    }
}
