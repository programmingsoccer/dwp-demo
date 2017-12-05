#!/usr/bin/env python
import pango
import cairo
import pangocairo
import pygame
import math

pygame.init()

class Row:
    """A class for rows of typical terminal text"""
    def __init__(self, instr):
        self.str = instr

class RichRow(Row):
    """A class for rows of rich text"""

class Terminal:
    """A class that defines an instance of a terminal"""
    size = 400,400
    def __init__(self):
        # Initialize pygame with 32-bit colors. This setting stores the pixels
        # in the format 0x00rrggbb.
        self.screen = pygame.display.set_mode(self.size, 0, 32)
        
        # Get a reference to the memory block storing the pixel data.
        self.pixels = pygame.surfarray.pixels2d(self.screen)

        # Set up a Cairo surface using the same memory block and the same pixel
        # format (Cairo's RGB24 format means that the pixels are stored as
        # 0x00rrggbb; i.e. only 24 bits are used and the upper 16 are 0).
        self.cairo_surface = cairo.ImageSurface.create_for_data(
                self.pixels.data, cairo.FORMAT_RGB24, self.size[0], self.size[1])

terminal1 = Terminal()

# Flip the changes into view.
pygame.display.flip()

# Wait for the user to quit.
while pygame.QUIT not in [e.type for e in pygame.event.get()]:
	pass
