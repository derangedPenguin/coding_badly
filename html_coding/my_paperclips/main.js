//----VARS-----  weird values for simpler init
const console_prefixes = ['- ', '- ', '- ', '- ', '> ']
var player_console = ['', '', '', '', 'Welcome to Planetary Paperclips!']

var clips_count = -1
var wire_remaining = 1001


function update_console() {
    var console_text = ''
    for (let i = 0; i < 5; i++) {
        console_text += console_prefixes[i] + player_console[i] + '<br>'
    }
    document.getElementById('player_console').innerHTML = console_text
}

function update_display_element(element_id, prefix, value) {
    document.getElementById(element_id).innerHTML = prefix + value
    return null
}

function make_clip() {
    if (wire_remaining >= 1) {
        clips_count += 1
        wire_remaining -= 1
        update_display_element('clips_display', 'Clips: ', clips_count)
        update_display_element('wire_display', 'Wire Remaining: ', wire_remaining)
    }
    return null
}