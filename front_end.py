# Hey Preston. As you might guess, this is a single line Python comment.

"""
Multi-line
comments
look
like
this.
"""

import pygame

SIZE = 640, 480  # The dimensions, in pixels, of the display window
FRAME_RATE = 30  # The number of frames that will be drawn each second
RADIUS = 10

BACKGROUND_COLOR = pygame.color.THECOLORS['lightskyblue']
CIRCLE_COLOR = pygame.color.THECOLORS['white']

# This is just a placeholder for Preston's update code
def update_position(ball, frame_rate):
	# If a ball reaches the edge of the screen, negate its velocity so that it
	# moves in the other direction.
	if (ball[1] - RADIUS < 0) or (ball[1] + RADIUS > SIZE[1]):
		ball[2] = -ball[2]
	
	# Update the position of the ball using its velocity
	ball[1] = ball[1] + ball[2]
	
	return ball

# The pygame library is special in that it's not ready to use immediately upon
# import, but requires this call to finish setting up.
pygame.init()

screen = pygame.display.set_mode(SIZE)  # A display window to draw in.
clock = pygame.time.Clock()  # A clock to separate neighboring frames.
balls = []  # A list to hold all of the balls in the simulation.

while True:
	# Process all of the events that happened in the last 1/FRAME_RATE
	# seconds. There are 3 types of events that we might be interested in:
	# mouse clicks in the window, keyboard presses, and quitting via the
	# close button in the top left.
	for event in pygame.event.get():
		# If there was a click somewhere, make a ball there.
		if event.type == pygame.MOUSEBUTTONDOWN:
			# Get the x and y position of the click.
			x = event.dict['pos'][0]
			y = event.dict['pos'][1]
			
			# Until Preston implements the Ball class, balls are just position
			# coordinates and a y-axis velocity.
			balls.append([x,y,1])

		elif event.type == pygame.QUIT:
			exit(0)

	screen.fill(BACKGROUND_COLOR)  # Get ready to clear the display.
	
	# For each ball, update its position and then get ready to draw it.
	for i in range(len(balls)):
		# Update ball positions
		balls[i] = update_position(balls[i], FRAME_RATE)
		
		# Get ready to draw a white ball of border width 1 and the given 
		# radius to the screen, centered at the given position.
		pygame.draw.circle(screen, CIRCLE_COLOR, balls[i][:2], 2*RADIUS, 1)
	
	pygame.display.update()  # Done getting ready. Redraw the display.

	# Wait around for 1/FRAME_RATE seconds before restarting this loop.
	clock.tick(FRAME_RATE)