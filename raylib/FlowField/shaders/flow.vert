#version 410 core

uniform float time;
uniform float costime;
uniform float sintime;

uniform vec2 mouse_pos;

uniform vec2 scale = vec2(480., 320.); //idk y but I cant manage to set this properly externally

layout (location = 0) in vec3 aPos;

out vec4 vertexColor;

void main()
{
    //have right coords
    vec4 scaledPos = vec4(aPos.x / scale.x, aPos.y / scale.y, aPos.z, 1.0);

    //calc fancy angle
    float angle = distance(aPos.xy, mouse_pos) / 300 * scaledPos.x * 10 - scaledPos.y;

    //apply angle & magnitude
    float xmod = 0.2 * cos(angle);
    float ymod = 0.2 * sin(angle);

    vec3 fancyColor = vec3(costime * scaledPos.x, sintime*sin(scaledPos.y+time), tanh(time));
    
    //apply fancy
    scaledPos.x += xmod * mod(gl_VertexID, 2); // only apply to every other point
    scaledPos.y += (ymod * scale.x/scale.y - 20./320.) * mod(gl_VertexID, 2); // only apply to every other point, proportion properly to window

    //basic outs
    gl_Position = scaledPos;
    vertexColor = vec4(fancyColor,1.);
}