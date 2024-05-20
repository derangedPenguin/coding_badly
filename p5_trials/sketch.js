let my_shader

let vertSource, fragSource

let poi

const num_circles = 100
let circles = []
let c_vs = []

function preload() {
  vertSource = loadStrings('shader.vert');
  fragSource = loadStrings('shader.frag');
}

function setup() {
  createCanvas(windowHeight, windowHeight, WEBGL)

  vertSource = resolveLygia(vertSource);
  fragSource = resolveLygia(fragSource);

  my_shader = loadShader(vertSource, fragSource)
  shader(my_shader)

  noStroke()

  // poi = [0.5,0.5]//[random(), random()]
  // my_shader.setUniform('poi', poi)


  // for (let i = 0; i < num_circles; i++) {
  //   circles.push(random(), random(), random()/20)
  // }
  // for (let i = 0; i < num_circles; i++) {
  //   c_vs.push([(random()-0.5)/100, (random()-0.5)/100])
  // }

}

function draw() {
  clear()
  my_shader.setUniform('time', millis())
  my_shader.setUniform('poi', [0.5,0.5])//[winMouseX/width, 1- winMouseY/height])
  // my_shader.setUniform('circles', circles)
  
  // for (let i = 0; i < num_circles; i+=3) {
  //   v = c_vs[Math.floor(i/3)]
  //   p = circles[i]
  //   circles[i] = max(min(v[0] + p[0], width), 0)
  //   circles[i+1] = max(min(v[1] + p[1], height), 0)
  // }


  //run shader
  rect(0, 0, 200, height)
  // ellipse(0, 0, width, height, 150);
  // rect(40, 0, width, height);
  // cylinder(10,10,150)
}
