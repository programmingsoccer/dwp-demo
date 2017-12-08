#!/usr/bin/env python
import pango
import cairo
import pangocairo
import pygame
import math
import subprocess

pygame.init()

#class Row:
#    """A class for rows of typical terminal text"""
#    def __init__(self, instr):
#        self.str = instr
#
#class RichRow(Row):
#    """A class for rows of rich text"""

class Terminal:
    """A class that defines an instance of a terminal"""
    size = 600,400
    def __init__(self):
        # Initialize pygame with 32-bit colors. This setting stores the pixels
        # in the format 0x00rrggbb.
        self.screen = pygame.display.set_mode(self.size, 0, 32)
        
        # Get a reference to the memory block storing the pixel data.
        self.pixels = pygame.surfarray.pixels2d(self.screen)

        # Set up a Cairo surface using the same memory block and the same pixel
        # format (Cairo's RGB24 format means that the pixels are stored as
        # 0x00rrggbb; i.e. only 24 bits are used and the upper 16 are 0).
        self.csurface = cairo.ImageSurface.create_for_data(
                self.pixels.data, cairo.FORMAT_RGB24, self.size[0], self.size[1])

        # Set up a Cairo context to draw shapes to
        self.ccontext = cairo.Context(self.csurface)

        # Make a background rectangle
        self.ccontext.rectangle(0, 0, self.size[0], self.size[1])
        self.ccontext.set_source_rgb(255, 255, 255)
        self.ccontext.fill()

        # Print text to the screen
        self.pcontext = pangocairo.CairoContext(self.ccontext)
        self.playout  = self.pcontext.create_layout()
        self.pfont    = pango.FontDescription("Mono 12")
        self.playout.set_font_description(self.pfont)
        self.playout.set_text("hello world")
        self.ccontext.set_source_rgb(0, 0, 0)
        self.pcontext.update_layout(self.playout)
        self.pcontext.show_layout(self.playout)

    def open(self):
        self.file = open("/home/u669373/dynamic-text.txt")

    def readBlitRoutine(self, val):
        # Make a background rectangle
        self.ccontext.rectangle(0, 0, self.size[0], self.size[1])
        self.ccontext.set_source_rgb(255, 255, 255)
        self.ccontext.fill()
        
        # Print text to the screen
        self.playout.set_text(self.file.readline())             # NOTE TO SELF
        self.ccontext.set_source_rgb(0, 0, 0)       # readBlitRoutine should be renamed to blitRoutine, and
        self.pcontext.update_layout(self.playout)   # additional functions should be made to parse the incoming
        self.pcontext.show_layout(self.playout)     # swarm of stdout terminal data.

sessions = []
sessions.append(Terminal())
sessions[0].open();
# Flip the changes into view.
#pygame.display.flip()

# Wait for the user to quit.
i = 0

while pygame.QUIT not in [e.type for e in pygame.event.get()]:
    pygame.display.flip();
    for session in sessions:
        i += 1
        print(session.size)
        session.readBlitRoutine(i);

  
