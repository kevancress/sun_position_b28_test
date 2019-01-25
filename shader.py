class Dashed_Shader_3D ():

    vertex_shader = '''
    uniform mat4 ModelViewProjectionMatrix;

    in vec3 pos;
    in float arcLength;    
    
    out float v_ArcLength;

    vec4 project = ModelViewProjectionMatrix * vec4(pos, 1.0f);
    vec4 offset = vec4(0,0,-0.001,0);

    void main()
    {
        v_ArcLength = arcLength;
        gl_Position = project + offset;
    }
    '''

    fragment_shader = '''
        uniform float u_Scale;
        uniform vec4 finalColor;
        
        in float v_ArcLength;
        
        void main()
        {
            if (step(sin(v_ArcLength * u_Scale), 0.5) == 1) discard;
            gl_FragColor = finalColor;
        }
    '''