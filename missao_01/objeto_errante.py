import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glBegin(gl.GL_QUADS)

    gl.glColor3f(1.0, 1.0, 0.0)
    gl.glVertex2f(-0.2, 0.2)
    gl.glVertex2f(-0.2, -0.2)
    gl.glVertex2f(0.2, -0.2)
    gl.glVertex2f(0.2, 0.2)

    gl.glEnd()
    gl.glFlush()

def deslocar(key, x, y):
    if key == b"d":
        gl.glTranslate(0.1, 0.0, 0.0)
        glut.glutPostRedisplay()
    elif key == b"a":
        gl.glTranslate(-0.1, 0.0, 0.0)
        glut.glutPostRedisplay()
    elif key == b"s":
        gl.glTranslate(0.0, -0.1, 0.0)
        glut.glutPostRedisplay()
    elif key == b"w":
        gl.glTranslate(0.0, 0.1, 0.0)
        glut.glutPostRedisplay()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
glut.glutInitWindowSize(650, 650)
glut.glutCreateWindow(b"Objeto Errante")
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(deslocar)
glut.glutMainLoop()
