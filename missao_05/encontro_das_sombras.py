import OpenGL.GL as gl
import OpenGL.GLUT as glut

reflexoY = 1.0
reflexoX = 1.0

def eixos():

    gl.glBegin(gl.GL_LINES)

    gl.glColor3f(1.0, 1.0, 1.0)

    gl.glVertex2f(-1.0, 0.0)
    gl.glVertex2f(1.0, 0.0)

    gl.glVertex2f(0.0, -1.0)
    gl.glVertex2f(0.0, 1.0)

    gl.glEnd()


def diamante():

    gl.glPushMatrix()

    gl.glScalef(reflexoX, reflexoY, 1.0)

    gl.glColor3f(0.0, 1.0, 1.0)

    gl.glBegin(gl.GL_POLYGON)

    gl.glVertex2f(0.2, 0.6)
    gl.glVertex2f(0.3, 0.7)
    gl.glVertex2f(0.7, 0.7)
    gl.glVertex2f(0.8, 0.6)
    gl.glVertex2f(0.5, 0.2)

    gl.glEnd()

    gl.glPopMatrix()


def display():

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    diamante()
    eixos()

    glut.glutSwapBuffers()


def teclado(key, x, y):

    global reflexoX, reflexoY

    if key == b"x":
        reflexoY = -reflexoY
    elif key == b"y":
        reflexoX = -reflexoX

    glut.glutPostRedisplay()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(700, 700)
glut.glutCreateWindow(b"O Encontro das Sombras")

glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(teclado)

glut.glutMainLoop()
