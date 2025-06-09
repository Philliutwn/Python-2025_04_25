// script.js 檔案內容
console.log("Hello from external JavaScript!");

const carouselTrack = document.querySelector('.homes-for-you-section__carousel-track');
const prevArrow = document.querySelector('.carousel-arrow--prev');
const nextArrow = document.querySelector('.carousel-arrow--next');
const dots = document.querySelectorAll('.carousel-pagination__dot');

let currentIndex = 0;
const cardWidth = 380; // 這裡需要根據您的實際卡片寬度和 gap 計算

if (nextArrow) {
    nextArrow.addEventListener('click', () => {
        // 這裡需要根據實際的輪播邏輯來移動 carouselTrack
        // 例如：
        // const totalCards = carouselTrack.children.length;
        // const visibleCards = 3; // 假設一次顯示3張
        // currentIndex = (currentIndex + 1) % (totalCards / visibleCards);
        // carouselTrack.style.transform = `translateX(-${currentIndex * cardWidth * visibleCards}px)`;
        console.log("Next button clicked from external JS!");
    });
}

if (prevArrow) {
    prevArrow.addEventListener('click', () => {
        console.log("Prev button clicked from external JS!");
    });
}

// 可以在這裡加入初始化的邏輯，例如設定第一個點為 active
if (dots.length > 0) {
    dots[0].classList.add('carousel-pagination__dot--active');
}