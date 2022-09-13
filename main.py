import pygame

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def myinit():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(0,500,0,500)
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.9,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(100,100)
    glVertex2f(300,200)
    glEnd()
    glFlush()
    
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100,100)
glutCreateWindow("Meu fkfjsdfjksdfhn")
myinit()
glutDisplayFunc(display)
glutMainLoop()
