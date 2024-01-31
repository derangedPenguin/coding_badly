/*setInterval(() => {
    get_data()
}, 1000);*/

import data from './data.json' assert {type:'json'}

function update() {
    if (data.last_accessor == "server") {
        return
    }
    document.getElementById('counter').innerHTML = data.counter
    data.last_accessor = "server"
}

setInterval(() => {
    update()
}, 100)

