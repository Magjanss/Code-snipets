
function readIt(id) {
    
    var searchTerm = id 
   
    var j = messages.indexOf(searchTerm)
    var temp = messages.slice(0,j)
   
    var i = temp.lastIndexOf("urtext") //not good if message contains urtext
    
    j = temp.indexOf("retext", i)
    if (j == -1) {	
	messages = messages.substr(0, i) + "re" + messages.substr(i+2)
    }
    
    document.getElementById("message").innerHTML =  messages
}

function sendMessage() {
 
    var msg = document.getElementById("inputText").value
    
    if (typeof messages === 'undefined') {
	messages = ""    // Note to self DO NOT PUT var HERE AGAIN
	messageIndex = 0
    }
    if ((msg.length == 0) || (msg.length > 140) ) {
	pre =  "<p id=\x27alert\x27>"
	pst =  "</p>"
	msg =  " Felmeddelande: Meddelanden måste vara mellan 1 - 140 tecken."
	
	temp = pre  + msg + pst + messages
	document.getElementById("message").innerHTML =  temp
    }
    else {
	messageIndex++
	pre =  "<p id=\x27urtext\x27>"
	pst =  "<input id=\x27mess" + messageIndex  + "\x27 onclick="
	pst = pst + "\x27readIt(this.id)\x27 type=\x27checkbox\x27></p>"
	messages = pre  + msg + pst + messages
	//alert(messages)
	document.getElementById("message").innerHTML =  messages
    }
}
var messages
var messageIndex
    
