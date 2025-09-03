from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

class Cubo:
    def __init__(self, centro=(0.0, 0.0, 0.0), arista=1.0):
        self.cx, self.cy, self.cz = map(float, centro)
        self.arista = float(arista)
        self.rx = 0.0
        self.ry = 0.0
        self.rz = 0.0

    def set_centro(self, centro):
        self.cx, self.cy, self.cz = map(float, centro)

    def set_arista(self, arista):
        self.arista = float(arista)

    def rotar(self, angulos):
        ax, ay, az = map(float, angulos)
        self.rx += ax
        self.ry += ay
        self.rz += az

    def trasladar(self, destino):
        self.cx, self.cy, self.cz = map(float, destino)

    def rotacion_por_pivote(self, pivote, angulos):
        px, py, pz = map(float, pivote)
        ax_d, ay_d, az_d = map(float, angulos)
        ax, ay, az = map(math.radians, (ax_d, ay_d, az_d))
        x = self.cx - px
        y = self.cy - py
        z = self.cz - pz
        cosy, siny = math.cos(ay), math.sin(ay)
        x, z = x * cosy + z * siny, -x * siny + z * cosy
        cosx, sinx = math.cos(ax), math.sin(ax)
        y, z = y * cosx - z * sinx, y * sinx + z * cosx
        cosz, sinz = math.cos(az), math.sin(az)
        x, y = x * cosz - y * sinz, x * sinz + y * cosz
        self.cx = px + x
        self.cy = py + y
        self.cz = pz + z
        self.rotar((ax_d, ay_d, az_d))

    def mover(self, velocidad, direccion, tiempo):
        dx = velocidad * direccion[0] * tiempo
        dy = velocidad * direccion[1] * tiempo
        dz = velocidad * direccion[2] * tiempo
        self.cx += dx
        self.cy += dy
        self.cz += dz

    def draw(self):
        glPushMatrix()
        glTranslatef(self.cx, self.cy, self.cz)
        glRotatef(self.rx, 1.0, 0.0, 0.0)
        glRotatef(self.ry, 0.0, 1.0, 0.0)
        glRotatef(self.rz, 0.0, 0.0, 1.0)
        glScalef(self.arista, self.arista, self.arista)

        glBegin(GL_QUADS)

        # frente
        glColor3f(1.0, 0.2, 0.2)
        glNormal3f(0.0, 0.0, 1.0)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)

        # atrás
        glColor3f(0.2, 1.0, 0.2)
        glNormal3f(0.0, 0.0, -1.0)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)

        # izquierda
        glColor3f(0.2, 0.4, 1.0)
        glNormal3f(-1.0, 0.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5, -0.5)

        # derecha
        glColor3f(1.0, 1.0, 0.2)
        glNormal3f(1.0, 0.0, 0.0)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5,  0.5)

        # arriba
        glColor3f(1.0, 0.2, 1.0)
        glNormal3f(0.0, 1.0, 0.0)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)

        # abajo
        glColor3f(0.2, 1.0, 1.0)
        glNormal3f(0.0, -1.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f(-0.5, -0.5,  0.5)

        glEnd()
        glPopMatrix()
