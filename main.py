import pygame

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def myinit():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(0,500,0,500)
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5,0.2,0.3)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex2f(100,100)
    glVertex2f(300,200)
    glVertex2f(200,300)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(100,100)
    glVertex2f(300,200)
    glVertex2f(300,200)
    glVertex2f(200,300)
    glVertex2f(200,300)    
    glVertex2f(100,100)
    glEnd()
    glFlush()
    
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowPosition(100,100)
glutCreateWindow("Teste")
myinit()
glutDisplayFunc(display)
glutMainLoop()
