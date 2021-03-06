from display import *
from draw import *
from matrix import *

screen = new_screen()
c1 = [ 255, 255, 255 ]
matrix = new_matrix()
test = [[100, 100, 100, 1], [200, 200, 2, 1], [300, 300, 3, 1], [400, 400, 4, 1], [100, 400, 5, 1], [400, 100, 6, 1]] # n of x,y,z,1
bob = [[1, 1, 1, 1], [2.1, 1.1, 0.3, 0.6], [0.1, 0.23, 0.35, 0.67], [0.11, 0.94, 0.88, 0.65]]
brown = [117, 48, 2]
lshoe = [[63, 0, 0, 1], [183, 0, 0, 1], [183, 0, 0, 1], [183, 63, 0, 1], [183, 63, 0, 1], [94, 63, 0, 1], [94, 63, 0, 1], [94, 31, 0, 1], [94, 31, 0, 1], [63, 31, 0, 1], [63, 31, 0, 1], [63, 0, 0, 1]]
rshoe = [[313, 0, 0, 1], [438, 0, 0, 1], [438, 0, 0, 1], [438, 31, 0, 1], [438, 31, 0, 1], [406, 31, 0, 1], [406, 31, 0, 1], [406, 63, 0, 1], [406, 63, 0, 1], [313, 63, 0, 1], [313, 63, 0, 1], [313, 0, 0, 1]]
blue = [0, 0, 255]
overall1 = [[125, 64, 0, 1], [219, 64, 0, 1], [375, 64, 0, 1], [281, 64, 0, 1], [219, 64, 0, 1], [219, 95, 0, 1], [281, 64, 0, 1], [281, 95, 0, 1], [281, 95, 0, 1], [219, 95, 0, 1]]
overall2 = [[125, 64, 0, 1], [125, 126, 0, 1], [375, 64, 0, 1], [375, 126, 0, 1], [375, 126, 0, 1], [344, 126, 0, 1], [125, 126, 0, 1], [156, 126, 0, 1], [156, 126, 0, 1], [156, 188, 0, 1], [344, 126, 0, 1], [344, 188, 0, 1]]
overall3 = [[156, 188, 0, 1], [187, 188, 0, 1], [187, 188, 0, 1], [187, 281, 0, 1], [187, 281, 0, 1], [218, 281, 0, 1], [344, 188, 0, 1], [313, 188, 0, 1], [313, 188, 0, 1], [313, 281, 0, 1], [313, 281, 0, 1], [282, 281, 0, 1]]
overall4 = [[218, 281, 0, 1], [218, 218, 0, 1], [282, 281, 0, 1], [282, 218, 0, 1], [282, 218, 0, 1], [218, 218, 0, 1]]
yellow = [255, 239, 99]
buttons = [[219, 187, 0, 1], [188, 187, 0, 1], [188, 187, 0, 1], [188, 156, 0, 1], [188, 156, 0, 1], [219, 156, 0, 1], [219, 156, 0, 1], [219, 187, 0, 1], [281, 187, 0, 1], [312, 187, 0, 1], [312, 187, 0, 1], [312, 156, 0, 1], [312, 156, 0, 1], [281, 156, 0, 1], [281, 156, 0, 1], [281, 187, 0, 1]]
red = [255, 0, 0]
shirt1 = [[220, 280, 0, 1], [281, 280, 0, 1], [281, 280, 0, 1], [281, 219, 0, 1], [220, 280, 0, 1], [220, 219, 0, 1], [281, 219, 0, 1], [220, 219, 0, 1]]
shirt2 = [[63, 189, 0, 1], [126, 189, 0, 1], [126, 189, 0, 1], [126, 158, 0, 1], [126, 158, 0, 1], [157, 158, 0, 1], [63, 189, 0, 1], [63, 220, 0, 1], [63, 220, 0, 1], [94, 220, 0, 1], [94, 220, 0, 1], [94, 251, 0, 1], [94, 251, 0, 1], [125, 251, 0, 1], [125, 251, 0, 1], [125, 279, 0, 1], [125, 279, 0, 1], [186, 279, 0, 1]]
shirt3 = [[344, 158, 0, 1], [375, 158, 0, 1], [375, 158, 0, 1], [375, 189, 0, 1], [375, 189, 0, 1], [437, 189, 0, 1], [437, 189, 0, 1], [437, 220, 0, 1], [437, 220, 0, 1], [406, 220, 0, 1], [406, 220, 0, 1], [406, 251, 0, 1], [406, 251, 0, 1], [375, 251, 0, 1], [375, 251, 0, 1], [375, 279, 0, 1], [375, 279, 0, 1], [314, 279, 0, 1]]
skin = [224, 169, 29]
hand = [[63, 93, 0, 1], [124, 93, 0, 1], [63, 93, 0, 1], [63, 188, 0, 1], [438, 93, 0, 1], [438, 188, 0, 1], [438, 93, 0, 1], [376, 93, 0, 1]]
head = [[156, 281, 0, 1], [156, 437, 0, 1], [156, 437, 0, 1], [344, 437, 0, 1], [344, 437, 0, 1], [344, 281, 0, 1], [125, 344, 0, 1], [125, 406, 0, 1], [125, 406, 0, 1], [406, 406, 0, 1], [406, 406, 0, 1], [406, 375, 0, 1], [406, 375, 0, 1], [437, 375, 0, 1], [437, 375, 0, 1], [437, 344, 0, 1], [437, 344, 0, 1], [125, 344, 0, 1]]
hat = [[125, 438, 0, 1], [125, 469, 0, 1], [125, 469, 0, 1], [156, 469, 0, 1], [156, 469, 0, 1], [156, 499, 0, 1], [156, 499, 0, 1], [312, 499, 0, 1], [312, 499, 0, 1], [312, 468, 0, 1], [312, 468, 0, 1], [406, 468, 0, 1], [406, 468, 0, 1], [406, 437, 0, 1], [406, 437, 0, 1], [125, 437, 0, 1]]

print("example matrix")
print_matrix(test)
ident(matrix)
print("\nidentity matrix")
print_matrix(matrix)
print("\nmatrix multi: example and bob")
test = matrix_mult(bob, test)
print_matrix(test)
"""draw_lines( test, screen, color )
display(screen)"""
add_point(test, 250, 250)
print("\nadded (250, 250) to example")
print_matrix(test)
add_edge(test, 140, 140, 0, 220, 220, 0)
print("\nadded edge: (140, 140), (220, 220)")
print_matrix(test)
print("\nDisplaying Mario")
draw_lines(lshoe, screen, brown)
draw_lines(rshoe, screen, brown)
draw_lines(overall1, screen, blue)
draw_lines(overall2, screen, blue)
draw_lines(overall3, screen, blue)
draw_lines(overall4, screen, blue)
draw_lines(buttons, screen, yellow)
draw_lines(shirt1, screen, red)
draw_lines(shirt2, screen, red)
draw_lines(shirt3, screen, red)
draw_lines(hand, screen, skin)
draw_lines(head, screen, skin)
draw_lines(hat, screen, red)
display(screen)
save_ppm(screen, "mario.ppm")
