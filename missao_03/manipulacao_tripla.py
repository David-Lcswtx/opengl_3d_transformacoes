import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

anguloY = 0.0
posicaoX = 0.0
escalaZ = 1.0

def prisma():

    gl.glBegin(gl.GL_TRIANGLES)

    gl.glColor3f(1.0, 0.0, 0.0)

    gl.glVertex3f(0.0, 0.8, 0.6)
    gl.glVertex3f(-0.8, 0.8, -0.6)
    gl.glVertex3f(0.8, 0.8, -0.6)

    gl.glColor3f(1.0, 1.0, 0.0)

    gl.glVertex3f(0.0, -0.8, 0.6)
    gl.glVertex3f(0.8, -0.8, -0.6)
    gl.glVertex3f(-0.8, -0.8, -0.6)

    gl.glEnd()


    gl.glBegin(gl.GL_QUADS)

    gl.glColor3f(0.0, 0.0, 1.0)

    gl.glVertex3f(0.0, 0.8, 0.6)
    gl.glVertex3f(0.0, -0.8, 0.6)
    gl.glVertex3f(-0.8, -0.8, -0.6)
    gl.glVertex3f(-0.8, 0.8, -0.6)

    gl.glColor3f(0.0, 1.0, 0.0)

    gl.glVertex3f(0.0, 0.8, 0.6)
    gl.glVertex3f(0.8, 0.8, -0.6)
    gl.glVertex3f(0.8, -0.8, -0.6)
    gl.glVertex3f(0.0, -0.8, 0.6)

    gl.glColor3f(0.0, 1.0, 1.0)

    gl.glVertex3f(-0.8, 0.8, -0.6)
    gl.glVertex3f(-0.8, -0.8, -0.6)
    gl.glVertex3f(0.8, -0.8, -0.6)
    gl.glVertex3f(0.8, 0.8, -0.6)

    gl.glEnd()

def desenhar():

    global anguloY, posicaoX, escalaZ

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    glu.gluPerspective(45.0, 1.0, 0.1, 50.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    glu.gluLookAt(0.0, 0.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    gl.glScalef(1.0, 1.0, escalaZ)

    gl.glTranslatef(posicaoX, 0.0, 0.0)

    gl.glRotatef(anguloY, 0, 1, 0)

    gl.glColor3f(1.0, 1.0, 0.0)

    prisma()

    glut.glutSwapBuffers()


def deslocar(key, x, y):
    global anguloY, posicaoX, escalaZ

    if key == b"y":
        anguloY += 3.0
    elif key == b"Y":
        anguloY -= 3.0
    elif key == b"t":
        posicaoX += 0.1
    elif key == b"T":
        posicaoX -= 0.1
    elif key == b"e":
        escalaZ += 0.3
    elif key == b"E":
        escalaZ -= 0.3

    glut.glutPostRedisplay()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutInitWindowSize(600, 600)
glut.glutCreateWindow(b"O Nucleo da Manipulacao Tripla")
gl.glEnable(gl.GL_DEPTH_TEST)

glut.glutDisplayFunc(desenhar)
glut.glutKeyboardFunc(deslocar)

glut.glutMainLoop()
