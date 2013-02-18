# Hey Preston, this is what a single line Python comment looks like.

"""
Multi-line comments look like this.
"""

import pygame

SIZE = 640, 480  # The dimensions, in pixels, of the display window
FRAME_RATE = 30  # The number of frames that will be drawn each second

BACKGROUND_COLOR = pygame.color.THECOLORS['lightskyblue']
CIRCLE_COLOR = pygame.color.THECOLORS['white']

# This is just a placeholder for Preston's update code
def update_position(ball, frame_rate):
	return [x,y]

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
			
			# Until Preston implements the Ball class, balls are
			# just position coordinates.
			balls.append([x,y])

		elif event.type == pygame.QUIT:
			exit(0)

	screen.fill(BACKGROUND_COLOR)  # Get ready to clear the display.
	
	# For each ball, update its position and then get ready to draw it.
	for i in range(len(balls)):
		# Update ball positions
		balls[i] = update_position(balls[i], FRAME_RATE)

		# Get ready to draw a white ball of border width 1 and radius 20
		# to the screen, centered at the given position.
		pygame.draw.circle(screen, CIRCLE_COLOR, balls[i], 20, 1)
	
	pygame.display.update()  # Done getting ready. Redraw the display.

	# Wait around for 1/FRAME_RATE seconds before restarting this loop.
	clock.tick(FRAME_RATE)
