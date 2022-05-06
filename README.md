# BALLISTIC
#### Video Demo:  <URL https://www.youtube.com/watch?v=EDNF4ZUk2Js>
#### Description:
Ballistic is a small game developed in Python, using the Pygame Zero
framework, in which the goal is to hit a target that gets
increasingly smaller and changes it's position randomly at each level.

It contains a file named 'ballistic.py' with the game script, a folder
named 'sounds', with the sound effects used in the game and a file named
ballistic.bat

## HOW TO RUN -> .BAT FILE

To run the game, you must edit the file ballistic.bat, including the path where
your Python exe is stored where indicated and the path where ballistic.py is stored
where indicated. The file example.bat is an example of how the file ballistic.bat
should look.

## HOW TO PLAY

To make a shoot, just left-click your mouse. Mouse clicks made with
the cannon ball in the air are ignored.

The cannon ball's initial speed and launch angle are defined by the mouse position
relative to the initial position of the cannon ball (at the bottom left
corner of the screen).

The farther the mouse pointer is from the bottom left corner, the higher
is the range of the shot. The closer the mouse pointer is from the ground,
the shallower the show will be.

The game will come to an end after five missed shots, when it will be reseted.
The wind changes everytime you try a new shot, so pay attention to the wind's
direction and speed displayed in the top left corner of the screen (the clouds'
movement is also a hint of the wind's direction and spped). From level five on,
a moving obstacle will appear on the screen, at a random distance from the cannon
ball's origin. It will get faster as you advance levels.

The highest score is the biggest level completed, i.e, the last level in
which the player hit the target. For example, if your last missed shot occours at
level 7,your score will be 6. The highest score is reseted when the game window is
closed.

## COMMENTS ON DEVELOPMENT

The script was written in Python, using the Pygame Zero framework.
For simplicity,the script is not object oriented.
The first thing was to set general parameters, such as sizes and positions.
The gravity's acceleration parameter is equal to 516. There's no math behind it,
it is a result of some attempts to check if the cannon ball trajectory would feel real.

At first, the obstacle's position is set to a number off screem, as it is set to
appear only after level 5, when it's x coordinate is set to a on screen position.

The boolean variable 'shoot' is used to define of a shot is made. When it's value is
false, no dynamics area applied to the cannon ball. When 'shoot' is True, mouse clicks
are ignored, making impossible to the player to change the cannon ball's trajectory after
the cannon ball is in the air. The variable 'shoot' is reseted to 'False' after the cannon
ball hits a "wall" (screen boundaries), the target or the obstacle.

The functions 'set_wind' and 'set_target_position' define the wind parameters (speed
and direction) and the target's location and size. The wind is reseted at every new shot,
regardless of the result (a hit or a miss). The target is set to a new random position and
size only after a hit. There's a region in which the target can be placed, in order not
to make some levels impossible (or to easy). The parameters used to define the target region
were also defined after some attemps.

The shot's range and angle are defined based on the mouse's pointer at the moment of a left
button click. The math behind it is quite simple, just applying Pythagoras's theorem.

The update function is a built-in function form Pygame Zero, called repeatedly 60 times a
second. It is within this function that all of the objects dynamics are described.

At first, the obstacle movement is defined. For simplicity reasons, it always moves in the
same direction (downards). In future developments, obstacles can have different trajectories.

Then, the cannon ball's movement is described. On the X axis, it suffers the effects of the wind.
On the Y axis, it suffers the effects of gravity. As said before, the cannon ball's position
is not updated the the boolean variable 'shoot' is False.

The clouds's movement is quite simple, just a multiplier of the wind speed, in order to give
the player a visual look of the wind's direction and speed.

Finally, the update function checks if the cannon ball hits the target (a hit), the obstacle
or the screen boundaries (a miss). In both cases, the funcion 'reset' is called, after
definig 'shoot' to false, indicating that the cannon ball must no be subjected to any dynamics
and the boolean variable 'hit' to True in case of a hit or to False in case of a miss

In the reset function, the cannon ball is raplaced to it's origin. In case of a hit, the
target's position and size are redefined. From level 5 on, the obstacle's position is setted to
an on screen position, with it's speed increasing at each new level.

In case of a miss, the shot count is updated and the wind is reset. If the shot count goes to
zero, the highest socre is updated if that's the case, and the game is restarted, by redefining
it's original parameters.

The last function of the script is the 'draw' function, responsible for drawing the game's
elements in the screen

The first layer is the ground color ((35, 200, 118)). The second layer is the sky (color (0, 220, 255)).
Next, the dynamic elements are drawn. The clouds are drawn using two for loops.
To finish, a text informing the current level, the highest score, shots left and the wind parameters
is included in the screen.

## IMPROVEMENTS FOR FUTURE VERSIONS:
- Moving target: making the target change it's position by different patterns.
- Showing a cannon that follows the mouse pointer before the shot:. Include the cannon and
make it point to the mouse direction, giving the player a better idea of the cannon ball's
trajectory.
- Estimate land spotting: trace as estimated landing spot for the cannon ball, ignoring the
wind effects (otherwise it would be to easy...)
- Include other obstacles, such as birds: The idea is to include more and more birds, with
different moving patterns, and make then a sudden death obstacle, i.e., if you shoot one of
the birds, the game comes to an end.
- Change the lanscape, including hills, mountains, etc: turn the game a little bit more
difficult by including static obstacles
- Save highest scores in a database: Create a login menu and a database so that the highest
score is saved after closing the game's window.

The code used as reference the examples showed at
https://simplegametutorials.github.io/pygamezero/

The sound effects were downloaded from
https://mixkit.co/free-sound-effects/