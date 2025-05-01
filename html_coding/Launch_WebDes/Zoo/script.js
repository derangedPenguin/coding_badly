let slideIndex = 0;

// update on init and every 5 seconds, bad performance-wise, but idc
setInterval(() => {
    showSlides(slideIndex);
    // setMargins();
}, 5);


// cant get this to work properly
function setMargins() {
    let slides = document.getElementsByClassName("slide_img");
    let images = []

    let max_height = 0;

    for (i = 0; i < slides.length; i++) {
        images[i] = new Image()
        images[i].src = slides[i].src

        if (images[i].naturalHeight > max_height) {
            max_height = images[i].naturalHeight
        }
    }

    for (i = 0; i < images.length; i++) {
        images[i].style.marginTop = toString((max_height - images[i].naturalHeight) / 2) + "px"
    }
    // handle non-uniform img heights
    // let max_height = slides[0].naturalHeight;
    // for (i = 0; i < slides.length; i++) {
    //     if (slides[i].naturalHeight > max_height) {
    //         max_height = slides[i].hei
    //     }
    //     console.log(slides[i].naturalHeight)
    // }
    // for (i = 0; i < slides.length; i++) {
    //     slides[i].style.marginTop = String((max_height-slides[i].naturalHeight) / 2) + "px";
    //     // console.log(String((max_height-slides[i].naturalHeight) / 2) + "px")
    // }
    // console.log("once")
}

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("slide_img");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex-1].style.display = "block";
}