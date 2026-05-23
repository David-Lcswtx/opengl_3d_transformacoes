import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

escalaA = 1.0
escalaB = 1.0
escalaC = 1.0

def triangulo():

    global escalaB

    gl.glPushMatrix()

    gl.glScalef(escalaB, escalaB, 1.0)

    gl.glBegin(gl.GL_TRIANGLES)

    gl.glColor3f(1.0, 0.0, 0.0)

    gl.glVertex2f(0.0, 0.4)
    gl.glVertex2f(-0.2, 0.0)
    gl.glVertex2f(0.2, 0.0)

    gl.glEnd()

    gl.glPopMatrix()

def chaleira():

    global escalaA

    gl.glPushMatrix()

    gl.glTranslatef(-1.3, 0.17, 0.0)

    gl.glScalef(escalaA, escalaA, escalaA)

    gl.glColor3f(0.0, 1.0, 0.0)

    glut.glutSolidTeapot(0.25)

    gl.glPopMatrix()


def esfera():

    gl.glPushMatrix()

    gl.glTranslatef(1.3, 0.17, 0.0)

    gl.glScalef(escalaC, escalaC, escalaC)

    gl.glColor3f(0.0, 0.0, 1.0)

    glut.glutWireSphere(0.2, 10, 10)

    gl.glPopMatrix()


def desenhar():

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    glu.gluPerspective(45.0, 1.0, 0.1, 50.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    glu.gluLookAt(0.0, 0.0, 6.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    chaleira()
    triangulo()
    esfera()

    glut.glutSwapBuffers()


def deslocar(key, x, y):
    global escalaA, escalaB, escalaC

    if key == b"1":
        escalaA += 0.1
    elif key == b"q":
        escalaA -= 0.1
    elif key == b"2":
        escalaB += 0.1
    elif key == b"w":
        escalaB -= 0.1
    elif key == b"3":
        escalaC += 0.1
    elif key == b"e":
        escalaC -= 0.1

    glut.glutPostRedisplay()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
glut.glutInitWindowSize(600, 600)
glut.glutCreateWindow(b"O Nucleo da Manipulacao Tripla")
gl.glEnable(gl.GL_DEPTH_TEST)

glut.glutDisplayFunc(desenhar)
glut.glutKeyboardFunc(deslocar)

glut.glutMainLoop()
