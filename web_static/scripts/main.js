const myImage = document.querySelector("img");

myImage.onclick = () => {
    const mySrc = myImage.getAttribute("src");
    if (mySrc === "images/icon.png") {
        myImage.setAttribute("src", "images/logo.png");
    } else {
        myImage.setAttribute("src", "images/icon.png")
    }
};