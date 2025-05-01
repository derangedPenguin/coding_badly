class SpanValue {
    constructor(starting_val, span_key, transform = ((a)=>a), bounds=null ) {
        this.val = starting_val;
        this.transform = transform;
        this.span_key = span_key; // stored for identification/saving
        this.span_elem = document.getElementById(span_key);
        this.bounds = bounds;

        this.set(starting_val);  // force visual update
        saved_vals.push(this);   // so this val will be saved when save() is called
    };
    get() { // would likely be better by using real get/sets, but i dumb & have recursion issue
        return this.transform(+this.val.toFixed(2));
    };
    set(new_val) {
        if (this.bounds !== null) {
            this.val = Math.max(Math.min(Number(new_val), this.bounds[1]), this.bounds[0]);
        } else {
            this.val = Number(new_val);
        }
        this.span_elem.innerText = this.get();
    };
    add(new_val) {
        this.set(this.val + Number(new_val));
    };
};
class AveragedValue extends SpanValue {
    constructor(span_key, transform = ((a)=>a), bounds=null, max_measures, measure_period) {
        super(0, span_key, transform, bounds);
        this.measures = [0, ]
        this.max_measures = max_measures
        this.measure_period = measure_period
    }
    get() {
        var sum = 0
        for (var i in this.measures) {
            sum += this.measures[i]
        }
        return sum / this.measure_period
    }
    add(val) {
        this.measures.push(val)
        if (this.measures.length > this.max_measures) {
            this.measures.splice(0, 1)
        }
        this.span_elem.innerText = +this.get().toFixed(5);
    }
}

//full scope inits
let saved_vals = []

let total_things = undefined

let posessed_money = undefined
let posessed_things = undefined
let thing_market_value = undefined
let thing_sale_price = undefined

let material_cost_per_thing = undefined
let posessed_materials = undefined
let material_purchase_amount = undefined
let material_cost = undefined

let thing_producers = undefined
let thing_producer_cost = undefined
let thing_producer_speed = undefined

let thing_production = undefined

let marketing_budget = undefined

let societal_dependance;

function base_initialize() {
    // SpanValues
    total_things = new SpanValue(0, "total-things", (a)=>Math.floor(a))
    
    posessed_money = new SpanValue(10, "posessed-money");
    
    posessed_things = new SpanValue(0, "posessed-things", (a)=>Math.floor(a));
    thing_market_value = new SpanValue(0.5, "thing-market-value");
    thing_sale_price = new SpanValue(0.5, "thing-sale-price", undefined, [0.1,Infinity]);
    
    material_cost_per_thing = new SpanValue(10, "material-cost-per-thing");
    posessed_materials = new SpanValue(1500, "posessed-materials", (a)=>Math.floor(a));
    material_purchase_amount = new SpanValue(1500, "material-purchase-amount");
    material_cost = new SpanValue(20, "material-cost");

    thing_producers = new SpanValue(0, "thing-producers");
    thing_producer_cost = new SpanValue(10, "thing-producer-cost");
    
    marketing_budget = new SpanValue(0, "marketing-budget", undefined, [0,100]);

    research_budget = new SpanValue(0, "research-budget", undefined, [0,100]);
    
    societal_dependance = new SpanValue(0.01, "societal-dependence", undefined);

    //Calced Values
    thing_producer_speed = 0.25;
    thing_production = new AveragedValue("thing-production", undefined, undefined, 15, 15)
}

const calced_spans = {
    "expected-thing-production": ()=>{return thing_producers.get() * thing_producer_speed / 10}
}

// HTML Element Inits
window.addEventListener("DOMContentLoaded", () => {
    base_initialize();
})

// fast loop, 0.1sec
setInterval(() => {
    //Functions
    //Auto Producers
    var amount_produced = produce_things(thing_producers.get() * thing_producer_speed / 10);

    //Update Averaged Values
    thing_production.add(amount_produced)

    //Sale of Things


    //Factors: Price/Market Val, Societal Dependance <- Total Marketing, Active Marketing
    var purchase_likelyhood = Math.max((-0.2 + thing_market_value.get()/thing_sale_price.get()) / 10 * societal_dependance.get() / 0.01, 0)
    add_terminal_entry(purchase_likelyhood)
    if (Math.random() < purchase_likelyhood) {
        var x = Math.floor((purchase_likelyhood + Math.random() * 0.5) * posessed_things.get())
        sell_things(x)
        add_terminal_entry(`Sale: ${x}`)
    }

    // Display
    for (key in calced_spans) {
        document.getElementById(key).innerText = calced_spans[key]()
    }
}, 100);//milliseconds

function add_terminal_entry(text) {
    var term_entries = document.getElementById("header-terminal") 
    
    var prev_entry = term_entries.children[Math.max(term_entries.childElementCount - 4, 0)]
    
    
    var prev_text = prev_entry.innerText.slice(2)
    
    var prev_mult = 0
    var mult_term_start = 0
    if (prev_text[prev_text.length-1] == ']') {
        
        mult_term_start = prev_text.indexOf('[')
        
        // console.log(prev_text.slice(mult_term_start+2, prev_text.length-1))
        prev_mult = Number(prev_text.slice(mult_term_start+2, prev_text.length-1))
        prev_text = prev_text.slice(0,mult_term_start)
        
    }  
    if (prev_text==text) {
        console.log(prev_mult)
        prev_entry.innerText = `${prev_entry.innerText.slice(0,mult_term_start+4)} [x${toString(prev_mult+1)}]`
        term_entries.lastChild.scrollIntoView({"behavior":"smooth"})
        return
    }
    
    term_entries.innerHTML += `<span class="terminal-entry typed" style="--n:${2+text.length}">> ${text}</span><br>` //•
    
    var prev_entry = term_entries.children[term_entries.childElementCount - 4]
    prev_entry.classList.remove("typed")
    prev_entry.innerText = '•' +  prev_entry.innerText.substring(1, prev_entry.innerText.length)

    term_entries.lastChild.scrollIntoView({"behavior":"smooth"})
}

function sell_things(amount) {
    if (amount > posessed_things.get()) {
        var things_sold = posessed_things.get()
    } else {
        var things_sold = amount
    }

    posessed_things.add(-things_sold)
    posessed_money.add(things_sold*thing_sale_price.get())
}

function produce_things(amount) {
    // produces as much of :param amount: as possible, up to maximum based on posessed materials
    // returns actual amount produced
    var materials_used = amount*material_cost_per_thing.get()

    if (materials_used <= posessed_materials.get()) {

        posessed_things.add(amount)
        total_things.add(amount)

    } else if (materials_used > posessed_materials.get()) {
        amount = (posessed_materials.val / material_cost_per_thing.get())
        materials_used = amount * material_cost_per_thing.get()

        posessed_things.add(amount)
        total_things.add(amount)

    }
    posessed_materials.add(-materials_used)

    return amount
}
//Buttons
function buy_thing_producer() {
    if (posessed_money.get() >= thing_producer_cost.get()) {
        posessed_money.add(-thing_producer_cost.get())
        thing_producers.add(1)
    }
}
function buy_materials() {
    if (posessed_money.get() >= material_cost.get()) {
        posessed_money.add(-material_cost.get())
        posessed_materials.add(material_purchase_amount.get())
    }
}

// Debug Buttons
function reset_save() {
    base_initialize()
    save()
    location.reload()
}

// Handle Saving Data
function save() {
    for (spanVal of saved_vals) {
        localStorage.setItem(spanVal.span_key, spanVal.val)
    }
}
function load() {
    for (spanVal of saved_vals) {
        spanVal.set(localStorage.getItem(spanVal.span_key))
    }
}
window.addEventListener("visibilitychange", ()=>{
    if (document.visibilityState == "hidden") {save()} //runs when page may close, weird for handling mobile
})
window.addEventListener("DOMContentLoaded", load)

