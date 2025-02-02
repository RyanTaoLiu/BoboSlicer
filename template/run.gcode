;Generated by UVtools v4.3.2 64-bits @ 5/7/2024 5:27:23 PM
;fileName:
;machineType:Phrozen Sonic Mega 8K S
;estimatedPrintTime:1554.97
;volume:4.893
;resin:
;weight:4894.703
;price:0.294
;layerHeight:0.05
;resolutionX:7680
;resolutionY:4320
;machineX:330.24
;machineY:185.76
;machineZ:300
;projectType:Normal
;normalExposureTime:1.3
;bottomLayExposureTime:30
;bottomLayerExposureTime:30
;normalDropSpeed:240
;normalLayerLiftSpeed:60
;normalLayerLiftHeight:2
;zSlowUpDistance:0
;bottomLayCount:6
;bottomLayerCount:6
;mirror:0
;totalLayer:100
;bottomLayerLiftHeight:3
;bottomLayerLiftSpeed:60
;bottomLightOffTime:3
;lightOffTime:1
;bottomPWMLight:255
;PWMLight:204
;antiAliasLevel:8

;START_GCODE_BEGIN
G21;Set units to be mm
G90;Absolute positioning
M17;Enable motors
M106 S0;Turn LED OFF
;<Slice> Blank
G28 Z0;Home Z
;END_GCODE_BEGIN

;LAYER_START:0
;PositionZ:0.05mm
M6054 "1.png";Show image
G0 Z3.05 F60;Z Lift (1)
G0 Z8.05 F180;Z Lift (2)
G4 P1000;Wait after lift
G0 Z2.05 F180;Retract (1)
G0 Z0.05 F60;Retract (2)
G4 P3000;Wait before cure
M106 S255;Turn LED ON
G4 P30000;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
G4 P1000;Wait after cure
;LAYER_END

;LAYER_START:1
;PositionZ:0.1mm
M6054 "2.png";Show image
G0 Z3.1 F60;Z Lift (1)
G0 Z8.1 F180;Z Lift (2)
G4 P1000;Wait after lift
G0 Z2.1 F180;Retract (1)
G0 Z0.1 F60;Retract (2)
G4 P3000;Wait before cure
M106 S255;Turn LED ON
G4 P30000;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
G4 P1000;Wait after cure
;LAYER_END

;LAYER_START:2
;PositionZ:0.15mm
M6054 "3.png";Show image
G0 Z3.15 F60;Z Lift (1)
G0 Z8.15 F180;Z Lift (2)
G4 P1000;Wait after lift
G0 Z2.15 F180;Retract (1)
G0 Z0.15 F60;Retract (2)
G4 P3000;Wait before cure
M106 S255;Turn LED ON
G4 P30000;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
G4 P1000;Wait after cure
;LAYER_END

;LAYER_START:3
;PositionZ:0.2mm
M6054 "4.png";Show image
G0 Z3.2 F60;Z Lift (1)
G0 Z8.2 F180;Z Lift (2)
G4 P1000;Wait after lift
G0 Z2.2 F180;Retract (1)
G0 Z0.2 F60;Retract (2)
G4 P3000;Wait before cure
M106 S255;Turn LED ON
G4 P30000;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
G4 P1000;Wait after cure
;LAYER_END

;LAYER_START:4
;PositionZ:0.25mm
M6054 "5.png";Show image
G0 Z3.25 F60;Z Lift (1)
G0 Z8.25 F180;Z Lift (2)
G4 P1000;Wait after lift
G0 Z2.25 F180;Retract (1)
G0 Z0.25 F60;Retract (2)
G4 P3000;Wait before cure
M106 S255;Turn LED ON
G4 P30000;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
G4 P1000;Wait after cure
;LAYER_END

;LAYER_START:5
;PositionZ:0.3mm
M6054 "6.png";Show image
G0 Z3.3 F60;Z Lift (1)
G0 Z8.3 F180;Z Lift (2)
G4 P1000;Wait after lift
G0 Z2.3 F180;Retract (1)
G0 Z0.3 F60;Retract (2)
G4 P3000;Wait before cure
M106 S255;Turn LED ON
G4 P30000;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
G4 P1000;Wait after cure
;LAYER_END

;LAYER_START:6
;PositionZ:0.35mm
M6054 "7.png";Show image
G0 Z2.35 F60;Z Lift (1)
G0 Z6.35 F240;Z Lift (2)
G0 Z4.35 F240;Retract (1)
G0 Z0.35 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P25220;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:7
;PositionZ:0.4mm
M6054 "8.png";Show image
G0 Z2.4 F60;Z Lift (1)
G0 Z6.4 F240;Z Lift (2)
G0 Z4.4 F240;Retract (1)
G0 Z0.4 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P20430;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:8
;PositionZ:0.45mm
M6054 "9.png";Show image
G0 Z2.45 F60;Z Lift (1)
G0 Z6.45 F240;Z Lift (2)
G0 Z4.45 F240;Retract (1)
G0 Z0.45 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P15650;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:9
;PositionZ:0.5mm
M6054 "10.png";Show image
G0 Z2.5 F60;Z Lift (1)
G0 Z6.5 F240;Z Lift (2)
G0 Z4.5 F240;Retract (1)
G0 Z0.5 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P10870;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:10
;PositionZ:0.55mm
M6054 "11.png";Show image
G0 Z2.55 F60;Z Lift (1)
G0 Z6.55 F240;Z Lift (2)
G0 Z4.55 F240;Retract (1)
G0 Z0.55 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P6080;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:11
;PositionZ:0.6mm
M6054 "12.png";Show image
G0 Z2.6 F60;Z Lift (1)
G0 Z6.6 F240;Z Lift (2)
G0 Z4.6 F240;Retract (1)
G0 Z0.6 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:12
;PositionZ:0.65mm
M6054 "13.png";Show image
G0 Z2.65 F60;Z Lift (1)
G0 Z6.65 F240;Z Lift (2)
G0 Z4.65 F240;Retract (1)
G0 Z0.65 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:13
;PositionZ:0.7mm
M6054 "14.png";Show image
G0 Z2.7 F60;Z Lift (1)
G0 Z6.7 F240;Z Lift (2)
G0 Z4.7 F240;Retract (1)
G0 Z0.7 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:14
;PositionZ:0.75mm
M6054 "15.png";Show image
G0 Z2.75 F60;Z Lift (1)
G0 Z6.75 F240;Z Lift (2)
G0 Z4.75 F240;Retract (1)
G0 Z0.75 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:15
;PositionZ:0.8mm
M6054 "16.png";Show image
G0 Z2.8 F60;Z Lift (1)
G0 Z6.8 F240;Z Lift (2)
G0 Z4.8 F240;Retract (1)
G0 Z0.8 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:16
;PositionZ:0.85mm
M6054 "17.png";Show image
G0 Z2.85 F60;Z Lift (1)
G0 Z6.85 F240;Z Lift (2)
G0 Z4.85 F240;Retract (1)
G0 Z0.85 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:17
;PositionZ:0.9mm
M6054 "18.png";Show image
G0 Z2.9 F60;Z Lift (1)
G0 Z6.9 F240;Z Lift (2)
G0 Z4.9 F240;Retract (1)
G0 Z0.9 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:18
;PositionZ:0.95mm
M6054 "19.png";Show image
G0 Z2.95 F60;Z Lift (1)
G0 Z6.95 F240;Z Lift (2)
G0 Z4.95 F240;Retract (1)
G0 Z0.95 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:19
;PositionZ:1mm
M6054 "20.png";Show image
G0 Z3 F60;Z Lift (1)
G0 Z7 F240;Z Lift (2)
G0 Z5 F240;Retract (1)
G0 Z1 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:20
;PositionZ:1.05mm
M6054 "21.png";Show image
G0 Z3.05 F60;Z Lift (1)
G0 Z7.05 F240;Z Lift (2)
G0 Z5.05 F240;Retract (1)
G0 Z1.05 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:21
;PositionZ:1.1mm
M6054 "22.png";Show image
G0 Z3.1 F60;Z Lift (1)
G0 Z7.1 F240;Z Lift (2)
G0 Z5.1 F240;Retract (1)
G0 Z1.1 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:22
;PositionZ:1.15mm
M6054 "23.png";Show image
G0 Z3.15 F60;Z Lift (1)
G0 Z7.15 F240;Z Lift (2)
G0 Z5.15 F240;Retract (1)
G0 Z1.15 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:23
;PositionZ:1.2mm
M6054 "24.png";Show image
G0 Z3.2 F60;Z Lift (1)
G0 Z7.2 F240;Z Lift (2)
G0 Z5.2 F240;Retract (1)
G0 Z1.2 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:24
;PositionZ:1.25mm
M6054 "25.png";Show image
G0 Z3.25 F60;Z Lift (1)
G0 Z7.25 F240;Z Lift (2)
G0 Z5.25 F240;Retract (1)
G0 Z1.25 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:25
;PositionZ:1.3mm
M6054 "26.png";Show image
G0 Z3.3 F60;Z Lift (1)
G0 Z7.3 F240;Z Lift (2)
G0 Z5.3 F240;Retract (1)
G0 Z1.3 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:26
;PositionZ:1.35mm
M6054 "27.png";Show image
G0 Z3.35 F60;Z Lift (1)
G0 Z7.35 F240;Z Lift (2)
G0 Z5.35 F240;Retract (1)
G0 Z1.35 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:27
;PositionZ:1.4mm
M6054 "28.png";Show image
G0 Z3.4 F60;Z Lift (1)
G0 Z7.4 F240;Z Lift (2)
G0 Z5.4 F240;Retract (1)
G0 Z1.4 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:28
;PositionZ:1.45mm
M6054 "29.png";Show image
G0 Z3.45 F60;Z Lift (1)
G0 Z7.45 F240;Z Lift (2)
G0 Z5.45 F240;Retract (1)
G0 Z1.45 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:29
;PositionZ:1.5mm
M6054 "30.png";Show image
G0 Z3.5 F60;Z Lift (1)
G0 Z7.5 F240;Z Lift (2)
G0 Z5.5 F240;Retract (1)
G0 Z1.5 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:30
;PositionZ:1.55mm
M6054 "31.png";Show image
G0 Z3.55 F60;Z Lift (1)
G0 Z7.55 F240;Z Lift (2)
G0 Z5.55 F240;Retract (1)
G0 Z1.55 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:31
;PositionZ:1.6mm
M6054 "32.png";Show image
G0 Z3.6 F60;Z Lift (1)
G0 Z7.6 F240;Z Lift (2)
G0 Z5.6 F240;Retract (1)
G0 Z1.6 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:32
;PositionZ:1.65mm
M6054 "33.png";Show image
G0 Z3.65 F60;Z Lift (1)
G0 Z7.65 F240;Z Lift (2)
G0 Z5.65 F240;Retract (1)
G0 Z1.65 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:33
;PositionZ:1.7mm
M6054 "34.png";Show image
G0 Z3.7 F60;Z Lift (1)
G0 Z7.7 F240;Z Lift (2)
G0 Z5.7 F240;Retract (1)
G0 Z1.7 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:34
;PositionZ:1.75mm
M6054 "35.png";Show image
G0 Z3.75 F60;Z Lift (1)
G0 Z7.75 F240;Z Lift (2)
G0 Z5.75 F240;Retract (1)
G0 Z1.75 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:35
;PositionZ:1.8mm
M6054 "36.png";Show image
G0 Z3.8 F60;Z Lift (1)
G0 Z7.8 F240;Z Lift (2)
G0 Z5.8 F240;Retract (1)
G0 Z1.8 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:36
;PositionZ:1.85mm
M6054 "37.png";Show image
G0 Z3.85 F60;Z Lift (1)
G0 Z7.85 F240;Z Lift (2)
G0 Z5.85 F240;Retract (1)
G0 Z1.85 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:37
;PositionZ:1.9mm
M6054 "38.png";Show image
G0 Z3.9 F60;Z Lift (1)
G0 Z7.9 F240;Z Lift (2)
G0 Z5.9 F240;Retract (1)
G0 Z1.9 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:38
;PositionZ:1.95mm
M6054 "39.png";Show image
G0 Z3.95 F60;Z Lift (1)
G0 Z7.95 F240;Z Lift (2)
G0 Z5.95 F240;Retract (1)
G0 Z1.95 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:39
;PositionZ:2mm
M6054 "40.png";Show image
G0 Z4 F60;Z Lift (1)
G0 Z8 F240;Z Lift (2)
G0 Z6 F240;Retract (1)
G0 Z2 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:40
;PositionZ:2.05mm
M6054 "41.png";Show image
G0 Z4.05 F60;Z Lift (1)
G0 Z8.05 F240;Z Lift (2)
G0 Z6.05 F240;Retract (1)
G0 Z2.05 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:41
;PositionZ:2.1mm
M6054 "42.png";Show image
G0 Z4.1 F60;Z Lift (1)
G0 Z8.1 F240;Z Lift (2)
G0 Z6.1 F240;Retract (1)
G0 Z2.1 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:42
;PositionZ:2.15mm
M6054 "43.png";Show image
G0 Z4.15 F60;Z Lift (1)
G0 Z8.15 F240;Z Lift (2)
G0 Z6.15 F240;Retract (1)
G0 Z2.15 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:43
;PositionZ:2.2mm
M6054 "44.png";Show image
G0 Z4.2 F60;Z Lift (1)
G0 Z8.2 F240;Z Lift (2)
G0 Z6.2 F240;Retract (1)
G0 Z2.2 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:44
;PositionZ:2.25mm
M6054 "45.png";Show image
G0 Z4.25 F60;Z Lift (1)
G0 Z8.25 F240;Z Lift (2)
G0 Z6.25 F240;Retract (1)
G0 Z2.25 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:45
;PositionZ:2.3mm
M6054 "46.png";Show image
G0 Z4.3 F60;Z Lift (1)
G0 Z8.3 F240;Z Lift (2)
G0 Z6.3 F240;Retract (1)
G0 Z2.3 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:46
;PositionZ:2.35mm
M6054 "47.png";Show image
G0 Z4.35 F60;Z Lift (1)
G0 Z8.35 F240;Z Lift (2)
G0 Z6.35 F240;Retract (1)
G0 Z2.35 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:47
;PositionZ:2.4mm
M6054 "48.png";Show image
G0 Z4.4 F60;Z Lift (1)
G0 Z8.4 F240;Z Lift (2)
G0 Z6.4 F240;Retract (1)
G0 Z2.4 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:48
;PositionZ:2.45mm
M6054 "49.png";Show image
G0 Z4.45 F60;Z Lift (1)
G0 Z8.45 F240;Z Lift (2)
G0 Z6.45 F240;Retract (1)
G0 Z2.45 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:49
;PositionZ:2.5mm
M6054 "50.png";Show image
G0 Z4.5 F60;Z Lift (1)
G0 Z8.5 F240;Z Lift (2)
G0 Z6.5 F240;Retract (1)
G0 Z2.5 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:50
;PositionZ:2.55mm
M6054 "51.png";Show image
G0 Z4.55 F60;Z Lift (1)
G0 Z8.55 F240;Z Lift (2)
G0 Z6.55 F240;Retract (1)
G0 Z2.55 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:51
;PositionZ:2.6mm
M6054 "52.png";Show image
G0 Z4.6 F60;Z Lift (1)
G0 Z8.6 F240;Z Lift (2)
G0 Z6.6 F240;Retract (1)
G0 Z2.6 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:52
;PositionZ:2.65mm
M6054 "53.png";Show image
G0 Z4.65 F60;Z Lift (1)
G0 Z8.65 F240;Z Lift (2)
G0 Z6.65 F240;Retract (1)
G0 Z2.65 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:53
;PositionZ:2.7mm
M6054 "54.png";Show image
G0 Z4.7 F60;Z Lift (1)
G0 Z8.7 F240;Z Lift (2)
G0 Z6.7 F240;Retract (1)
G0 Z2.7 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:54
;PositionZ:2.75mm
M6054 "55.png";Show image
G0 Z4.75 F60;Z Lift (1)
G0 Z8.75 F240;Z Lift (2)
G0 Z6.75 F240;Retract (1)
G0 Z2.75 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:55
;PositionZ:2.8mm
M6054 "56.png";Show image
G0 Z4.8 F60;Z Lift (1)
G0 Z8.8 F240;Z Lift (2)
G0 Z6.8 F240;Retract (1)
G0 Z2.8 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:56
;PositionZ:2.85mm
M6054 "57.png";Show image
G0 Z4.85 F60;Z Lift (1)
G0 Z8.85 F240;Z Lift (2)
G0 Z6.85 F240;Retract (1)
G0 Z2.85 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:57
;PositionZ:2.9mm
M6054 "58.png";Show image
G0 Z4.9 F60;Z Lift (1)
G0 Z8.9 F240;Z Lift (2)
G0 Z6.9 F240;Retract (1)
G0 Z2.9 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:58
;PositionZ:2.95mm
M6054 "59.png";Show image
G0 Z4.95 F60;Z Lift (1)
G0 Z8.95 F240;Z Lift (2)
G0 Z6.95 F240;Retract (1)
G0 Z2.95 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:59
;PositionZ:3mm
M6054 "60.png";Show image
G0 Z5 F60;Z Lift (1)
G0 Z9 F240;Z Lift (2)
G0 Z7 F240;Retract (1)
G0 Z3 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:60
;PositionZ:3.05mm
M6054 "61.png";Show image
G0 Z5.05 F60;Z Lift (1)
G0 Z9.05 F240;Z Lift (2)
G0 Z7.05 F240;Retract (1)
G0 Z3.05 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:61
;PositionZ:3.1mm
M6054 "62.png";Show image
G0 Z5.1 F60;Z Lift (1)
G0 Z9.1 F240;Z Lift (2)
G0 Z7.1 F240;Retract (1)
G0 Z3.1 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:62
;PositionZ:3.15mm
M6054 "63.png";Show image
G0 Z5.15 F60;Z Lift (1)
G0 Z9.15 F240;Z Lift (2)
G0 Z7.15 F240;Retract (1)
G0 Z3.15 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:63
;PositionZ:3.2mm
M6054 "64.png";Show image
G0 Z5.2 F60;Z Lift (1)
G0 Z9.2 F240;Z Lift (2)
G0 Z7.2 F240;Retract (1)
G0 Z3.2 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:64
;PositionZ:3.25mm
M6054 "65.png";Show image
G0 Z5.25 F60;Z Lift (1)
G0 Z9.25 F240;Z Lift (2)
G0 Z7.25 F240;Retract (1)
G0 Z3.25 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:65
;PositionZ:3.3mm
M6054 "66.png";Show image
G0 Z5.3 F60;Z Lift (1)
G0 Z9.3 F240;Z Lift (2)
G0 Z7.3 F240;Retract (1)
G0 Z3.3 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:66
;PositionZ:3.35mm
M6054 "67.png";Show image
G0 Z5.35 F60;Z Lift (1)
G0 Z9.35 F240;Z Lift (2)
G0 Z7.35 F240;Retract (1)
G0 Z3.35 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:67
;PositionZ:3.4mm
M6054 "68.png";Show image
G0 Z5.4 F60;Z Lift (1)
G0 Z9.4 F240;Z Lift (2)
G0 Z7.4 F240;Retract (1)
G0 Z3.4 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:68
;PositionZ:3.45mm
M6054 "69.png";Show image
G0 Z5.45 F60;Z Lift (1)
G0 Z9.45 F240;Z Lift (2)
G0 Z7.45 F240;Retract (1)
G0 Z3.45 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:69
;PositionZ:3.5mm
M6054 "70.png";Show image
G0 Z5.5 F60;Z Lift (1)
G0 Z9.5 F240;Z Lift (2)
G0 Z7.5 F240;Retract (1)
G0 Z3.5 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:70
;PositionZ:3.55mm
M6054 "71.png";Show image
G0 Z5.55 F60;Z Lift (1)
G0 Z9.55 F240;Z Lift (2)
G0 Z7.55 F240;Retract (1)
G0 Z3.55 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:71
;PositionZ:3.6mm
M6054 "72.png";Show image
G0 Z5.6 F60;Z Lift (1)
G0 Z9.6 F240;Z Lift (2)
G0 Z7.6 F240;Retract (1)
G0 Z3.6 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:72
;PositionZ:3.65mm
M6054 "73.png";Show image
G0 Z5.65 F60;Z Lift (1)
G0 Z9.65 F240;Z Lift (2)
G0 Z7.65 F240;Retract (1)
G0 Z3.65 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:73
;PositionZ:3.7mm
M6054 "74.png";Show image
G0 Z5.7 F60;Z Lift (1)
G0 Z9.7 F240;Z Lift (2)
G0 Z7.7 F240;Retract (1)
G0 Z3.7 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:74
;PositionZ:3.75mm
M6054 "75.png";Show image
G0 Z5.75 F60;Z Lift (1)
G0 Z9.75 F240;Z Lift (2)
G0 Z7.75 F240;Retract (1)
G0 Z3.75 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:75
;PositionZ:3.8mm
M6054 "76.png";Show image
G0 Z5.8 F60;Z Lift (1)
G0 Z9.8 F240;Z Lift (2)
G0 Z7.8 F240;Retract (1)
G0 Z3.8 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:76
;PositionZ:3.85mm
M6054 "77.png";Show image
G0 Z5.85 F60;Z Lift (1)
G0 Z9.85 F240;Z Lift (2)
G0 Z7.85 F240;Retract (1)
G0 Z3.85 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:77
;PositionZ:3.9mm
M6054 "78.png";Show image
G0 Z5.9 F60;Z Lift (1)
G0 Z9.9 F240;Z Lift (2)
G0 Z7.9 F240;Retract (1)
G0 Z3.9 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:78
;PositionZ:3.95mm
M6054 "79.png";Show image
G0 Z5.95 F60;Z Lift (1)
G0 Z9.95 F240;Z Lift (2)
G0 Z7.95 F240;Retract (1)
G0 Z3.95 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:79
;PositionZ:4mm
M6054 "80.png";Show image
G0 Z6 F60;Z Lift (1)
G0 Z10 F240;Z Lift (2)
G0 Z8 F240;Retract (1)
G0 Z4 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:80
;PositionZ:4.05mm
M6054 "81.png";Show image
G0 Z6.05 F60;Z Lift (1)
G0 Z10.05 F240;Z Lift (2)
G0 Z8.05 F240;Retract (1)
G0 Z4.05 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:81
;PositionZ:4.1mm
M6054 "82.png";Show image
G0 Z6.1 F60;Z Lift (1)
G0 Z10.1 F240;Z Lift (2)
G0 Z8.1 F240;Retract (1)
G0 Z4.1 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:82
;PositionZ:4.15mm
M6054 "83.png";Show image
G0 Z6.15 F60;Z Lift (1)
G0 Z10.15 F240;Z Lift (2)
G0 Z8.15 F240;Retract (1)
G0 Z4.15 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:83
;PositionZ:4.2mm
M6054 "84.png";Show image
G0 Z6.2 F60;Z Lift (1)
G0 Z10.2 F240;Z Lift (2)
G0 Z8.2 F240;Retract (1)
G0 Z4.2 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:84
;PositionZ:4.25mm
M6054 "85.png";Show image
G0 Z6.25 F60;Z Lift (1)
G0 Z10.25 F240;Z Lift (2)
G0 Z8.25 F240;Retract (1)
G0 Z4.25 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:85
;PositionZ:4.3mm
M6054 "86.png";Show image
G0 Z6.3 F60;Z Lift (1)
G0 Z10.3 F240;Z Lift (2)
G0 Z8.3 F240;Retract (1)
G0 Z4.3 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:86
;PositionZ:4.35mm
M6054 "87.png";Show image
G0 Z6.35 F60;Z Lift (1)
G0 Z10.35 F240;Z Lift (2)
G0 Z8.35 F240;Retract (1)
G0 Z4.35 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:87
;PositionZ:4.4mm
M6054 "88.png";Show image
G0 Z6.4 F60;Z Lift (1)
G0 Z10.4 F240;Z Lift (2)
G0 Z8.4 F240;Retract (1)
G0 Z4.4 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:88
;PositionZ:4.45mm
M6054 "89.png";Show image
G0 Z6.45 F60;Z Lift (1)
G0 Z10.45 F240;Z Lift (2)
G0 Z8.45 F240;Retract (1)
G0 Z4.45 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:89
;PositionZ:4.5mm
M6054 "90.png";Show image
G0 Z6.5 F60;Z Lift (1)
G0 Z10.5 F240;Z Lift (2)
G0 Z8.5 F240;Retract (1)
G0 Z4.5 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:90
;PositionZ:4.55mm
M6054 "91.png";Show image
G0 Z6.55 F60;Z Lift (1)
G0 Z10.55 F240;Z Lift (2)
G0 Z8.55 F240;Retract (1)
G0 Z4.55 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:91
;PositionZ:4.6mm
M6054 "92.png";Show image
G0 Z6.6 F60;Z Lift (1)
G0 Z10.6 F240;Z Lift (2)
G0 Z8.6 F240;Retract (1)
G0 Z4.6 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:92
;PositionZ:4.65mm
M6054 "93.png";Show image
G0 Z6.65 F60;Z Lift (1)
G0 Z10.65 F240;Z Lift (2)
G0 Z8.65 F240;Retract (1)
G0 Z4.65 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:93
;PositionZ:4.7mm
M6054 "94.png";Show image
G0 Z6.7 F60;Z Lift (1)
G0 Z10.7 F240;Z Lift (2)
G0 Z8.7 F240;Retract (1)
G0 Z4.7 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:94
;PositionZ:4.75mm
M6054 "95.png";Show image
G0 Z6.75 F60;Z Lift (1)
G0 Z10.75 F240;Z Lift (2)
G0 Z8.75 F240;Retract (1)
G0 Z4.75 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:95
;PositionZ:4.8mm
M6054 "96.png";Show image
G0 Z6.8 F60;Z Lift (1)
G0 Z10.8 F240;Z Lift (2)
G0 Z8.8 F240;Retract (1)
G0 Z4.8 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:96
;PositionZ:4.85mm
M6054 "97.png";Show image
G0 Z6.85 F60;Z Lift (1)
G0 Z10.85 F240;Z Lift (2)
G0 Z8.85 F240;Retract (1)
G0 Z4.85 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:97
;PositionZ:4.9mm
M6054 "98.png";Show image
G0 Z6.9 F60;Z Lift (1)
G0 Z10.9 F240;Z Lift (2)
G0 Z8.9 F240;Retract (1)
G0 Z4.9 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:98
;PositionZ:4.95mm
M6054 "99.png";Show image
G0 Z6.95 F60;Z Lift (1)
G0 Z10.95 F240;Z Lift (2)
G0 Z8.95 F240;Retract (1)
G0 Z4.95 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;LAYER_START:99
;PositionZ:5mm
M6054 "100.png";Show image
G0 Z7 F60;Z Lift (1)
G0 Z11 F240;Z Lift (2)
G0 Z9 F240;Retract (1)
G0 Z5 F60;Retract (2)
G4 P1000;Wait before cure
M106 S204;Turn LED ON
G4 P1300;Cure time/delay
M106 S0;Turn LED OFF
;<Slice> Blank
;LAYER_END

;START_GCODE_END
M106 S0;Turn LED OFF
G0 Z9 F60;Z Lift (1)
G1 Z300 F240;Move Z
M18;Disable motors
;END_GCODE_END
;<Completed>
