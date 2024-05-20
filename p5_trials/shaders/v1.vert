precision mediump float;

attribute vec3 aPosition;
attribute vec2 aTexCoord;

varying vec2 pos;

uniform float time;

void main() {
    pos = aTexCoord;

    vec4 position = vec4(aPosition, 1.);
    
    position.xy = position.xy * 2. - 1.;

    // position.y += (sin(pos.x*10. * (time/1000.))+1.)/2.;


    // position.y += sin(position.x*18. + (time/1000.))/8.;// + (time/10000.));

    gl_Position = position;
}