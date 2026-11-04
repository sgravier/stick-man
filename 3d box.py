import pygame
from pygame import *
import math
xo = 500
yo = 250
rx1 = 300
rx2 = 1000
ry2 = 150
ry1 =150
thdh = 500
thdw = 0
player_angle = 0
ray_length = 1000
runing = True
window = display.set_mode((1000, 500))
display.set_caption('3D box')
list_of_obstacles = []
obstarect = draw.rect(window, (255, 0, 0), (xo, yo, 10, 10))
wall1 = draw.rect(window, (255, 0, 0), (950, 0, 500, 1000))
wall2 = draw.rect(window, (255, 0, 0), (0, -10, 1000, 50))
wall3 = draw.rect(window, (255, 0, 0), (0, 0, 50, 1000))
wall4 = draw.rect(window, (255, 0, 0), (0, 450, 1000, 50))
draw.circle(window, (0, 255, 0), (rx1 // 5, ry1 // 5), 10 // 5)
list_of_obstacles.append((wall1, (255, 0, 0)))
list_of_obstacles.append((obstarect, (0, 255, 0)))
list_of_obstacles.append((wall2, (255, 0, 0)))
list_of_obstacles.append((wall3, (255, 0, 0)))
list_of_obstacles.append((wall4, (255, 0, 0)))
display.flip()
nor = 0
rdto = []
shortest_distance = 999999999999
while runing:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
        closest_hit = None
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                list_of_obstacles = []
                player_angle -= 10
                list_of_obstacles.append((obstarect, (255, 0, 0)))
                list_of_obstacles.append((wall2, (255, 0, 0)))
                list_of_obstacles.append((wall3, (255, 0, 0)))
                list_of_obstacles.append((wall4, (255, 0, 0)))
                list_of_obstacles.append((wall1, (255, 0, 0)))
            if event.key == K_RIGHT:
                list_of_obstacles = []
                player_angle += 10
                list_of_obstacles.append((obstarect, (255, 0, 0)))
                list_of_obstacles.append((wall2, (255, 0, 0)))
                list_of_obstacles.append((wall3, (255, 0, 0)))
                list_of_obstacles.append((wall4, (255, 0, 0)))
                list_of_obstacles.append((wall1, (255, 0, 0)))
            if event.key == K_UP:
                rx1 += math.cos(math.radians(player_angle)) * 10
                ry1 += math.sin(math.radians(player_angle)) * 10
                list_of_obstacles.append((obstarect, (255, 0, 0)))
                list_of_obstacles.append((wall2, (255, 0, 0)))
                list_of_obstacles.append((wall3, (255, 0, 0)))
                list_of_obstacles.append((wall4, (255, 0, 0)))
                list_of_obstacles.append((wall1, (255, 0, 0)))
            if event.key == K_DOWN:
                rx1 -= math.cos(math.radians(player_angle)) * 10
                ry1 -= math.sin(math.radians(player_angle)) * 10
                list_of_obstacles.append((obstarect, (255, 0, 0)))
                list_of_obstacles.append((wall2, (255, 0, 0)))
                list_of_obstacles.append((wall3, (255, 0, 0)))
                list_of_obstacles.append((wall4, (255, 0, 0)))
                list_of_obstacles.append((wall1, (255, 0, 0)))
            if event.key == K_a:
                list_of_obstacles = []
                player_angle += 10
                list_of_obstacles.append((obstarect, (255, 0, 0)))
                list_of_obstacles.append((wall2, (255, 0, 0)))
                list_of_obstacles.append((wall3, (255, 0, 0)))
                list_of_obstacles.append((wall4, (255, 0, 0)))
                list_of_obstacles.append((wall1, (255, 0, 0)))

            if event.key == K_d:
                list_of_obstacles = []
                player_angle -= 10
                list_of_obstacles.append((obstarect, (255, 0, 0)))
                list_of_obstacles.append((wall2, (255, 0, 0)))
                list_of_obstacles.append((wall3, (255, 0, 0)))
                list_of_obstacles.append((wall4, (255, 0, 0)))
                list_of_obstacles.append((wall1, (255, 0, 0)))
            if event.key == K_w:
                rx1 += math.cos(math.radians(player_angle)) * 10
                ry1 += math.sin(math.radians(player_angle)) * 10
                list_of_obstacles.append((obstarect, (255, 0, 0)))
                list_of_obstacles.append((wall2, (255, 0, 0)))
                list_of_obstacles.append((wall3, (255, 0, 0)))
                list_of_obstacles.append((wall4, (255, 0, 0)))
                list_of_obstacles.append((wall1, (255, 0, 0)))
            if event.key == K_s:
                rx1 -= math.cos(math.radians(player_angle)) * 10
                ry1 -= math.sin(math.radians(player_angle)) * 10
                list_of_obstacles.append((obstarect, (255, 0, 0)))
                list_of_obstacles.append((wall2, (255, 0, 0)))
                list_of_obstacles.append((wall3, (255, 0, 0)))
                list_of_obstacles.append((wall4, (255, 0, 0)))
                list_of_obstacles.append((wall1, (255, 0, 0)))
    n = 0
    for c in range(60):
        shortest_distance = 999999999999
        closest_hit = None
        angle = player_angle + c
        rx2 = rx1 + math.cos(math.radians(angle)) * ray_length

        ry2 = ry1 + math.sin(math.radians(angle)) * ray_length
        for obst in list_of_obstacles:
            ray1 = obst[0].clipline((rx1, ry1), (rx2, ry2))

            if ray1:
                distans = math.dist((rx1, ry1), ray1[0])
                if distans < shortest_distance:
                    shortest_distance = distans
                    closest_hit = ray1[0]

        if closest_hit:
            # draw.line(window, (255, 255, 255), (rx1, ry1), closest_hit)
            sow = 100000 / shortest_distance
            color_intensity = int(max(0, 255 - (shortest_distance / 3)))
            draw.rect(window, (color_intensity, 0, 0), (n, 100, 10, sow))
        ry2 += 1
        n += 10

    time.Clock().tick(60)
    # draw.circle(window, (0, 0, 255), (rx1, ry1), 10)
    rx2 = 1000
    ry2 = 100
    list_of_obstacles = []
    draw.rect(window, (255, 0, 0), (xo // 5, yo // 5, 10 // 5, 10 // 5))
    draw.rect(window, (255, 0, 0), (950 // 5, 0 // 5, 500 // 5, 1000 // 10))
    draw.rect(window, (255, 0, 0), (0 // 5, -10 // 5, 1000 // 5, 50 // 5))
    draw.rect(window, (255, 0, 0), (0 // 5, 0 // 5, 50 // 5, 1000 // 10))
    draw.rect(window, (255, 0, 0), (0 // 5, 450 // 5, 1000 // 5, 50 // 5))
    draw.circle(window, (0, 255, 0), (rx1 // 5, ry1 // 5), 10 // 5)
    list_of_obstacles.append((wall1, (255, 0, 0)))
    list_of_obstacles.append((obstarect, (0, 255, 0)))
    list_of_obstacles.append((wall2, (255, 0, 0)))
    list_of_obstacles.append((wall3, (255, 0, 0)))
    list_of_obstacles.append((wall4, (255, 0, 0)))
    display.flip()
display.quit()