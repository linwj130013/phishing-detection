url = window.location.origin

const xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
        let res = JSON.parse(xhr.responseText).is_phishing_website
        console.log(res);
        if (res == 1) {
            alert("This might be a phishing website!");
        }
    }
}

xhr.open("POST", "http://127.0.0.1:5000/phishing_detector", true);
xhr.setRequestHeader('Content-Type', 'application/json');

xhr.send(JSON.stringify({
    "url": url
}));