//--------------VARS---------------
var player_console = {
    prefixes: "----->",
    messages: ['','','','','Welcome to Planetary Paperclips!'],
    get_string: function() {
        var full_string = ''
        for (var i=0; i<5;i++) {
            full_string += ' ' + this.prefixes[i] + this.messages[this.messages.length-i] + '<br>'
        }
    }
}

var clips = 0
var funds = 0
var available_clips = 0
var wire_remaining = 1000

var demand = 0
var price_per_clip = 25 //stored at 100x actual
var marketing_lvl = 1

//-----------------MAINLOOP------------------
setInterval(function() {
    
}, 100);

//--------------BUTTONS----------------
function make_clip(amount) {
    if (wire_remaining >= amount) {
        clips += amount
        available_clips += amount
        wire_remaining -= amount
    }
}

function change_price(amount) {
    if (price_per_clip + amount > 1) {
        price_per_clip += amount
    }
}