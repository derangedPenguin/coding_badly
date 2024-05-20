precision highp float;

varying vec2 pos;

uniform float time;

uniform vec2 poi;

// #include "lygia/generative/voronoi.glsl"

// const int num_circles = 100;
// uniform vec3 circles[num_circles];

void main() {
    //set initial color
    vec4 color = vec4(0.0, 0.37, 0.09, 1.0);

    /*----------noise testing------------*/
    // float val = noise(pos);

    // color.r = rand(val);
    // color.g = rand(val);
    // color.b = rand(val);

    /*--------Signed distance for circles (stored as 2d array)---------*/
    // float dist;
    // float colour = 1.;
    // for (int i = 0; i < num_circles; i++) {
    //     float d = length(pos - circles[i].xy) - circles[i].z;
    //     d = smoothstep(0., (sin(time/1000.)+1.)/20., sin(d));
    //     colour *= d;
    // }
    // // float d = length(pos - poi) - 0.03;
    // // d = fract(smoothstep(0., (sin(time/1000.)+1.)/20., sin(d))*1.5);
    // color.r *= 0.;
    // color.gb *= colour;

    /*--------wave approach single circle---------*/
    // float center_dist = distance(poi, pos);
    // float circle_dist = center_dist - 0.05;

    // float val = (smoothstep(0.0, noise(pos), circle_dist + (sin(time/1000.)-2.)/10.));
    // val = fract(val);
    // val = smoothstep(0.0,0.05, val);

    // color.b = val;
    // color.g = val;
    // color.r = val;

    // color.g = 1. - val;

    /*--------trig func motion weirdness circle (kinda SDF)---------*/
    // float center_dist = distance(pos, poi);

    // float func_val = (tan(((center_dist*2.)-(time/4000.)))+1.)/2.;

    // // func_val = (func_val+1.)/2.;

    // float dist = ((1.-center_dist)-(time/1500.) - func_val)*3.;

    // // color.r = smoothstep(0., 0.2, fract(dist*1.5));
    // // color.r = fract(dist*3.);
    // color.g = fract(dist*1.5);
    // color.b = fract(dist*2.);

    /*--------trig func motion weirdness circle (kinda SDF)---------*/
    // float func_val = (tan(((pos.x*8.)+(time/1000.)))+1.)/2.;

    // // func_val = (func_val+1.)/2.;

    // float dist = ((pos.y)-(time/1500.) - func_val)*3.;

    // // color.r = smoothstep(0., 0.2, fract(dist*1.5));
    // // color.r = fract(dist*3.);
    // color.g = 1. - fract(dist*2.);
    // color.b = 1. - fract(dist*2.);

    /*--------gradients & Stuff---------*/
    // color.r = fract((sin(dist*10.+(time/1000.))+1.)/2. * 10.);
    // color.g = fract((tan(dist*13.+(time/100.))+1.)/2. * 10.);

    // color.r = (sin(-pos.y + (time/600.)*0.8)+1.)/2.;

    // color.g = (sin(-pos.x + (time/600.)*0.8)+1.)/2.;

    // color.b = (cos((pos.y+pos.x) + (time/800.)*0.8)+1.)/2.;

    gl_FragColor = color;
}