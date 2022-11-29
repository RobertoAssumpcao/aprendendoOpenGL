# Roberto de Paiva Assumpção
# 19102745

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

Width = 1024
Height = 600  

fAspect = 1.77
angle = 45


def Inicializa():
    glClearColor(0., 0., 1., 1.)


def Visualizacao():
    global angle, fAspect
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(angle, fAspect, 0.4, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 8, 20,
              0, 0, 0,
              0, 1, 0)


def ControlaMouse(button, state, x, y):
    global angle

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            if angle >= 10:
                angle -= 5
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:
            if angle <= 130:
                angle += 5
    Visualizacao()
    glutPostRedisplay()


def AlteraTamanhoJanela(Width, Height):
    if Height == 0:
        Height = 1

    glViewport(0, 0, Width, Height)
    fAspect = Width / Height

    Visualizacao()


def Desenhar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    color = [1.0, 0., 0., 1.]  # Cor do objeto
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    glPushMatrix()
    glTranslate(0, 0, 0)
    glScalef(10, 0.05, 10)
    glutWireCube(1.7)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0, -1, 0)
    glutWireTeapot(1.5)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-8, -4, -10)
    glRotatef(120, -170, 180, 180)
    glutWireCylinder(2, 2, 15, 12)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-10, -5, -20)
    glScalef(1, 6, 1)
    glutWireCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-10, -2, -20)
    glRotatef(120, -150, 180, 180)
    glutWireCone(3, 1, 8, 10)
    glPopMatrix()
    glutSwapBuffers()
    return


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutCreateWindow("APS2")
    glutDisplayFunc(Desenhar)
    glutReshapeFunc(AlteraTamanhoJanela)
    glutMouseFunc(ControlaMouse)
    Inicializa()
    glutMainLoop()
    return


if __name__ == '__main__': main()
