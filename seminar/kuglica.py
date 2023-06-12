import matplotlib.pyplot as plt
import numpy as np

ball_radius = 20
ball_mass = 1.0

wall_x_min = ball_radius
wall_x_max = 700 
wall_y_min = ball_radius
wall_y_max = 500 

def simulate_motion():
    ball_x = 100  
    ball_y = 100
    ball_speed = 50

    ball_angle = np.radians(45) 
    dt = 0.1 

    x = [ball_x]
    y = [ball_y]
    
    t = 0

    while True:
        
        if ball_x + ball_radius >= wall_x_max or ball_x - ball_radius <= wall_x_min:
            ball_angle = np.pi - ball_angle
        if ball_y + ball_radius >= wall_y_max or ball_y - ball_radius <= wall_y_min:
            ball_angle = -ball_angle

        
        ball_x += ball_speed * np.cos(ball_angle) * dt
        ball_y += ball_speed * np.sin(ball_angle) * dt
        
        if t >= 110:
            break

        t += dt

        x.append(ball_x)
        y.append(ball_y)

    return x, y

x_coords, y_coords = simulate_motion()

fig, ax = plt.subplots()
ax.set_xlim(0, 700)
ax.set_ylim(0, 500)
ax.set_aspect('equal', adjustable='box')

ball = plt.Circle((x_coords[0], y_coords[0]), ball_radius, fc='darkred')
ax.add_patch(ball)

ball_angle = np.radians(45) 

for i in range(1, len(x_coords)):
    ball.center = (x_coords[i], y_coords[i])

    if x_coords[i] + ball_radius >= wall_x_max or x_coords[i] - ball_radius <= wall_x_min:
        ball_angle = np.pi - ball_angle
    if y_coords[i] + ball_radius >= wall_y_max or y_coords[i] - ball_radius <= wall_y_min:
        ball_angle = -ball_angle

    plt.pause(0.01)

plt.show()
plt.close()