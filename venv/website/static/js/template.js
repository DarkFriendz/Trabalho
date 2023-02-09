/* Style */
const style = document.getElementById("styleTemplate")

if (window.innerWidth <= 800) {
    style.href = "static/css/mobile.css"
} else {
    style.href = "static/css/pc.css"
}

addEventListener("resize", function() {
    if (window.innerWidth <= 800) {
        style.href = "static/css/mobile.css"
    } else {
        style.href = "static/css/pc.css"
    }
});