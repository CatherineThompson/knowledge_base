G00 S1; endstops
G00 E0; no extrusion
G01 S1; endstops
G01 E0; no extrusion
G21; millimeters
G91 G0 F300.0 Z20.000; pen park !!Zsafe
G90; absolute
G00 F300.0 Z21.000; pen park !!Zpark
G00 F2400.0 Y0.000; !!Ybottom
G00 F2400.0 X0.000; !!Xleft
G00 F2400.0 X59.361 Y42.279; move !!Xleft+59.361 Ybottom+42.279
G00 F300.0 Z1.000; pen down !!Zwork
G01 F2100.0 X51.221 Y44.216; draw !!Xleft+51.221 Ybottom+44.216
G01 F2100.0 X44.458 Y39.470; draw !!Xleft+44.458 Ybottom+39.470
G01 F2100.0 X43.869 Y47.473; draw !!Xleft+43.869 Ybottom+47.473
G01 F2100.0 X37.060 Y52.158; draw !!Xleft+37.060 Ybottom+52.158
G01 F2100.0 X44.836 Y55.167; draw !!Xleft+44.836 Ybottom+55.167
G01 F2100.0 X47.390 Y62.808; draw !!Xleft+47.390 Ybottom+62.808
G01 F2100.0 X52.785 Y56.665; draw !!Xleft+52.785 Ybottom+56.665
G01 F2100.0 X61.173 Y56.702; draw !!Xleft+61.173 Ybottom+56.702
G01 F2100.0 X56.731 Y49.897; draw !!Xleft+56.731 Ybottom+49.897
G01 F2100.0 X59.361 Y42.279; draw !!Xleft+59.361 Ybottom+42.279
G01 F2100.0 X58.388 Y42.511; draw !!Xleft+58.388 Ybottom+42.511
G00 F300.0 Z21.000; pen park !!Zpark
