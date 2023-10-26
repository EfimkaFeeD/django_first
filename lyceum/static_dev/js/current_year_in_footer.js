function get_correct_year() {
    const client_dt = Date.now()

    let element = document.getElementById("yearify")

    const xhr = new XMLHttpRequest();
    xhr.open("GET", "/date/" + client_dt.toString() + "/");
    xhr.onload = () => {
        element.innerHTML = element.innerHTML.slice(0, element.innerHTML.lastIndexOf(" "));
        element.innerHTML += " " + xhr.responseText;
        console.log(xhr.responseText);
    }
    console.log(client_dt.toString());
    xhr.send();

}
window.onload = get_correct_year;