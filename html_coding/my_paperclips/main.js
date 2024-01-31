//----VARS----- 
const console_prefixes = ['- ', '- ', '- ', '- ', '> ']
var player_console = ['', '', '', '', 'Welcome to Planetary Paperclips!']

class auto_val {
    constructor(start_val, display_id, fix_to) {
        this.val = start_val
        this.display_id = display_id
        this.fix_to = fix_to
    }
    set(value) {
        this.val = value
        update_display_element(this.display_id, this.val.toFixed(this.fix_to))
    }
    add(value) {
        this.val += value
        update_display_element(this.display_id, this.val.toFixed(this.fix_to))
    }
}
var clips_count = new auto_val(0, 'clips_display', 0)
var available_funds = new auto_val(0, 'available_funds', 2)
var inventory = new auto_val(0, 'unsold_inventory', 0)

//public demand stored as 100x to avoid weird values
var public_demand = new auto_val(0, 'public_demand', 0)
var avg_clips_sold_sec = new auto_val(0, 'clips_sold_per_sec', 2)
//stored at 100x to avoid weird values
var price_per_clip = 25
var marketing_lvl = 1

var wire_remaining = 100

//--------MAINLOOP----------
setInterval(function() {
    if (Math.random() < public_demand.val/100) {
        sell_clips(Math.floor(.7 * public_demand.val**1.15))
    }
    avg_clips_sold_sec.set((inventory.val == 0) ? 0 : Math.min(1, public_demand.val/10000) * 7 * (public_demand.val/100)**1.15)
}, 100);

//-------GENERIC---------
function update_demand() {
    public_demand.set((1.1 ** (marketing_lvl-1)) * (0.8/(price_per_clip/1000)))
}

function sell_clips(clips_wanted) {
    //stop if nothing to buy
    if (inventory.val > 0) {
        //if there is enough clips
        if (inventory.val >= clips_wanted) {
            available_funds.add(clips_wanted * price_per_clip.val)
            inventory.add(-clips_wanted)
        } else {
            available_funds.add(inventory.val * price_per_clip.val)
            inventory.set(0)
        }
    }
    /*//calc based on average per second
    var clips_bought = Math.round(Math.min(1, public_demand.value/10000) * 7 * (public_demand.value/100)**1.15)
    //reduce clips bought to not go over available inventory
    if (inventory.value < clips_bought) {
        clips_bought = inventory.value
    }
    //apply
    inventory.add(0-clips_bought)
    available_funds.add(clips_bought * price_per_clip)*/
}

//------UTILS--------
function update_console() {
    var console_text = ''
    for (let i = 0; i < 5; i++) {
        console_text += console_prefixes[i] + player_console[i] + '<br>'
    }
    document.getElementById('player_console').innerHTML = console_text
}

function update_display_element(element_id, value) {
    document.getElementById(element_id).innerHTML = value
    return null
}

//---------BUTTONS--------------
function make_clip(amount) {
    if (wire_remaining >= amount) {
        clips_count.add(amount)
        inventory.add(amount)
        wire_remaining -= amount
        update_display_element('wire_display', wire_remaining)
    }
    return null
}

function raise_price() {
    price_per_clip += 1
    update_display_element('price_per_clip', (price_per_clip/100).toFixed(2))
    update_demand()
}
function lower_price() {
    if (price_per_clip > 1) {
        price_per_clip -= 1
        update_display_element('price_per_clip', (price_per_clip/100).toFixed(2))
        update_demand()
    }
}

