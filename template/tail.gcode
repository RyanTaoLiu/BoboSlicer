;START_GCODE_END
M106 S0;Turn LED OFF
G0 Z{position_z_p8} F60;Z Lift (1)
G1 Z300 F240;Move Z
M18;Disable motors
;END_GCODE_END
;<Completed>

