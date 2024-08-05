# Inhalt des Moduls:
# - das Dictionary mit den BMS Telemetrie-Daten
# - die Funktion zum Setzen der BMS Telemetrie-Daten

telemetry = {
    "alive": False,
    "analog_data_packs": 0,
    "total_cells": 0,
    "v_cell_1": 0,
    "v_cell_2": 0,
    "v_cell_3": 0,
    "v_cell_4": 0,
    "v_cell_5": 0,
    "v_cell_6": 0,
    "v_cell_7": 0,
    "v_cell_8": 0,
    "v_cell_9": 0,
    "v_cell_10": 0,
    "v_cell_11": 0,
    "v_cell_12": 0,
    "v_cell_13": 0,
    "v_cell_14": 0,
    "v_cell_15": 0,
    "v_cell_16": 0,
    "cell_max_diff_volt": 0,
    "total_temps": 0,
    "temp_1": 0,
    "temp_2": 0,
    "temp_3": 0,
    "temp_4": 0,
    "temp_5": 0,
    "temp_6": 0,
    "i_pack": 0,
    "v_pack": 0,
    "i_remaining_capacity": 0,
    "i_full_capacity": 0,
    "soc": 0,
    "cycles": 0,
    "i_design_capacity": 0,
    "soh": 0,
    "warning_info_packs": 0,
    "current_limit": 0,
    "charge_fet": 0,
    "discharge_fet": 0,
    "pack_indicate": 0,
    "reverse": 0,
    "ac_in": 0,
    "heart": 0,
    "warning_string": "",
    "balancing_1": 0,
    "balancing_2": 0
}

def set_telemetry(key, value):
    telemetry[key] = value
    return telemetry
