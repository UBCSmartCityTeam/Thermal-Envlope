from tkinter import *
from tkinter import Label

def assign_values():
        ns_length = float(ns_length_field.get())
        ew_length = float(ew_length_field.get())
        height = float(height_field.get())
        floor_count = float(floor_count_field.get())

        # ratio = (window area)/(wall area)
        north_wall_ratio = float(north_wall_field.get())
        south_wall_ratio = float(south_wall_field.get())
        east_wall_ratio = float(east_field.get())
        west_wall_ratio = float(west_wall_field.get())

        temperature = float(outer_temperature_field.get())
        k_wall = float(thermal_conductivity_wall_field.get())
        k_window = float(thermal_conductivity_window_field.get())
        thickness_wall = float(thickness_wall_field.get())
        thickness_window = float(thickness_window_field.get())

        calculate(ns_length, ew_length, height, floor_count,
                  north_wall_ratio, south_wall_ratio, east_wall_ratio, west_wall_ratio,
                  temperature, k_wall, k_window, thickness_wall, thickness_window,
                  0, 0)


def calculate(ns_length, ew_length, height, floor_count,
              north_wall_ratio, south_wall_ratio, east_wall_ratio, west_wall_ratio,
              temperature, k_wall, k_window, thickness_wall, thickness_window,
              k_wall_retrofit, k_window_retrofit):

    rvalue_ns_wall = thickness_wall / (k_wall * ns_length * height)
    rvalue_ew_wall = thickness_wall / (k_wall * ew_length * height)
    rvalue_roof = thickness_wall / (k_wall * ns_length * ew_length)
    rvalue_north_window = thickness_window / (k_window * ((ns_length * height) * north_wall_ratio))
    rvalue_south_window = thickness_window / (k_window * ((ns_length * height) * south_wall_ratio))
    rvalue_east_window = thickness_window / (k_window * ((ew_length * height) * east_wall_ratio))
    rvalue_west_window = thickness_window / (k_window * ((ew_length * height) * west_wall_ratio))

    rvalue_ns_wall_retrofit = thickness_retrofit / (k_wall_retrofit * ns_length * height)
    rvalue_ew_wall_retrofit = thickness_retrofit / (k_wall_retrofit * ew_length * height)
    rvalue_roof_retrofit = thickness_retrofit / (k_wall_retrofit * ns_length * ew_length)
    rvalue_north_window_retrofit = 1 / ( k_window_retrofit * ((ns_length * height) * north_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_south_window_retrofit = 1 / ( k_window_retrofit * ((ns_length * height) * south_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_east_window_retrofit = 1 / (k_window_retrofit * ((ew_length * height) * east_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_west_window_retrofit = 1 / (k_window_retrofit * ((ew_length * height) * west_wall_ratio))  # WINDOW NEEDS THICKNESS

    room_temperature = 301

    north_wall_heat_loss = ((ns_length * height) * (1 - north_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ns_wall + rvalue_ns_wall_retrofit)
    south_wall_heat_loss = ((ns_length * height) * (1 - south_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ns_wall + rvalue_ns_wall_retrofit)
    east_wall_heat_loss = ((ew_length * height) * (1 - east_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ew_wall + rvalue_ew_wall_retrofit)
    west_wall_heat_loss = ((ew_length * height) * (1 - west_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ew_wall + rvalue_ew_wall_retrofit)
    # assuming the roof has the same properties as the wall
    roof_heat_loss = ((ns_length * ew_length) * (room_temperature - temperature)) / (rvalue_roof + rvalue_roof_retrofit)

    north_window_heat_loss = ((ns_length * height) * north_wall_ratio * (room_temperature - temperature)) / (
            rvalue_north_window + rvalue_north_window_retrofit)
    south_window_heat_loss = ((ns_length * height) * south_wall_ratio * (room_temperature - temperature)) / (
            rvalue_south_window + rvalue_south_window_retrofit)
    east_window_heat_loss = ((ew_length * height) * east_wall_ratio * (room_temperature - temperature)) / (
            rvalue_east_window + rvalue_east_window_retrofit)
    west_window_heat_loss = ((ew_length * height) * west_wall_ratio * (room_temperature - temperature)) / (
            rvalue_west_window + rvalue_west_window_retrofit)

    total_wall_heat_loss = floor_count * (
            north_wall_heat_loss + south_wall_heat_loss + east_wall_heat_loss + roof_heat_loss)
    total_wall_heat_loss = round(total_wall_heat_loss)
    total_window_heat_loss = floor_count * (
            north_window_heat_loss + south_window_heat_loss + east_window_heat_loss + west_window_heat_loss)
    total_window_heat_loss = round(total_window_heat_loss)
    total_heat_loss = total_wall_heat_loss + total_window_heat_loss
    total_heat_loss = round(total_heat_loss)

    percentage_wall_heat_loss = (total_wall_heat_loss / total_heat_loss) * 100
    percentage_wall_heat_loss = round(percentage_wall_heat_loss)
    percentage_window_heat_loss = (total_window_heat_loss / total_heat_loss) * 100
    percentage_window_heat_loss = round(percentage_window_heat_loss)

    results_window()


def results_window():
    # window 2 setup
    window2 = Tk()
    window2.configure(background='light grey')  # set the background colour of GUI window
    window2.title("Results")  # set the title of GUI window
    window2.geometry("600x400")  # set the configuration of GUI window

    current_heat_loss = Label(window2, text="Current Heat-Loss", bg="light grey")
    building_heat_loss = Label(window2, text=f"Heat-loss from building", bg="light grey")
    wall_heat_loss = Label(window2, text=f"Heat-loss from walls", bg="light grey")
    window_heat_loss = Label(window2, text=f"Heat-loss from windows", bg="light grey")

    retrofit_insulation = Label(window2, text="Retro-fit Insulation", bg="light grey")
    rvalue_wall2 = Label(window2, text="R-Value (Wall)", bg="light grey")
    rvalue_window2 = Label(window2, text="R-Value (Window)", bg="light grey")

    configured_building_heat_loss = Label(window2, text=f"Configured building heat-loss", bg="light grey")
    configured_wall_heat_loss = Label(window2, text=f"Configured walls heat-loss", bg="light grey")
    configured_window_heat_loss = Label(window2, text=f"Configured window heat-loss", bg="light grey")

    building_heat_loss_field = Entry(window2)
    wall_heat_loss_field = Entry(window2)
    window_heat_loss_field = Entry(window2)

    rvalue_wall2_field = Entry(window2)
    rvalue_window2_field = Entry(window2)

    building_heat_loss_field.bind("<Return>", building_heat_loss_field.focus_set())
    wall_heat_loss_field.bind("<Return>", wall_heat_loss_field.focus_set())
    window_heat_loss_field.bind("<Return>", window_heat_loss_field.focus_set())

    rvalue_wall2_field.bind("<Return>", rvalue_wall2_field.focus_set())
    rvalue_window2_field.bind("<Return>", rvalue_window2_field.focus_set())

    current_heat_loss.grid(row=1, column=1, ipadx="50")
    building_heat_loss.grid(row=2, column=0, ipadx="50")
    wall_heat_loss.grid(row=3, column=0, ipadx="50")
    window_heat_loss.grid(row=4, column=0, ipadx="50")

    retrofit_insulation.grid(row=5, column=1, ipadx="50")
    rvalue_wall2.grid(row=6, column=0, ipadx="50")
    rvalue_wall2_field.grid(row=6, column=1, ipadx="50")
    rvalue_window2.grid(row=7, column=0, ipadx="50")
    rvalue_window2_field.grid(row=7, column=1, ipadx="50")

    configure = Button(window2, text=" Configure ", fg="Black",
                       bg="grey", command=lambda: [f() for f in [retrofit(window2)]])
    configure.grid(row=8, column=1, ipadx="50")

    configured_building_heat_loss.grid(row=9, column=0, ipadx="50")
    configured_wall_heat_loss.grid(row=10, column=0, ipadx="50")
    configured_window_heat_loss.grid(row=11, column=0, ipadx="50")

    evaluate(window2)


# Function to evaluate heat loss
def evaluate(window2):

    ns_length = 2.0
    ew_length = 3.0
    height = 5.0
    floor_count = 5.0

    # ratio = (window area)/(wall area)
    north_wall_ratio = 0.3
    south_wall_ratio = 0.4
    east_wall_ratio = 0.5
    west_wall_ratio = 0.6

    temperature = 4.0
    k_wall = 2.0
    k_window = 3.0
    thickness_wall = 5
    thickness_window = 5

    rvalue_ns_wall = thickness_wall / (k_wall * ns_length * height)
    rvalue_ew_wall = thickness_wall / (k_wall * ew_length * height)
    rvalue_roof = thickness_wall / (k_wall * ns_length * ew_length)
    rvalue_north_window = thickness_window / (k_window * ((ns_length * height) * north_wall_ratio))
    rvalue_south_window = thickness_window / (k_window * ((ns_length * height) * south_wall_ratio))
    rvalue_east_window = thickness_window / (k_window * ((ew_length * height) * east_wall_ratio))
    rvalue_west_window = thickness_window / (k_window * ((ew_length * height) * west_wall_ratio))

    room_temperature = 301

    north_wall_heat_loss = ((ns_length * height) * (1 - north_wall_ratio) * (
            room_temperature - temperature)) / rvalue_ns_wall
    south_wall_heat_loss = ((ns_length * height) * (1 - south_wall_ratio) * (
            room_temperature - temperature)) / rvalue_ns_wall
    east_wall_heat_loss = ((ew_length * height) * (1 - east_wall_ratio) * (
            room_temperature - temperature)) / rvalue_ew_wall
    west_wall_heat_loss = ((ew_length * height) * (1 - west_wall_ratio) * (
            room_temperature - temperature)) / rvalue_ew_wall
    # assuming the roof has the same properties as the wall
    roof_heat_loss = ((ns_length * ew_length) * (room_temperature - temperature)) / rvalue_roof

    north_window_heat_loss = ((ns_length * height) * north_wall_ratio * (
            room_temperature - temperature)) / rvalue_north_window
    south_window_heat_loss = ((ns_length * height) * south_wall_ratio * (
            room_temperature - temperature)) / rvalue_south_window
    east_window_heat_loss = ((ew_length * height) * east_wall_ratio * (
            room_temperature - temperature)) / rvalue_east_window
    west_window_heat_loss = ((ew_length * height) * west_wall_ratio * (
            room_temperature - temperature)) / rvalue_west_window

    total_wall_heat_loss = floor_count * (
            north_wall_heat_loss + south_wall_heat_loss + east_wall_heat_loss + west_wall_heat_loss + roof_heat_loss)
    total_wall_heat_loss = round(total_wall_heat_loss)
    total_window_heat_loss = floor_count * (
            north_window_heat_loss + south_window_heat_loss + east_window_heat_loss + west_window_heat_loss)
    total_window_heat_loss = round(total_window_heat_loss)
    total_heat_loss: int = total_wall_heat_loss + total_window_heat_loss
    total_heat_loss = round(total_heat_loss)

    percentage_wall_heat_loss = (total_wall_heat_loss / total_heat_loss) * 100
    percentage_wall_heat_loss = round(percentage_wall_heat_loss)
    percentage_window_heat_loss = (total_window_heat_loss / total_heat_loss) * 100
    percentage_window_heat_loss = round(percentage_window_heat_loss)

    total_wall_heat_loss_label = Label(window2, text=f"{total_wall_heat_loss}", bg="light grey")
    total_window_heat_loss_label: Label = Label(window2, text=f"{total_window_heat_loss}", bg="light grey")
    total_heat_loss_label = Label(window2, text=f"{total_heat_loss}", bg="light grey")

    total_heat_loss_label.grid(row=2, column=1, ipadx="50")
    total_wall_heat_loss_label.grid(row=3, column=1, ipadx="50")
    total_window_heat_loss_label.grid(row=4, column=1, ipadx="50")


def change_thickness(value):
    global thickness_retrofit
    thickness_retrofit = value
    return


def retrofit(window2):
    # USE CORRECT THICKNESS
    level_1 = Button(window2, text="1 cm", fg="Black",
                     bg="grey", command=lambda *args: change_thickness(1))
    level_1.grid(row=9, column=2, ipadx="10")

    # USE CORRECT THICKNESS
    level_2 = Button(window2, text="2 cm", fg="Black",
                     bg="grey", command=lambda *args: change_thickness(2))
    level_2.grid(row=10, column=2, ipadx="10")

    # USE CORRECT THICKNESS
    level_3 = Button(window2, text="3 cm", fg="Black",
                     bg="grey", command=lambda *args: change_thickness(3))
    level_3.grid(row=11, column=2, ipadx="10")

    ns_length = 3.0
    ew_length = 4.0
    height = 4.0
    floor_count = 7.0

    # ratio = (window area)/(wall area)
    north_wall_ratio = 0.1
    south_wall_ratio = 0.6
    east_wall_ratio = 0.5
    west_wall_ratio = 0.5

    temperature = 4.0
    k_wall = 2.0
    k_window = 3.0
    thickness_wall = 5
    thickness_window = 5

    k_wall_retrofit = 3
    k_window_retrofit = 2

    rvalue_ns_wall = thickness_wall / (k_wall * ns_length * height)
    rvalue_ew_wall = thickness_wall / (k_wall * ew_length * height)
    rvalue_roof = thickness_wall / (k_wall * ns_length * ew_length)
    rvalue_north_window = thickness_window / (k_window * ((ns_length * height) * north_wall_ratio))
    rvalue_south_window = thickness_window / (k_window * ((ns_length * height) * south_wall_ratio))
    rvalue_east_window = thickness_window / (k_window * ((ew_length * height) * east_wall_ratio))
    rvalue_west_window = thickness_window / (k_window * ((ew_length * height) * west_wall_ratio))

    rvalue_ns_wall_retrofit = thickness_retrofit / (k_wall_retrofit * ns_length * height)
    rvalue_ew_wall_retrofit = thickness_retrofit / (k_wall_retrofit * ew_length * height)
    rvalue_roof_retrofit = thickness_retrofit / (k_wall_retrofit * ns_length * ew_length)
    rvalue_north_window_retrofit = 1 / (k_window_retrofit * ((ns_length * height) * north_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_south_window_retrofit = 1 / (k_window_retrofit * ((ns_length * height) * south_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_east_window_retrofit = 1 / (k_window_retrofit * ((ew_length * height) * east_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_west_window_retrofit = 1 / (k_window_retrofit * ((ew_length * height) * west_wall_ratio))  # WINDOW NEEDS THICKNESS

    room_temperature = 301

    north_wall_heat_loss = ((ns_length * height) * (1 - north_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ns_wall + rvalue_ns_wall_retrofit)
    south_wall_heat_loss = ((ns_length * height) * (1 - south_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ns_wall + rvalue_ns_wall_retrofit)
    east_wall_heat_loss = ((ew_length * height) * (1 - east_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ew_wall + rvalue_ew_wall_retrofit)
    west_wall_heat_loss = ((ew_length * height) * (1 - west_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ew_wall + rvalue_ew_wall_retrofit)
    # assuming the roof has the same properties as the wall
    roof_heat_loss = ((ns_length * ew_length) * (room_temperature - temperature)) / (rvalue_roof + rvalue_roof_retrofit)

    north_window_heat_loss = ((ns_length * height) * north_wall_ratio * (room_temperature - temperature)) / (
            rvalue_north_window + rvalue_north_window_retrofit)
    south_window_heat_loss = ((ns_length * height) * south_wall_ratio * (room_temperature - temperature)) / (
            rvalue_south_window + rvalue_south_window_retrofit)
    east_window_heat_loss = ((ew_length * height) * east_wall_ratio * (room_temperature - temperature)) / (
            rvalue_east_window + rvalue_east_window_retrofit)
    west_window_heat_loss = ((ew_length * height) * west_wall_ratio * (room_temperature - temperature)) / (
            rvalue_west_window + rvalue_west_window_retrofit)

    total_wall_heat_loss = floor_count * (
            north_wall_heat_loss + south_wall_heat_loss + east_wall_heat_loss + roof_heat_loss)
    total_wall_heat_loss = round(total_wall_heat_loss)
    total_window_heat_loss = floor_count * (
            north_window_heat_loss + south_window_heat_loss + east_window_heat_loss + west_window_heat_loss)
    total_window_heat_loss = round(total_window_heat_loss)
    total_heat_loss = total_wall_heat_loss + total_window_heat_loss
    total_heat_loss = round(total_heat_loss)

    percentage_wall_heat_loss = (total_wall_heat_loss / total_heat_loss) * 100
    percentage_wall_heat_loss = round(percentage_wall_heat_loss)
    percentage_window_heat_loss = (total_window_heat_loss / total_heat_loss) * 100
    percentage_window_heat_loss = round(percentage_window_heat_loss)

    retrofit_wall_heat_loss_label = Label(window2, text=f"{total_wall_heat_loss}", bg="light grey")
    retrofit_window_heat_loss_label: Label = Label(window2, text=f"{total_window_heat_loss}", bg="light grey")
    retrofit_heat_loss_label = Label(window2, text=f"{total_heat_loss}", bg="light grey")

    retrofit_heat_loss_label.grid(row=9, column=1, ipadx="50")
    retrofit_wall_heat_loss_label.grid(row=10, column=1, ipadx="50")
    retrofit_window_heat_loss_label.grid(row=11, column=1, ipadx="50")

    # savings(total_heat_loss, window2)


'''
# Conversion is not correct. Needs work.
def savings(total_heat_loss, window2):
    yearly_loss = total_heat_loss * 3600
    KWh_cost = 0.0829
    total_cost = yearly_loss * KWh_cost

    total_cost_label = Label(window2, text=f"{total_cost}", bg="light grey")
    total_cost_label.grid(row=12, column=1, ipadx="50")
'''

if __name__ == "__main__":
    # window 1 setup
    window1 = Tk()
    window1.configure(background='light grey')  # set the background colour of GUI window
    window1.title("Inputs")  # set the title of GUI window
    window1.geometry("600x400")  # set the configuration of GUI window

    # Labels
    heading = Label(window1, text="Building Information", bg="light grey", font='Helvetica 9 bold')
    floors = Label(window1, text="Floors", bg="light grey")
    ns_length = Label(window1, text="North/South Length", bg="light grey")
    ew_length = Label(window1, text="East/West Length", bg="light grey")
    height = Label(window1, text="Height", bg="light grey")
    floor_count = Label(window1, text="Floor Count", bg="light grey")

    wall_ratio = Label(window1, text="Window/Wall ratio", bg="light grey")
    north_wall = Label(window1, text="North wall", bg="light grey")
    south_wall = Label(window1, text="South wall", bg="light grey")
    east = Label(window1, text="East wall", bg="light grey")
    west_wall = Label(window1, text="West wall", bg="light grey")

    insulation = Label(window1, text="Insulation", bg="light grey")
    outer_temperature = Label(window1, text="Outer temperature", bg="light grey")
    thermal_conductivity_wall = Label(window1, text="Thermal Conductivity (Wall)", bg="light grey")
    thermal_conductivity_window = Label(window1, text="Thermal Conductivity (Window)", bg="light grey")
    thickness_wall = Label(window1, text="Wall Thickness", bg="light grey")
    thickness_window = Label(window1, text="Window Thickness", bg="light grey")

    # create a text entry box
    # for typing the information
    ns_length_field = Entry(window1)
    ew_length_field = Entry(window1)
    height_field = Entry(window1)
    floor_count_field = Entry(window1)

    north_wall_field = Entry(window1)
    south_wall_field = Entry(window1)
    east_field = Entry(window1)
    west_wall_field = Entry(window1)

    outer_temperature_field = Entry(window1)
    thermal_conductivity_wall_field = Entry(window1)
    thermal_conductivity_window_field = Entry(window1)
    thickness_wall_field = Entry(window1)
    thickness_window_field = Entry(window1)

    # bind method of widget is used for
    # the binding the function with the events
    # whenever the enter key is pressed
    # then call the focus1 function
    ns_length_field.bind("<Return>", ns_length_field.focus_set())
    ew_length_field.bind("<Return>", ew_length_field.focus_set())
    height_field.bind("<Return>", height_field.focus_set())
    floor_count_field.bind("<Return>", floor_count_field.focus_set())

    north_wall_field.bind("<Return>", north_wall_field.focus_set())
    south_wall_field.bind("<Return>", south_wall_field.focus_set())
    east_field.bind("<Return>", east_field.focus_set())
    west_wall_field.bind("<Return>", west_wall_field.focus_set())

    outer_temperature_field.bind("<Return>", outer_temperature_field.focus_set())
    thermal_conductivity_wall_field.bind("<Return>", thermal_conductivity_wall_field.focus_set())
    thermal_conductivity_window_field.bind("<Return>", thermal_conductivity_window_field.focus_set())
    thickness_wall_field.bind("<Return>", thickness_wall_field.focus_set())
    thickness_window_field.bind("<Return>", thickness_window_field.focus_set())

    # create Buttons and place into the window1 window
    # submit opens the next window and evaluates the results
    submit = Button(window1, text=" Submit ", fg="Black",
                    bg="grey", command=lambda: [f() for f in [assign_values()]])

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    heading.grid(row=0, column=0, ipadx="50")
    floors.grid(row=1, column=1, ipadx="50")
    ns_length.grid(row=2, column=0, ipadx="50")
    ns_length_field.grid(row=2, column=1, ipadx="50")
    ew_length.grid(row=3, column=0, ipadx="50")
    ew_length_field.grid(row=3, column=1, ipadx="50")
    height.grid(row=4, column=0, ipadx="50")
    height_field.grid(row=4, column=1, ipadx="50")
    floor_count.grid(row=5, column=0, ipadx="50")
    floor_count_field.grid(row=5, column=1, ipadx="50")

    wall_ratio.grid(row=6, column=1, ipadx="50")
    north_wall.grid(row=7, column=0, ipadx="50")
    north_wall_field.grid(row=7, column=1, ipadx="50")
    south_wall.grid(row=8, column=0, ipadx="50")
    south_wall_field.grid(row=8, column=1, ipadx="50")
    east.grid(row=9, column=0, ipadx="50")
    east_field.grid(row=9, column=1, ipadx="50")
    west_wall.grid(row=10, column=0, ipadx="50")
    west_wall_field.grid(row=10, column=1, ipadx="50")

    insulation.grid(row=11, column=1, ipadx="50")
    outer_temperature.grid(row=12, column=0, ipadx="50")
    outer_temperature_field.grid(row=12, column=1, ipadx="50")
    thermal_conductivity_wall.grid(row=13, column=0, ipadx="50")
    thermal_conductivity_wall_field.grid(row=13, column=1, ipadx="50")
    thermal_conductivity_window.grid(row=14, column=0, ipadx="50")
    thermal_conductivity_window_field.grid(row=14, column=1, ipadx="50")
    thickness_wall.grid(row=15, column=0, ipadx="50")
    thickness_wall_field.grid(row=15, column=1, ipadx="50")
    thickness_window.grid(row=16, column=0, ipadx="50")
    thickness_window_field.grid(row=16, column=1, ipadx="50")

    submit.grid(row=17, column=1, ipadx="50")

    # start the GUI
    window1.mainloop()
