url = window.location.origin

var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE) {
        let res = JSON.parse(xhr.responseText).url_returned
        
        alert(res);
    }
}
xhr.open("POST", "http://127.0.0.1:5000/test", true);
xhr.setRequestHeader('Content-Type', 'application/json');

xhr.send(JSON.stringify({
    "url": url
}));
