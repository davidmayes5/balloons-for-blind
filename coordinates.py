# Variables for compatability between screens
from win32api import GetSystemMetrics

# Developed on screen with 2560 width by 1440 height pixels
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dev_width = 2560
dev_height = 1440

x_scale = int(width/dev_width)
y_scale = int(height/dev_height)


# Title screen bottom row
title = {
    "settings": {"x": x_scale*100, "y": y_scale*285},
    "achievements": {"x": x_scale*100, "y": y_scale*470},
    "shop": {"x": x_scale*100, "y": y_scale*640},
    "trophy store": {"x": x_scale*100, "y": y_scale*820},

    "monkeys": {"x": x_scale*500, "y": y_scale*1275},
    "heroes": {"x": x_scale*810, "y": y_scale*1275},
    "play": {"x": x_scale*1110, "y": y_scale*1275},
    "play social": {"x": x_scale*1450, "y": y_scale*1275},
    "powers": {"x": x_scale*1750, "y": y_scale*1275},
    "knowledge": {"x": x_scale*2050, "y": y_scale*1275},

    "odyssey event": {"x": x_scale*2450, "y": y_scale*300},
    "race event": {"x": x_scale*2450, "y": y_scale*495},
    "boss bloon event": {"x": x_scale*2450, "y": y_scale*690}
}

navigation = {
    "back": {"x": x_scale*100, "y":y_scale*75}
}