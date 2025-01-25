import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("05 Performance Task 1 - Montiano Pogi")

glEnable(GL_DEPTH_TEST)

gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -10)

vertices = [
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (-1, 1, 1),
    (-1, -1, -1),
    (-1, -1, 1),
    (-1, 1, -1)
]

triangles = [
    (0, 1, 2), (0, 2, 3),
    (4, 5, 6), (4, 7, 5),
    (0, 4, 6), (0, 6, 3),
    (1, 7, 5), (1, 5, 2),
    (0, 1, 7), (0, 7, 4),
    (3, 2, 5), (3, 5, 6)
]

def draw_cube(color):
    glBegin(GL_TRIANGLES)
    glColor4f(*color)
    for triangle in triangles:
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_cubes():
    # First Cube (Green)
    glPushMatrix()
    glTranslatef(0, 0, 0) 
    glScalef(0.3, 0.3, 0.3) 
    draw_cube((0, 1, 0, 1)) 
    glPopMatrix()

    # Second Cube (Orange)
    glPushMatrix()
    glTranslatef(0.5, 0, 0)  
    glScalef(0.3, 0.3, 0.3) 
    draw_cube((1, 0.647, 0, 1))  
    glPopMatrix()

    # Third Cube (Blue)
    glPushMatrix()
    glTranslatef(1, 0, 0)
    glScalef(0.3, 0.3, 0.3) 
    draw_cube((0, 0, 1, 1))  
    glPopMatrix()

    # Fourth Cube (Red)
    glPushMatrix()
    glTranslatef(1.5, 0, 0) 
    glScalef(0.3, 0.3, 0.3)  
    draw_cube((1, 0, 0, 1))  
    glPopMatrix()

    # Fifth Cube (Pink)
    glPushMatrix()
    glTranslatef(2, 0, 0)
    glScalef(0.3, 0.3, 0.3) 
    draw_cube((1, 0.411, 0.705, 1))  
    glPopMatrix()

def reset_view():
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -10)

x_translation = 0
roll_angle = 0
rotate_angle = 0
auto_rotate = False  
auto_roll = False  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  
                x_translation -= 1
            if event.key == pygame.K_d:  
                x_translation += 1
            if event.key == pygame.K_w:  
                roll_angle += 15
                auto_roll = True
            if event.key == pygame.K_s:  
                roll_angle -= 15
                auto_roll = True
            if event.key == pygame.K_r:  
                auto_rotate = True
                auto_roll = False  

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    reset_view()
    
    glTranslatef(x_translation, 0, 0)  

    if auto_rotate:
        rotate_angle += 1
        glRotatef(rotate_angle, 0, 1, 1) 

    if auto_roll:
        roll_angle += 0.5  
    glRotatef(roll_angle, 1, 0, 0)  

    draw_cubes()

    pygame.display.flip()
    pygame.time.wait(15)
