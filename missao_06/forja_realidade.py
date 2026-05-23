from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

sh = 0.0

vertices = [
    [-0.5, -0.5,  0.5],
    [ 0.5, -0.5,  0.5],
    [ 0.5,  0.5,  0.5],
    [-0.5,  0.5,  0.5],
    [-0.5, -0.5, -0.5],
    [ 0.5, -0.5, -0.5],
    [ 0.5,  0.5, -0.5],
    [-0.5,  0.5, -0.5]
]

faces = [
    [0, 1, 2, 3],
    [1, 5, 6, 2],
    [5, 4, 7, 6],
    [4, 0, 3, 7],
    [3, 2, 6, 7],
    [4, 5, 1, 0]
]

cores = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [1.0, 1.0, 0.0],
    [1.0, 0.0, 1.0],
    [0.0, 1.0, 1.0]
]

def desenhar_cubo():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(cores[i])
        for vertice_idx in face:
            glVertex3fv(vertices[vertice_idx])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    gluLookAt(1.5, 1.5, 2.0,  0.0, 0.0, 0.0,  0.0, 1.0, 0.0)
    
    matriz_cisalhamento = [
        1.0,  sh,   0.0,  0.0,
        0.0,  1.0,  0.0,  0.0,
        0.0,  0.0,  1.0,  0.0,
        0.0,  0.0,  0.0,  1.0
    ]
    
    glPushMatrix()
    glMultMatrixf(matriz_cisalhamento)
    
    desenhar_cubo()
    
    glPopMatrix()
    
    glutSwapBuffers()

def teclado(key, x, y):
    global sh

    if key == b'h':
        sh += 0.05
    elif key == b'H':
        sh -= 0.05
    elif key == b'z':
        sh = 0.0 
        
    glutPostRedisplay()

def inicializar():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 10.0)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(600, 600)
glutCreateWindow(b"O Cubo Primordial - Arte do Cisalhamento")
inicializar()
glutDisplayFunc(display)
glutKeyboardFunc(teclado) 
glutMainLoop()