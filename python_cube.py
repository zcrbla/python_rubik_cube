#Variables
red = 0
orange = 1
yellow = 2
green = 3
blue = 4
white = 5
red_face_current =    [0,0,0,0, 0 ,0,0,0,0]
orange_face_current = [1,1,1,1, 1 ,1,1,1,1]
yellow_face_current = [2,2,2,2, 2 ,2,2,2,2]
green_face_current =  [3,3,3,3, 3 ,3,3,3,3]
blue_face_current =   [4,4,4,4, 4 ,4,4,4,4]
white_face_current =  [5,5,5,5, 5 ,5,5,5,5]
solved = False
running = True
version = "1.0.0"
#Classes
class Cube():
    def u():
        print(f'{rotation.upper()} turn done.')
        print(white_face_current[:2])
    def d():
        print(f'{rotation.upper()} turn done.')
        
    def r():
        print(f'{rotation.upper()} turn done.')
        
    def l():
        print(f'{rotation.upper()} turn done.')
        
    def f():
        print(f'{rotation.upper()} turn done.')
        
    def b():
        print(f'{rotation.upper()} turn done.')
        
    def _u():
        print(f'{rotation.upper()} turn done.')
        
    def _d():
        print(f'{rotation.upper()} turn done.')
        
    def _r():
        print(f'{rotation.upper()} turn done.')
        
    def _l():
        print(f'{rotation.upper()} turn done.')
        
    def _f():
        print(f'{rotation.upper()} turn done.')
        
    def _b():
        print(f'{rotation.upper()} turn done.')
        
    def print_state():
        print('placeholder')
#Start code, shown only once
print(f"Welcome to zcrbla's rubik's cube simulator v{version}")
first_run = True
while running:
    #Proccess
    if red_face_current != [0,0,0,0,0,0,0,0,0] and orange_face_current != [1,1,1,1,1,1,1,1,1] and yellow_face_current != [2,2,2,2,2,2,2,2,2] and green_face_current != [3,3,3,3,3,3,3,3,3] and blue_face_current != [4,4,4,4,4,4,4,4,4] and white_face_current != [5,5,5,5,5,5,5,5,5]:
        solved = False

    if red_face_current == [0,0,0,0,0,0,0,0,0] and orange_face_current == [1,1,1,1,1,1,1,1,1] and yellow_face_current == [2,2,2,2,2,2,2,2,2] and green_face_current == [3,3,3,3,3,3,3,3,3] and blue_face_current == [4,4,4,4,4,4,4,4,4] and white_face_current == [5,5,5,5,5,5,5,5,5]:
        if first_run == True:
            first_run = False
        elif first_run == False:
            solved = True
    if solved == True:
        print("Congratulations! You solved the cube. Would you like to continue?")
        while True:
            continue_input = input()
            continue_input = continue_input.lower()
            continue_input = continue_input.replace(" ", "")
            if continue_input.startswith('y'):
                print("Alright, get back to solving it, then!")
                break
            elif continue_input.startswith('n'):
                print("Okay, enjoy the rest of your day!")
                quit("User solved the cube and chose to leave.")
            else:
                print("Sorry, please try again.")
                print("Would you like to continue?")
    print("How would you like to turn the cube?")
    rotation = input()
    rotation = rotation.lower()
    rotation = rotation.replace(" ", "")
    #Update
    if 'u' == rotation:
        Cube.u()
    elif 'd' == rotation:
        Cube.d()
    elif 'r' == rotation:
        Cube.r()
    elif 'l' == rotation:
        Cube.l()
    elif 'f' == rotation:
        Cube.f()
    elif 'b' == rotation:
        Cube.b()
    elif 'u\'' == rotation:
        Cube._u()
    elif 'd\'' == rotation:
        Cube._d()
    elif 'r\'' == rotation:
        Cube._r()
    elif 'l\'' == rotation:
        Cube._l()
    elif 'f\'' == rotation:
        Cube._f()
    elif 'b\'' == rotation:
        Cube._b()
    elif 'u2' == rotation:
        Cube.u()
        Cube.u()
    elif 'd2' == rotation:
        Cube.d()
        Cube.d()
    elif 'r2' == rotation:
        Cube.r()
        Cube.r()
    elif 'l2' == rotation:
        Cube.l()
        Cube.l()
    elif 'f2' == rotation:
        Cube.f()
        Cube.f()
    elif 'b2' == rotation:
        Cube.b()
        Cube.b()
    elif 'u\'2' == rotation:
        Cube._u()
        Cube._u()
    elif 'd\'2' == rotation:
        Cube._d()
        Cube._d()
    elif 'r\'2' == rotation:
        Cube._r()
        Cube._r()
    elif 'l\'2' == rotation:
        Cube._l()
        Cube._l()
    elif 'f\'2' == rotation:
        Cube._f()
        Cube._f()
    elif 'b\'2' == rotation:
        Cube._b()
        Cube._b()
    else:
        print("Input not recognized.")
        print("Sorry, please try again.")
    #Display
    Cube.print_state()
