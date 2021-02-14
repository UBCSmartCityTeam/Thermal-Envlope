from tkinter import *
from tkinter import Label

# Contains all th information about user parameters
# Can be used for running tests instead of inputing values

input_dictionary = {"ns_length": 7, "ew_length": 5, "height": 2, "floor_count": 4, "north_wall_ratio": 0.2,
                    "south_wall_ratio": 0.3, "east_wall_ratio": .3, "west_wall_ratio": 0.4, "temperature": 75,
                    "k_wall": 5, "k_window": 7, "thickness_wall": 1, "thickness_window": 0.2, "k_wall_retrofit": 1,
                    "k_window_retrofit": 1, "thickness_wall_retrofit": 1}



# Contains all the information about retrofit options
# Updates overtime as input-dependent values are calculated
retrofit_dictionary = {  # Wall Options

    # K-value = thickness / RSI- value
    # Value obtained from: https://www.iko.com/comm/blog/insulation-thickness-r-value-chart/,
    # for 1-inch thickness
    # cost per meter-square
    "foam_board": {"k_wall_retrofit": 0.24, "thickness_wall_retrofit": 0.0254, "material_cost": 22,
                   "heat_loss_savings": 0, "implementation": 0, "cost_savings": 0},

    # Value obtained from: https://en.wikipedia.org/wiki/R-value_(insulation), for 1-inch thickness
    # cost per meter-square
    "Fiberglass_Loose_Fill": {"k_wall_retrofit": 0.039, "thickness_wall_retrofit": 0.0254, "material_cost": 16.2,
                              "heat_loss_savings": 0, "implementation": 0, "cost_savings": 0},

    # Value obtained from: https://en.wikipedia.org/wiki/R-value_(insulation), for 1-inch thickness,
    # cost per meter-square: https://www.remodelingexpense.com/costs/cost-of-spray-foam-insulation/
    "Injection_Foam": {"k_wall_retrofit": 0.026, "thickness_wall_retrofit": 0.0254, "material_cost": 16.1,
                       "heat_loss_savings": 0, "implementation": 0, "cost_savings": 0},

    # For adding additional options replicate the code above for e.g.
    # "Option": {"k_wall_retrofit": XXX, "thickness_wall_retrofit": XXX, "material_cost": XXX,
    # "heat_loss_savings": XXX, "implementation": XXX, "cost_savings": XXX},

    # Window Options
    # Value obtained from: https://en.wikipedia.org/wiki/R-value_(insulation), for 3/32-inch thickness
    # Value obtained from https://homeguide.com/costs/window-glass-replacement-cost, cost per meter-square
    "Glass": {"k_window_retrofit": 0.0132, "thickness_window_retrofit": 0.00238, "material_cost": 32.3,
              "heat_loss_savings": 0, "implementation": 0, "cost_savings": 0},

    # Value obtained from: https://en.wikipedia.org/wiki/R-value_(insulation),
    # for 20mm thickness: http://blog.thermawood.com.au/how-thick-is-double-glazed-glass#:~:text=How%20thick%20are%20the%20two,glass%20pane%20is%204mm%20thick.
    # Value obtained from https://homeguide.com/costs/window-glass-replacement-cost, cost per meter-square
    "Argon_Double_Pane": {"k_window_retrofit": 0.003, "thickness_window_retrofit": 0.02, "material_cost": 129,
                          "heat_loss_savings": 0, "implementation": 0, "cost_savings": 0},
    # Value obtained from: https://www.lindusconstruction.com/single-double-triple-pane/#:~:text=Double%20pane%20windows%20have%20all,the%20resistance%20to%20heat%20flow.
    # for 36mm thickness: https://www.johnknightglass.co.uk/about-us/blog/triple-glazing-is-it-really-worth-it/#:~:text=Triple%20glazing%20is%20generally%20supplied,than%20a%20double%20glazed%20unit.
    # Cost is an assumption as could not find material cost, cost per meter-square
    "Triple_Pane": {"k_window_retrofit": 0.002, "thickness_window_retrofit": 0.0036, "material_cost": 180,
                 "heat_loss_savings": 0, "implementation": 0, "cost_savings": 0}

    # For adding additional options replicate the code above for e.g.
    # "Option": {"k_wall_retrofit": XXX, "thickness_wall_retrofit": XXX, "material_cost": XXX,
    # "heat_loss_savings": XXX, "implementation": XXX, "cost_savings": XXX},
}


# Complies user input into a dictionary
# The dictionary is then passed along to be used in the calculations
def assign_values():
    '''
    input_dictionary["ns_length"] = float(ns_length_field.get())
    input_dictionary["ew_length"] = float(ew_length_field.get())
    input_dictionary["height"] = float(height_field.get())
    input_dictionary["floor_count"] = float(floor_count_field.get())

    # ratio = (window area)/(wall area)
    input_dictionary["north_wall_ratio"] = float(north_wall_field.get())
    input_dictionary["south_wall_ratio"] = float(south_wall_field.get())
    input_dictionary["east_wall_ratio"] = float(east_field.get())
    input_dictionary["west_wall_ratio"] = float(west_wall_field.get())

    input_dictionary["temperature"] = float(outer_temperature_field.get())
    input_dictionary["k_wall"] = float(thermal_conductivity_wall_field.get())
    input_dictionary["k_window"] = float(thermal_conductivity_window_field.get())
    input_dictionary["thickness_wall"] = float(thickness_wall_field.get())
    input_dictionary["thickness_window"] = float(thickness_window_field.get())
    '''
    calculate(input_dictionary)


# Performs calculations for current heat loss
def calculate(input_dictionary):
    # Extract values from input dictionary
    ns_length = input_dictionary["ns_length"]
    ew_length = input_dictionary["ew_length"]
    height = input_dictionary["height"]
    floor_count = input_dictionary["floor_count"]

    # ratio = (window area)/(wall area)
    north_wall_ratio = input_dictionary["north_wall_ratio"]
    south_wall_ratio = input_dictionary["south_wall_ratio"]
    east_wall_ratio = input_dictionary["east_wall_ratio"]
    west_wall_ratio = input_dictionary["west_wall_ratio"]

    temperature = input_dictionary["temperature"]
    k_wall = input_dictionary["k_wall"]
    k_window = input_dictionary["k_window"]
    thickness_wall = input_dictionary["thickness_wall"]
    thickness_window = input_dictionary["thickness_window"]

    # r-value = thickness / (k-value * length * height)
    rvalue_ns_wall = thickness_wall / (k_wall * ns_length * height)
    rvalue_ew_wall = thickness_wall / (k_wall * ew_length * height)
    rvalue_roof = thickness_wall / (k_wall * ns_length * ew_length)
    rvalue_north_window = thickness_window / (k_window * ((ns_length * height) * north_wall_ratio))
    rvalue_south_window = thickness_window / (k_window * ((ns_length * height) * south_wall_ratio))
    rvalue_east_window = thickness_window / (k_window * ((ew_length * height) * east_wall_ratio))
    rvalue_west_window = thickness_window / (k_window * ((ew_length * height) * west_wall_ratio))

    # Assumption based on normal residence parameters (Kelvin)
    room_temperature = 301

    # Heat-loss from walls
    north_wall_heat_loss = ((ns_length * height) * (1 - north_wall_ratio) * (room_temperature - temperature)) / (
        rvalue_ns_wall)
    south_wall_heat_loss = ((ns_length * height) * (1 - south_wall_ratio) * (room_temperature - temperature)) / (
        rvalue_ns_wall)
    east_wall_heat_loss = ((ew_length * height) * (1 - east_wall_ratio) * (room_temperature - temperature)) / (
        rvalue_ew_wall)
    west_wall_heat_loss = ((ew_length * height) * (1 - west_wall_ratio) * (room_temperature - temperature)) / (
        rvalue_ew_wall)
    # assuming the roof has the same properties as the wall
    roof_heat_loss = ((ns_length * ew_length) * (room_temperature - temperature)) / (rvalue_roof)

    # Heat-loss from windows
    north_window_heat_loss = ((ns_length * height) * north_wall_ratio * (room_temperature - temperature)) / (
        rvalue_north_window)
    south_window_heat_loss = ((ns_length * height) * south_wall_ratio * (room_temperature - temperature)) / (
        rvalue_south_window)
    east_window_heat_loss = ((ew_length * height) * east_wall_ratio * (room_temperature - temperature)) / (
        rvalue_east_window)
    west_window_heat_loss = ((ew_length * height) * west_wall_ratio * (room_temperature - temperature)) / (
        rvalue_west_window)

    # Total Heat-loss = (walls + windows) * number of floors
    total_wall_heat_loss = floor_count * (
            north_wall_heat_loss + south_wall_heat_loss + east_wall_heat_loss + west_wall_heat_loss + roof_heat_loss)
    total_wall_heat_loss = round(total_wall_heat_loss) / 1000  # Round off and convert to KW
    total_window_heat_loss = floor_count * (
            north_window_heat_loss + south_window_heat_loss + east_window_heat_loss + west_window_heat_loss)
    total_window_heat_loss = round(total_window_heat_loss) / 1000  # Round off and convert to KW
    total_heat_loss = total_wall_heat_loss + total_window_heat_loss
    total_heat_loss = round(total_heat_loss)

    # Results are displayed on the 2nd window
    results_window(input_dictionary, total_wall_heat_loss, total_window_heat_loss, total_heat_loss)


# 2nd window for showing current heat loss
def results_window(inputs, total_wall_heat_loss, total_window_heat_loss, total_heat_loss):
    # window 2 setup
    window2 = Tk()
    window2.configure(background='light grey')  # set the background colour of GUI window
    window2.title("Results")  # set the title of GUI window
    window2.geometry("900x400")  # set the configuration of GUI window

    # Labels for the window
    current_heat_loss = Label(window2, text="Current Heat-Loss (KW)", bg="light grey")
    building_heat_loss = Label(window2, text=f"Heat-loss from building", bg="light grey")
    total_heat_loss_label = Label(window2, text=f"{total_heat_loss}", bg="light grey")
    wall_heat_loss = Label(window2, text=f"Heat-loss from walls", bg="light grey")
    total_wall_heat_loss_label = Label(window2, text=f"{total_wall_heat_loss}", bg="light grey")
    window_heat_loss = Label(window2, text=f"Heat-loss from windows", bg="light grey")
    total_window_heat_loss_label: Label = Label(window2, text=f"{total_window_heat_loss}", bg="light grey")

    wall_retrofits = Label(window2, text=f"After Wall Insulation", bg="light grey", font='Helvetica 9 bold')
    configured_building_heat_loss = Label(window2, text=f"Configured building heat-loss (KW)", bg="light grey")
    implementation_cost = Label(window2, text=f"Implementation_cost", bg="light grey")
    yearly_savings = Label(window2, text=f"yearly_savings", bg="light grey")

    wall_types = Label(window2, text=f"Wall Types", bg="light grey")
    foam_board = Label(window2, text=f"Foam Board", bg="light grey")
    wood = Label(window2, text=f"Fiberglass_Loose_Fill", bg="light grey")
    foam = Label(window2, text=f"Injection_Foam", bg="light grey")

    window_retrofits = Label(window2, text=f"After Window Insulation", bg="light grey", font='Helvetica 9 bold')
    glass = Label(window2, text=f"Glass", bg="light grey")
    argon_double_pane = Label(window2, text=f"Argon Double Pane", bg="light grey")
    triple_pane = Label(window2, text=f"Triple Pane", bg="light grey")

    # create a text entry box
    # for displaying results for current heat loss
    building_heat_loss_field = Entry(window2)
    wall_heat_loss_field = Entry(window2)
    window_heat_loss_field = Entry(window2)

    # bind method of widget is used for
    # the binding the function with the events
    # whenever the enter key is pressed
    # then call the focus1 function
    # must be passed for the code to work
    building_heat_loss_field.bind("<Return>", building_heat_loss_field.focus_set())
    wall_heat_loss_field.bind("<Return>", wall_heat_loss_field.focus_set())
    window_heat_loss_field.bind("<Return>", window_heat_loss_field.focus_set())

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    current_heat_loss.grid(row=1, column=1, ipadx="50")
    building_heat_loss.grid(row=2, column=0, ipadx="50")
    total_heat_loss_label.grid(row=2, column=1, ipadx="50")
    wall_heat_loss.grid(row=3, column=0, ipadx="50")
    total_wall_heat_loss_label.grid(row=3, column=1, ipadx="50")
    window_heat_loss.grid(row=4, column=0, ipadx="50")
    total_window_heat_loss_label.grid(row=4, column=1, ipadx="50")

    wall_retrofits.grid(row=5, column=0, ipadx="50")
    configured_building_heat_loss.grid(row=6, column=1, ipadx="50")
    implementation_cost.grid(row=6, column=2, ipadx="50")
    yearly_savings.grid(row=6, column=3, ipadx="50")

    wall_types.grid(row=6, column=0, ipadx="50")
    foam_board.grid(row=7, column=0, ipadx="50")
    wood.grid(row=8, column=0, ipadx="50")
    foam.grid(row=9, column=0, ipadx="50")

    window_retrofits.grid(row=10, column=0, ipadx="50")
    glass.grid(row=11, column=0, ipadx="50")
    argon_double_pane.grid(row=12, column=0, ipadx="50")
    triple_pane.grid(row=13, column=0, ipadx="50")

    retrofit(window2, input_dictionary)


# Displays retrofit heat loss table on 2nd window
# Uses calculate_retrofit function to calculate heat loss savings
# Uses cost_analysis function to calculate material cost and energy savings
def retrofit(window2, input_dictionary):
    # foam_board
    input_dictionary["k_wall_retrofit"] = retrofit_dictionary["foam_board"]["k_wall_retrofit"]
    input_dictionary["thickness_wall_retrofit"] = retrofit_dictionary["foam_board"]["thickness_wall_retrofit"]
    retrofit_dictionary["foam_board"]["heat_loss_savings"] = calculate_retrofit(input_dictionary)
    input_dictionary["k_wall_retrofit"] = 1  # resets value
    input_dictionary["thickness_wall_retrofit"] = 1  # resets value
    retrofit_dictionary["foam_board"]["implementation"] = cost_analysis(input_dictionary, "foam_board")
    cost_per_kwh = 0.0935  # 9.35 cents
    retrofit_dictionary["foam_board"]["cost_savings"] = retrofit_dictionary["foam_board"][
                                                            "heat_loss_savings"] * cost_per_kwh

    heat_loss_savings_foam_board_label = Label(window2,
                                               text=f'{retrofit_dictionary["foam_board"]["heat_loss_savings"]}',
                                               bg="light grey")
    implementation_foam_board_label: Label = Label(window2,
                                                   text=f'{retrofit_dictionary["foam_board"]["implementation"]}',
                                                   bg="light grey")
    cost_savings_foam_board_label = Label(window2, text=f'{retrofit_dictionary["foam_board"]["cost_savings"]}',
                                          bg="light grey")

    heat_loss_savings_foam_board_label.grid(row=7, column=1, ipadx="50")
    implementation_foam_board_label.grid(row=7, column=2, ipadx="50")
    cost_savings_foam_board_label.grid(row=7, column=3, ipadx="50")

    # Fiberglass_Loose_Fill
    input_dictionary["k_wall_retrofit"] = retrofit_dictionary["Fiberglass_Loose_Fill"]["k_wall_retrofit"]
    input_dictionary["thickness_wall_retrofit"] = retrofit_dictionary["Fiberglass_Loose_Fill"][
        "thickness_wall_retrofit"]
    retrofit_dictionary["Fiberglass_Loose_Fill"]["heat_loss_savings"] = calculate_retrofit(input_dictionary)
    input_dictionary["k_wall_retrofit"] = 1  # resets value
    input_dictionary["thickness_wall_retrofit"] = 1  # resets value
    retrofit_dictionary["Fiberglass_Loose_Fill"]["implementation"] = cost_analysis(input_dictionary,
                                                                                   "Fiberglass_Loose_Fill")
    cost_per_kwh = 0.0935  # 9.35 cents
    retrofit_dictionary["Fiberglass_Loose_Fill"]["cost_savings"] = retrofit_dictionary["Fiberglass_Loose_Fill"][
                                                                       "heat_loss_savings"] * cost_per_kwh

    heat_loss_savings_foam_board_label = Label(window2,
                                               text=f'{retrofit_dictionary["Fiberglass_Loose_Fill"]["heat_loss_savings"]}',
                                               bg="light grey")
    implementation_foam_board_label: Label = Label(window2,
                                                   text=f'{retrofit_dictionary["Fiberglass_Loose_Fill"]["implementation"]}',
                                                   bg="light grey")
    cost_savings_foam_board_label = Label(window2,
                                          text=f'{retrofit_dictionary["Fiberglass_Loose_Fill"]["cost_savings"]}',
                                          bg="light grey")

    heat_loss_savings_foam_board_label.grid(row=8, column=1, ipadx="50")
    implementation_foam_board_label.grid(row=8, column=2, ipadx="50")
    cost_savings_foam_board_label.grid(row=8, column=3, ipadx="50")

    # Injection_Foam
    input_dictionary["k_wall_retrofit"] = retrofit_dictionary["Injection_Foam"]["k_wall_retrofit"]
    input_dictionary["thickness_wall_retrofit"] = retrofit_dictionary["Injection_Foam"]["thickness_wall_retrofit"]
    retrofit_dictionary["Injection_Foam"]["heat_loss_savings"] = calculate_retrofit(input_dictionary)
    input_dictionary["k_wall_retrofit"] = 1  # resets value
    input_dictionary["thickness_wall_retrofit"] = 1  # resets value
    retrofit_dictionary["Injection_Foam"]["implementation"] = cost_analysis(input_dictionary, "Injection_Foam")
    cost_per_kwh = 0.0935  # 9.35 cents
    retrofit_dictionary["Injection_Foam"]["cost_savings"] = retrofit_dictionary["Injection_Foam"][
                                                                "heat_loss_savings"] * cost_per_kwh

    heat_loss_savings_foam_board_label = Label(window2,
                                               text=f'{retrofit_dictionary["Injection_Foam"]["heat_loss_savings"]}',
                                               bg="light grey")
    implementation_foam_board_label: Label = Label(window2,
                                                   text=f'{retrofit_dictionary["Injection_Foam"]["implementation"]}',
                                                   bg="light grey")
    cost_savings_foam_board_label = Label(window2, text=f'{retrofit_dictionary["Injection_Foam"]["cost_savings"]}',
                                          bg="light grey")

    heat_loss_savings_foam_board_label.grid(row=9, column=1, ipadx="50")
    implementation_foam_board_label.grid(row=9, column=2, ipadx="50")
    cost_savings_foam_board_label.grid(row=9, column=3, ipadx="50")

    # Glass
    input_dictionary["k_window_retrofit"] = retrofit_dictionary["Glass"]["k_window_retrofit"]
    input_dictionary["thickness_window_retrofit"] = retrofit_dictionary["Glass"]["thickness_window_retrofit"]
    retrofit_dictionary["Glass"]["heat_loss_savings"] = calculate_retrofit(input_dictionary)
    input_dictionary["k_window_retrofit"] = 1  # resets
    input_dictionary["k_window_retrofit"] = 1  # resets value
    retrofit_dictionary["Glass"]["implementation"] = cost_analysis(input_dictionary, "glass")
    cost_per_kwh = 0.0935  # 9.35 cents
    retrofit_dictionary["Glass"]["cost_savings"] = retrofit_dictionary["Glass"]["heat_loss_savings"] * cost_per_kwh

    heat_loss_savings_glass_label = Label(window2, text=f'{retrofit_dictionary["Glass"]["heat_loss_savings"]}',
                                          bg="light grey")
    implementation_glass_label: Label = Label(window2, text=f'{retrofit_dictionary["Glass"]["implementation"]}',
                                              bg="light grey")
    cost_savings_glass_label = Label(window2, text=f'{retrofit_dictionary["Glass"]["cost_savings"]}', bg="light grey")

    heat_loss_savings_glass_label.grid(row=11, column=1, ipadx="50")
    implementation_glass_label.grid(row=11, column=2, ipadx="50")
    cost_savings_glass_label.grid(row=11, column=3, ipadx="50")

    # Argon_Double_Pane
    input_dictionary["k_window_retrofit"] = retrofit_dictionary["Argon_Double_Pane"]["k_window_retrofit"]
    input_dictionary["thickness_window_retrofit"] = retrofit_dictionary["Argon_Double_Pane"][
        "thickness_window_retrofit"]
    retrofit_dictionary["Argon_Double_Pane"]["heat_loss_savings"] = calculate_retrofit(input_dictionary)
    input_dictionary["k_window_retrofit"] = 1  # resets value
    input_dictionary["k_window_retrofit"] = 1  # resets value
    retrofit_dictionary["Argon_Double_Pane"]["implementation"] = cost_analysis(input_dictionary, "Argon_Double_Pane")
    cost_per_kwh = 0.0935  # 9.35 cents
    retrofit_dictionary["Argon_Double_Pane"]["cost_savings"] = retrofit_dictionary["Argon_Double_Pane"][
                                                                   "heat_loss_savings"] * cost_per_kwh

    heat_loss_savings_glass_label = Label(window2,
                                          text=f'{retrofit_dictionary["Argon_Double_Pane"]["heat_loss_savings"]}',
                                          bg="light grey")
    implementation_glass_label: Label = Label(window2,
                                              text=f'{retrofit_dictionary["Argon_Double_Pane"]["implementation"]}',
                                              bg="light grey")
    cost_savings_glass_label = Label(window2, text=f'{retrofit_dictionary["Argon_Double_Pane"]["cost_savings"]}',
                                     bg="light grey")

    heat_loss_savings_glass_label.grid(row=12, column=1, ipadx="50")
    implementation_glass_label.grid(row=12, column=2, ipadx="50")
    cost_savings_glass_label.grid(row=12, column=3, ipadx="50")

    # Triple_Pane
    input_dictionary["k_window_retrofit"] = retrofit_dictionary["Triple_Pane"]["k_window_retrofit"]
    input_dictionary["thickness_window_retrofit"] = retrofit_dictionary["Triple_Pane"]["thickness_window_retrofit"]
    retrofit_dictionary["Triple_Pane"]["heat_loss_savings"] = calculate_retrofit(input_dictionary)
    input_dictionary["k_window_retrofit"] = 1  # resets value
    input_dictionary["k_window_retrofit"] = 1  # resets value
    retrofit_dictionary["Triple_Pane"]["implementation"] = cost_analysis(input_dictionary, "Triple_Pane")
    cost_per_kwh = 0.0935  # 9.35 cents
    retrofit_dictionary["Triple_Pane"]["cost_savings"] = retrofit_dictionary["Triple_Pane"][
                                                          "heat_loss_savings"] * cost_per_kwh

    heat_loss_savings_glass_label = Label(window2, text=f'{retrofit_dictionary["Triple_Pane"]["heat_loss_savings"]}',
                                          bg="light grey")
    implementation_glass_label: Label = Label(window2, text=f'{retrofit_dictionary["Triple_Pane"]["implementation"]}',
                                              bg="light grey")
    cost_savings_glass_label = Label(window2, text=f'{retrofit_dictionary["Triple_Pane"]["cost_savings"]}',
                                     bg="light grey")

    heat_loss_savings_glass_label.grid(row=13, column=1, ipadx="50")
    implementation_glass_label.grid(row=13, column=2, ipadx="50")
    cost_savings_glass_label.grid(row=13, column=3, ipadx="50")

    print(retrofit_dictionary)


# Used by retrofit function to calculate heat loss savings
def calculate_retrofit(input_dictionary):
    ns_length = input_dictionary["ns_length"]
    ew_length = input_dictionary["ew_length"]
    height = input_dictionary["height"]
    floor_count = input_dictionary["floor_count"]

    # ratio = (window area)/(wall area)
    north_wall_ratio = input_dictionary["north_wall_ratio"]
    south_wall_ratio = input_dictionary["south_wall_ratio"]
    east_wall_ratio = input_dictionary["east_wall_ratio"]
    west_wall_ratio = input_dictionary["west_wall_ratio"]

    temperature = input_dictionary["temperature"]
    k_wall = input_dictionary["k_wall"]
    k_window = input_dictionary["k_window"]
    thickness_wall = input_dictionary["thickness_wall"]
    thickness_window = input_dictionary["thickness_window"]

    k_wall_retrofit = input_dictionary["k_wall_retrofit"]
    k_window_retrofit = input_dictionary["k_window_retrofit"]
    thickness_wall_retrofit = input_dictionary["thickness_wall_retrofit"]

    # R-values
    rvalue_ns_wall = thickness_wall / (k_wall * ns_length * height)
    rvalue_ew_wall = thickness_wall / (k_wall * ew_length * height)
    rvalue_roof = thickness_wall / (k_wall * ns_length * ew_length)
    rvalue_north_window = thickness_window / (k_window * ((ns_length * height) * north_wall_ratio))
    rvalue_south_window = thickness_window / (k_window * ((ns_length * height) * south_wall_ratio))
    rvalue_east_window = thickness_window / (k_window * ((ew_length * height) * east_wall_ratio))
    rvalue_west_window = thickness_window / (k_window * ((ew_length * height) * west_wall_ratio))

    # Retrofit R-values
    rvalue_ns_wall_retrofit = thickness_wall_retrofit / (k_wall_retrofit * ns_length * height)
    rvalue_ew_wall_retrofit = thickness_wall_retrofit / (k_wall_retrofit * ew_length * height)
    rvalue_roof_retrofit = thickness_wall_retrofit / (k_wall_retrofit * ns_length * ew_length)
    rvalue_north_window_retrofit = 1 / (
            k_window_retrofit * ((ns_length * height) * north_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_south_window_retrofit = 1 / (
            k_window_retrofit * ((ns_length * height) * south_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_east_window_retrofit = 1 / (
            k_window_retrofit * ((ew_length * height) * east_wall_ratio))  # WINDOW NEEDS THICKNESS
    rvalue_west_window_retrofit = 1 / (
            k_window_retrofit * ((ew_length * height) * west_wall_ratio))  # WINDOW NEEDS THICKNESS

    room_temperature = 301

    # Heat loss from wall
    north_wall_heat_loss = ((ns_length * height) * (1 - north_wall_ratio) * (room_temperature - temperature)) / (
        rvalue_ns_wall)
    south_wall_heat_loss = ((ns_length * height) * (1 - south_wall_ratio) * (room_temperature - temperature)) / (
        rvalue_ns_wall)
    east_wall_heat_loss = ((ew_length * height) * (1 - east_wall_ratio) * (room_temperature - temperature)) / (
        rvalue_ew_wall)
    west_wall_heat_loss = ((ew_length * height) * (1 - west_wall_ratio) * (room_temperature - temperature)) / (
        rvalue_ew_wall)
    # assuming the roof has the same properties as the wall
    roof_heat_loss = ((ns_length * ew_length) * (room_temperature - temperature)) / (rvalue_roof)

    # Heat loss from wall after retrofit
    north_wall_heat_loss_r = ((ns_length * height) * (1 - north_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ns_wall + rvalue_ns_wall_retrofit)
    south_wall_heat_loss_r = ((ns_length * height) * (1 - south_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ns_wall + rvalue_ns_wall_retrofit)
    east_wall_heat_loss_r = ((ew_length * height) * (1 - east_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ew_wall + rvalue_ew_wall_retrofit)
    west_wall_heat_loss_r = ((ew_length * height) * (1 - west_wall_ratio) * (room_temperature - temperature)) / (
            rvalue_ew_wall + rvalue_ew_wall_retrofit)
    # assuming the roof has the same properties as the wall
    roof_heat_loss_r = ((ns_length * ew_length) * (room_temperature - temperature)) / (
            rvalue_roof + rvalue_roof_retrofit)

    # Heat loss from window before retrofit
    north_window_heat_loss = ((ns_length * height) * north_wall_ratio * (room_temperature - temperature)) / (
        rvalue_north_window)
    south_window_heat_loss = ((ns_length * height) * south_wall_ratio * (room_temperature - temperature)) / (
        rvalue_south_window)
    east_window_heat_loss = ((ew_length * height) * east_wall_ratio * (room_temperature - temperature)) / (
        rvalue_east_window)
    west_window_heat_loss = ((ew_length * height) * west_wall_ratio * (room_temperature - temperature)) / (
        rvalue_west_window)

    # Heat loss from window after REPLACING with retrofit
    north_window_heat_loss_r = ((ns_length * height) * north_wall_ratio * (room_temperature - temperature)) / (
        rvalue_north_window_retrofit)
    south_window_heat_loss_r = ((ns_length * height) * south_wall_ratio * (room_temperature - temperature)) / (
        rvalue_south_window_retrofit)
    east_window_heat_loss_r = ((ew_length * height) * east_wall_ratio * (room_temperature - temperature)) / (
        rvalue_east_window_retrofit)
    west_window_heat_loss_r = ((ew_length * height) * west_wall_ratio * (room_temperature - temperature)) / (
        rvalue_west_window_retrofit)

    # total heat loss before retrofit
    total_wall_heat_loss = floor_count * (
            north_wall_heat_loss + south_wall_heat_loss + east_wall_heat_loss + west_wall_heat_loss + roof_heat_loss)
    total_window_heat_loss = floor_count * (
            north_window_heat_loss + south_window_heat_loss + east_window_heat_loss + west_window_heat_loss)
    total_heat_loss = total_wall_heat_loss + total_window_heat_loss

    # total heat loss after retrofit
    total_wall_heat_loss_r = floor_count * (
            north_wall_heat_loss_r + south_wall_heat_loss_r + east_wall_heat_loss_r + west_wall_heat_loss_r + roof_heat_loss_r)
    total_window_heat_loss_r = floor_count * (
            north_window_heat_loss_r + south_window_heat_loss_r + east_window_heat_loss_r + west_window_heat_loss_r)
    total_heat_loss_r = total_wall_heat_loss_r + total_window_heat_loss_r

    # difference in heat loss
    total_heat_loss_savings = total_heat_loss - total_heat_loss_r

    return round(total_heat_loss_savings)


# Used by retrofit function to calculate material cost and energy savings
def cost_analysis(input_dictionary, option):
    ns_length = input_dictionary["ns_length"]
    ew_length = input_dictionary["ew_length"]
    height = input_dictionary["height"]
    floor_count = input_dictionary["floor_count"]

    # ratio = (window area)/(wall area)
    north_wall_ratio = input_dictionary["north_wall_ratio"]
    south_wall_ratio = input_dictionary["south_wall_ratio"]
    east_wall_ratio = input_dictionary["east_wall_ratio"]
    west_wall_ratio = input_dictionary["west_wall_ratio"]

    total_wall_area = ((ns_length * height * north_wall_ratio) + (ns_length * height * south_wall_ratio) + \
                       (ew_length * height * east_wall_ratio) + (ew_length * height * west_wall_ratio)) * floor_count
    total_window_area = ((ns_length * height * (1 - north_wall_ratio)) + (ns_length * height * (1 - south_wall_ratio)) + \
                         (ew_length * height * (1 - east_wall_ratio)) + (
                                 ew_length * height * (1 - west_wall_ratio))) * floor_count

    foam_board_cost = retrofit_dictionary["foam_board"]["material_cost"]
    foam_board_implementation = total_wall_area * foam_board_cost

    Fiberglass_Loose_Fill_cost = retrofit_dictionary["Fiberglass_Loose_Fill"]["material_cost"]
    Fiberglass_Loose_Fill_implementation = total_wall_area * Fiberglass_Loose_Fill_cost

    Injection_Foam_cost = retrofit_dictionary["Injection_Foam"]["material_cost"]
    Injection_Foam_implementation = total_wall_area * Injection_Foam_cost

    glass_cost = retrofit_dictionary["Glass"]["material_cost"]
    glass_implementation = total_window_area * glass_cost

    Argon_Double_Pane_cost = retrofit_dictionary["Argon_Double_Pane"]["material_cost"]
    Argon_Double_Pane_implementation = total_window_area * Argon_Double_Pane_cost

    Triple_Pane_cost = retrofit_dictionary["Triple_Pane"]["material_cost"]
    Triple_Pane_implementation = total_window_area * Triple_Pane_cost

    if option == "foam_board":
        implementation_cost = foam_board_implementation
    if option == "Fiberglass_Loose_Fill":
        implementation_cost = Fiberglass_Loose_Fill_implementation
    if option == "Injection_Foam":
        implementation_cost = Injection_Foam_implementation
    if option == "glass":
        implementation_cost = glass_implementation
    if option == "Argon_Double_Pane":
        implementation_cost = Argon_Double_Pane_implementation
    if option == "Triple_Pane":
        implementation_cost = Triple_Pane_implementation

    return round(implementation_cost)


# CODE STARTS HERE
if __name__ == "__main__":
    # window 1 setup
    window1 = Tk()
    window1.configure(background='light grey')  # set the background colour of GUI window
    window1.title("Inputs")  # set the title of GUI window
    window1.geometry("600x400")  # set the configuration of GUI window

    # Labels for the window
    heading = Label(window1, text="Building Information", bg="light grey", font='Helvetica 9 bold')
    floors = Label(window1, text="Floors", bg="light grey")
    ns_length = Label(window1, text="North/South Length (m)", bg="light grey")
    ew_length = Label(window1, text="East/West Length (m)", bg="light grey")
    height = Label(window1, text="Height (m)", bg="light grey")
    floor_count = Label(window1, text="Floor Count", bg="light grey")

    wall_ratio = Label(window1, text="Window/Wall ratio", bg="light grey")
    north_wall = Label(window1, text="North wall", bg="light grey")
    south_wall = Label(window1, text="South wall", bg="light grey")
    east = Label(window1, text="East wall", bg="light grey")
    west_wall = Label(window1, text="West wall", bg="light grey")

    insulation = Label(window1, text="Insulation", bg="light grey")
    outer_temperature = Label(window1, text="Outer temperature (K)", bg="light grey")
    thermal_conductivity_wall = Label(window1, text="Thermal Conductivity (Wall)", bg="light grey")
    thermal_conductivity_window = Label(window1, text="Thermal Conductivity (Window)", bg="light grey")
    thickness_wall = Label(window1, text="Wall Thickness (m)", bg="light grey")
    thickness_window = Label(window1, text="Window Thickness (m)", bg="light grey")

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
    # must be passed for the code to work
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
    # submit button starts the evaluation
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
