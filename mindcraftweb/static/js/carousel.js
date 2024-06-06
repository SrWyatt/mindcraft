function showSlide(carouselId, index) {
    const carousel = document.getElementById(carouselId);
    const slides = carousel.querySelectorAll('.carousel-item');
    let currentIndex = carousel.dataset.currentIndex ? parseInt(carousel.dataset.currentIndex) : 0;

    if (index >= slides.length) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = slides.length - 1;
    } else {
        currentIndex = index;
    }
    
    const offset = -currentIndex * 100;
    carousel.querySelector('.carousel-inner').style.transform = `translateX(${offset}%)`;
    carousel.dataset.currentIndex = currentIndex;
}

function nextSlide(carouselId) {
    const carousel = document.getElementById(carouselId);
    let currentIndex = carousel.dataset.currentIndex ? parseInt(carousel.dataset.currentIndex) : 0;
    showSlide(carouselId, currentIndex + 1);
}

function prevSlide(carouselId) {
    const carousel = document.getElementById(carouselId);
    let currentIndex = carousel.dataset.currentIndex ? parseInt(carousel.dataset.currentIndex) : 0;
    showSlide(carouselId, currentIndex - 1);
}

document.addEventListener('DOMContentLoaded', () => {
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(carousel => {
        carousel.dataset.currentIndex = 0;
        showSlide(carousel.id, 0);
    });
});
