#version 410 core

uniform float time;

out vec4 FragColor;

in vec4 vertexColor; // the input variable from the vertex shader (same name and same type) 
// layout (origin_upper_left) in vec4 gl_FragCoord; 

void main()
{
    FragColor = vec4(1.,1.,1.,1.);
} 