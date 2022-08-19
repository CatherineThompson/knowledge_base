G00 S1; endstops
G00 E0; no extrusion
G01 S1; endstops
G01 E0; no extrusion
G21; millimeters
G91 G0 F300.0 Z20.000; pen park !!Zsafe
G90; absolute
G28 X; home
G28 Y; home
G28 Z; home
G00 F300.0 Z35.000; pen park !!Zpark
G00 F2400.0 Y0.000; !!Ybottom
G00 F2400.0 X0.000; !!Xleft
G00 F2400.0 X178.196 Y89.671; move !!Xleft+178.196 Ybottom+89.671
G00 F300.0 Z15.000; pen down !!Zwork
G01 F2100.0 X113.212 Y111.936; draw !!Xleft+113.212 Ybottom+111.936
G01 F2100.0 X55.853 Y78.938; draw !!Xleft+55.853 Ybottom+78.938
G01 F2100.0 X57.678 Y145.559; draw !!Xleft+57.678 Ybottom+145.559
G01 F2100.0 X7.487 Y188.094; draw !!Xleft+7.487 Ybottom+188.094
G01 F2100.0 X73.599 Y207.004; draw !!Xleft+73.599 Ybottom+207.004
G01 F2100.0 X99.938 Y266.290; draw !!Xleft+99.938 Ybottom+266.290
G01 F2100.0 X138.972 Y211.355; draw !!Xleft+138.972 Ybottom+211.355
G01 F2100.0 X205.441 Y205.461; draw !!Xleft+205.441 Ybottom+205.461
G01 F2100.0 X163.455 Y152.600; draw !!Xleft+163.455 Ybottom+152.600
G01 F2100.0 X178.196 Y89.671; draw !!Xleft+178.196 Ybottom+89.671
G01 F2100.0 X177.250 Y89.995; draw !!Xleft+177.250 Ybottom+89.995
G00 F300.0 Z35.000; pen park !!Zpark
