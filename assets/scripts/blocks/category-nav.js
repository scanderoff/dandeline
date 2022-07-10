const $catNavBtns = document.querySelectorAll(".category-nav__btn");
$catNavBtns.forEach($catNavBtn => $catNavBtn.addEventListener("click", toggleNav));

function toggleNav(event) {
    const $btn = event.currentTarget;
    const $item = $btn.closest(".category-nav__item");

    $item.classList.toggle("active");
}




const $items = document.querySelectorAll(".category-nav__item");

for (const $item of $items) {
    const $subs = $item.querySelectorAll(".category-nav--sub");

    if ($subs.length == 0) {
        continue;
    }

    let maxHeight = 0;

    for (const $sub of $subs) {
        maxHeight += $sub.scrollHeight;
    }

    $item.style.setProperty("--max-height", `${maxHeight}px`);
}









const $active = document.querySelector(".category-nav__item.active");

let $sup = $active?.parentElement.closest(".category-nav__item");

while ($sup) {
    $sup.classList.add("active");
    $sup = $sup.parentElement.closest(".category-nav__item");
}
