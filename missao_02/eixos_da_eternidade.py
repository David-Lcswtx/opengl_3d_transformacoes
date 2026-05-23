import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

anguloX = 0.0
anguloY = 0.0
anguloZ = 0.0


def desenhar():

    global anguloX, anguloY, anguloZ

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    glu.gluPerspective(45.0, 1.0, 0.1, 50.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    glu.gluLookAt(0.0, 0.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    gl.glRotatef(anguloX, 1, 0, 0)
    gl.glRotatef(anguloY, 0, 1, 0)
    gl.glRotatef(anguloZ, 0, 0, 1)

    gl.glColor3f(1.0, 1.0, 0.0)

    glut.glutWireCube(2.0)

    glut.glutSwapBuffers()


def deslocar(key, x, y):
    global anguloX, anguloY, anguloZ

    if key == b"x":
        anguloX += 3.0
    elif key == b"X":
        anguloX -= 3.0
    elif key == b"y":
        anguloY += 3.0
    elif key == b"Y":
        anguloY -= 3.0
    elif key == b"z":
        anguloZ += 3.0
    elif key == b"Z":
        anguloZ -= 3.0

    glut.glutPostRedisplay()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutInitWindowSize(600, 600)
glut.glutCreateWindow(b"Os Eixos da Eternidade")
gl.glEnable(gl.GL_DEPTH_TEST)

glut.glutDisplayFunc(desenhar)
glut.glutKeyboardFunc(deslocar)

glut.glutMainLoop()
