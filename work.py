from djitellopy import Tello

tello = Tello()

tello.connect()
battery = tello.get_battery()
tello.takeoff()
tello.move_up(20)
height = tello.get_height()
for i in range(0,8):
    tello.move_forward(100)
    tello.rotate_counter_clockwise(90)
flight_time = tello.get_flight_time()
tello.land()

print("Power Level:", battery,"%")
print("height:" , height)