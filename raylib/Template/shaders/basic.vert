#version 410 core

uniform vec2 scale = (480.,320.);

layout (location = 0) in vec3 aPos;

void main()
{
    gl_Position = vec4(aPos.x / scale.x, aPos.y / scale.y, aPos.z, 1.0);
}