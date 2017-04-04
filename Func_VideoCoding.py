#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

switch = -1


def coding_switch(self):
    switch = self.switch*-1
    return switch


def keypress_coding(self):
    pass


def save_file(self):
    pass

if __name__ == '__main__':
    pygame.init()
    waitingKeyPress = True
    while waitingKeyPress:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                print("hoge")
                waitingKeyPress = False
            else:
                print("no press")
