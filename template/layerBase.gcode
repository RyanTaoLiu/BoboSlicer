;LAYER_START:{layer_idx:d}
;PositionZ:{position_z}mm
M6054 "{image_file_name}";Show image
G0 Z{position_z_p5} F100;Z Lift (1)
G0 Z{position_z} F100;Retract (1)
G4 P{wait_time_before_cure:d};Wait before cure
M106 S{turn_on_led_M106_S:d};Turn LED ON
G4 P{cure_time_delay:d};Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

