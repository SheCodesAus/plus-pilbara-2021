window.onload = function () {
    // create new elements
    let speechBubbleElement = document.createElement("div");
    speechBubbleElement.classList.add("speech-bubble");
    let messageBox = document.createElement("p");
    messageBox.innerText = "...";
    messageBox.id = "message-box";
    speechBubbleElement.appendChild(messageBox);

    // add new element to page
    let outputElement = document.getElementById("output");
    outputElement.appendChild(speechBubbleElement);
};

function showMessage() {
    let message = document.getElementById("message-text").value;
    let name = document.getElementById("name").value;
    let messageBox = document.getElementById("message-box");
    messageBox.innerText = message + " - " + name;
};



