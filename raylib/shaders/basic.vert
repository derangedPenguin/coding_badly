#version 410 core

uniform float time;

layout (location = 0) in vec3 aPos;

void main()
{
    // gl_Position = vec4((aPos.x - 0)/960, (aPos.y - 0)/640, aPos.z, 1.0);
    gl_Position = vec4((aPos-320)/640, 1.0);
}