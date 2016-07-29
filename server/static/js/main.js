$(document).ready(function(){

// Uncomment to turn off all console messages
console.log = function() {}

// Websocket
var ws = new ReconnectingWebSocket("ws://127.0.0.1:9998");

ws.timeoutInterval = 2000;

ws.onopen = function(){
    console.log("connected");
};

ws.onclose = function(){
    console.log("disconnected");
};


ws.onmessage = function (message) {

    var incoming = JSON.parse(message.data);

    console.log(incoming);

    addr_to = incoming[0].to

    if (addr_to == "temp_humid") {
        $('#temp span').html(incoming[1]);
        $('#humid span').html(incoming[2]);
    }

    if (addr_to == "mister") {
        $('#mister span').html(incoming[1]);
    }

};


var sendMessage = function(message) {
    console.log("sending:" + message.data);
    ws.send(message.data);
};


});
