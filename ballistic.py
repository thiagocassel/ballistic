import pygame, math, random

def main():
    #set parameters
    global WIDTH, HEIGHT, FLOOR
    global highest_score, level, shots, shoot
    global BALL_RADIUS, ball_x, ball_y, ball_x_speed, ball_y_speed
    global gravity_acc
    global target_size
    global obstacle_speed, obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT
    global cloud_x
 
    #set window dimensions
    WIDTH = 800
    HEIGHT = 420
    FLOOR = 20

    #set highest score
    highest_score = 0
    #set cannon ball's radius
    BALL_RADIUS = 8

    #set cannon ball's initial position
    ball_x = BALL_RADIUS
    ball_y = HEIGHT - FLOOR - BALL_RADIUS

    #set cannon ball's initial speed
    ball_x_speed = 0
    ball_y_speed = 0

    #set initial gravity acceleration (parameter is not real) -> parameter turns bigger than zero with mouse click
    gravity_acc = 516

    #set initial level
    level = 1
    #set shots left
    shots = 5

    #set initial target size
    target_size = 100

    #set obstacle initial parameters
    obstacle_speed = 0
    obstacle_x = -200
    obstacle_y = -200
    OBSTACLE_WIDTH = 20
    OBSTACLE_HEIGHT = 70

    #boolean variable used to update cannon ball's position only after the shot
    shoot = False

    #set cloud pos
    cloud_x = -800

    set_target_position()
    set_wind()

    sounds.over.play()


#set wind
def set_wind():
    global wind_speed
    global wind_dir

    wind_speed = round(random.uniform(-5, 5),2)
    if wind_speed > 0:
        wind_dir = "East"
    elif wind_speed < 0:
        wind_dir = "West"
    else:
        wind_dir = "None"

def set_target_position():
    global target_x
    global target_y

    target_x = random.randint(WIDTH / 2, WIDTH - math.ceil(target_size))
    target_y = random.randint(math.floor(0.625 * (HEIGHT - FLOOR)), HEIGHT - FLOOR - math.floor(target_size))


def on_mouse_down():
    #shoots
    global ball_x_speed , ball_y_speed
    global gravity_acc
    global mouse_x, mouse_y
    global intensity, angle
    global shoot

    if not shoot:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x = mouse_x
        y = mouse_y - HEIGHT + FLOOR

        intensity = math.sqrt((x * x) + (y * y))
        angle = math.acos(x / intensity) 

        ball_x_speed =  intensity * math.cos(angle)
        ball_y_speed = -intensity * math.sin(angle)
        shoot = True


def update(dt):
    global ball_x, ball_y
    global ball_x_speed, ball_y_speed
    global gravity_acc
    global obstacle_x, obstacle_y, obstacle_speed
    global level
    global hit
    global shoot
    global cloud_x


    #obstacle movement
    if obstacle_y > HEIGHT - FLOOR - OBSTACLE_HEIGHT:
        obstacle_y = 0
    obstacle_y += obstacle_speed * dt

    #cannon ball trajectory
    if shoot:
        ball_y_speed += gravity_acc * dt
        ball_y += ball_y_speed * dt
        ball_x += ball_x_speed * dt + wind_speed

    #clouds
    cloud_x += 10 * wind_speed * dt

    #check if cannon ball hits boundaries or obstacle
    if (ball_y > HEIGHT - FLOOR - BALL_RADIUS) or (ball_x > WIDTH - BALL_RADIUS) or ((ball_x + BALL_RADIUS) >= obstacle_x and (ball_x - BALL_RADIUS) <= (obstacle_x + OBSTACLE_WIDTH) and (ball_y + BALL_RADIUS) > obstacle_y and (ball_y - BALL_RADIUS) < (obstacle_y + OBSTACLE_HEIGHT)):
        hit = False
        shoot = False
        reset()

    #check if the cannon ball hits the target
    if ball_x + BALL_RADIUS > target_x and ball_x - BALL_RADIUS < target_x + target_size and ball_y + BALL_RADIUS > target_y and ball_y - BALL_RADIUS < target_y + target_size: 
        hit = True
        shoot = False
        reset()


def reset():
    global level
    global ball_x, ball_y
    global ball_x_speed, ball_y_speed
    global gravity_acc
    global target_x, target_y, target_size
    global shots
    global obstacle_speed, obstacle_x, obstacle_y
    global highest_score
    global cloud_x

    if hit:
        sounds.bomb.play()
        level += 1
        #set target size
        target_size = 150 / level

        set_target_position()
        set_wind()

        if level == 5:
            obstacle_speed = 300
            obstacle_x = random.randint(WIDTH / 4, math.floor(0.4625 * WIDTH))
        elif level > 5:
            obstacle_speed += 30
            obstacle_x = random.randint(WIDTH / 4, math.floor(0.4625 * WIDTH))

    else:
        if shots == 1:
            sounds.over.play()
            if level -1 > highest_score:
                highest_score = level - 1
            level = 1
            shots = 5
            obstacle_x = -200
            obstacle_y = -200
            obstacle_speed = 0
            target_size = 150 / level
            set_target_position()
            set_wind()
        else:
            shots -= 1
            set_wind()

    #set cannon ball to initial position
    ball_x = BALL_RADIUS
    ball_y = HEIGHT - FLOOR - BALL_RADIUS

    #set cannon ball to initial speed
    ball_x_speed = 0
    ball_y_speed = 0


def draw():
    #fill screen
    screen.fill((35, 200, 118))

    #fill sky
    screen.draw.filled_rect(
        Rect(
            (0, 0),
            (WIDTH, HEIGHT - FLOOR)
        ),
        color=(0, 220, 255)
    )

    #draw clouds
    for i in range (0, 40):
        for j in range(0,3):
            if i % 2 == 0:
                screen.draw.filled_circle((cloud_x + 100 * i + 15 * j, 120), 20, (255, 255, 255))
            else:
                screen.draw.filled_circle((cloud_x + 100 * i + 15 * j, 75), 20, (255, 255, 255))                

    # draw target
    screen.draw.filled_rect(
        Rect(
            (target_x, target_y),
            (target_size, target_size)
        ),
        color=(255, 0, 0)
    )

    # draw obstacle
    screen.draw.filled_rect(
        Rect(
            (obstacle_x, obstacle_y),
            (OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        ),
        color=(255, 125, 0)
    )

    #draw the cannon ball
    screen.draw.filled_circle((ball_x, ball_y), BALL_RADIUS, (0, 0, 0))

    #show level and shots left
    screen.draw.text('Level: ' + str(level) + ' Shots left: ' + str(shots) + ' Highest Score: ' + str(highest_score)
            + '\nWind speed ' + str(abs(wind_speed)) + 'units/s' + ' Wind Direction: ' + wind_dir, (0, 0), color=(0, 0, 0))

main()
