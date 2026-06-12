STD_SYMBOLS = r"""
    (symbol "Device:R"
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 0)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "R"
    			(at 2.032 0 90)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Value" "R"
    			(at 0 0 90)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Footprint" ""
    			(at -1.778 0 90)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Resistor"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "R res resistor"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_fp_filters" "R_*"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "R_0_1"
    			(rectangle
    				(start -1.016 -2.54)
    				(end 1.016 2.54)
    				(stroke
    					(width 0.254)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "R_1_1"
    			(pin passive line
    				(at 0 3.81 270)
    				(length 1.27)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin passive line
    				(at 0 -3.81 90)
    				(length 1.27)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "2"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "Device:C"
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 0.254)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "C"
    			(at 0.635 2.54 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    				(justify left)
    			)
    		)
    		(property "Value" "C"
    			(at 0.635 -2.54 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    				(justify left)
    			)
    		)
    		(property "Footprint" ""
    			(at 0.9652 -3.81 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Unpolarized capacitor"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "cap capacitor"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_fp_filters" "C_*"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "C_0_1"
    			(polyline
    				(pts
    					(xy -2.032 0.762) (xy 2.032 0.762)
    				)
    				(stroke
    					(width 0.508)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy -2.032 -0.762) (xy 2.032 -0.762)
    				)
    				(stroke
    					(width 0.508)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "C_1_1"
    			(pin passive line
    				(at 0 3.81 270)
    				(length 2.794)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin passive line
    				(at 0 -3.81 90)
    				(length 2.794)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "2"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "Device:C_Polarized"
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 0.254)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "C"
    			(at 0.635 2.54 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    				(justify left)
    			)
    		)
    		(property "Value" "C_Polarized"
    			(at 0.635 -2.54 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    				(justify left)
    			)
    		)
    		(property "Footprint" ""
    			(at 0.9652 -3.81 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Polarized capacitor"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "cap capacitor"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_fp_filters" "CP_*"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "C_Polarized_0_1"
    			(rectangle
    				(start -2.286 0.508)
    				(end 2.286 1.016)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy -1.778 2.286) (xy -0.762 2.286)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy -1.27 2.794) (xy -1.27 1.778)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(rectangle
    				(start 2.286 -0.508)
    				(end -2.286 -1.016)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type outline)
    				)
    			)
    		)
    		(symbol "C_Polarized_1_1"
    			(pin passive line
    				(at 0 3.81 270)
    				(length 2.794)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin passive line
    				(at 0 -3.81 90)
    				(length 2.794)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "2"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "Device:L"
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 1.016)
    			(hide yes)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "L"
    			(at -1.27 0 90)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Value" "L"
    			(at 1.905 0 90)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Footprint" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Inductor"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "inductor choke coil reactor magnetic"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_fp_filters" "Choke_* *Coil* Inductor_* L_*"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "L_0_1"
    			(arc
    				(start 0 2.54)
    				(mid 0.6323 1.905)
    				(end 0 1.27)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(arc
    				(start 0 1.27)
    				(mid 0.6323 0.635)
    				(end 0 0)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(arc
    				(start 0 0)
    				(mid 0.6323 -0.635)
    				(end 0 -1.27)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(arc
    				(start 0 -1.27)
    				(mid 0.6323 -1.905)
    				(end 0 -2.54)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "L_1_1"
    			(pin passive line
    				(at 0 3.81 270)
    				(length 1.27)
    				(name "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin passive line
    				(at 0 -3.81 90)
    				(length 1.27)
    				(name "2"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "2"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "Device:Q_PMOS"
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 0)
    			(hide yes)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "Q"
    			(at 5.08 1.27 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    				(justify left)
    			)
    		)
    		(property "Value" "Q_PMOS"
    			(at 5.08 -1.27 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    				(justify left)
    			)
    		)
    		(property "Footprint" ""
    			(at 5.08 2.54 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "P-MOSFET transistor"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "PMOS P-MOS"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "Q_PMOS_0_1"
    			(polyline
    				(pts
    					(xy 0.254 1.905) (xy 0.254 -1.905)
    				)
    				(stroke
    					(width 0.254)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0.254 0) (xy -2.54 0)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0.762 2.286) (xy 0.762 1.27)
    				)
    				(stroke
    					(width 0.254)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0.762 1.778) (xy 3.302 1.778) (xy 3.302 -1.778) (xy 0.762 -1.778)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0.762 0.508) (xy 0.762 -0.508)
    				)
    				(stroke
    					(width 0.254)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0.762 -1.27) (xy 0.762 -2.286)
    				)
    				(stroke
    					(width 0.254)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(circle
    				(center 1.651 0)
    				(radius 2.794)
    				(stroke
    					(width 0.254)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 2.286 0) (xy 1.27 0.381) (xy 1.27 -0.381) (xy 2.286 0)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type outline)
    				)
    			)
    			(polyline
    				(pts
    					(xy 2.54 2.54) (xy 2.54 1.778)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(circle
    				(center 2.54 1.778)
    				(radius 0.254)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type outline)
    				)
    			)
    			(circle
    				(center 2.54 -1.778)
    				(radius 0.254)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type outline)
    				)
    			)
    			(polyline
    				(pts
    					(xy 2.54 -2.54) (xy 2.54 0) (xy 0.762 0)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 2.921 -0.381) (xy 3.683 -0.381)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 3.302 -0.381) (xy 2.921 0.254) (xy 3.683 0.254) (xy 3.302 -0.381)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "Q_PMOS_1_1"
    			(pin passive line
    				(at 2.54 5.08 270)
    				(length 2.54)
    				(name "D"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "D"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin input line
    				(at -5.08 0 0)
    				(length 2.54)
    				(name "G"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "G"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin passive line
    				(at 2.54 -5.08 90)
    				(length 2.54)
    				(name "S"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "S"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "Device:Speaker"
    		(pin_names
    			(offset 0)
    			(hide yes)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "LS"
    			(at 1.27 5.715 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    				(justify right)
    			)
    		)
    		(property "Value" "Speaker"
    			(at 1.27 3.81 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    				(justify right)
    			)
    		)
    		(property "Footprint" ""
    			(at 0 -5.08 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at -0.254 -1.27 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Speaker"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "speaker sound"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "Speaker_0_0"
    			(rectangle
    				(start -2.54 1.27)
    				(end 1.016 -3.81)
    				(stroke
    					(width 0.254)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 1.016 1.27) (xy 3.556 3.81) (xy 3.556 -6.35) (xy 1.016 -3.81)
    				)
    				(stroke
    					(width 0.254)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "Speaker_1_1"
    			(pin input line
    				(at -5.08 0 0)
    				(length 2.54)
    				(name "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin input line
    				(at -5.08 -2.54 0)
    				(length 2.54)
    				(name "2"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "2"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "Switch:SW_SPDT"
    		(pin_names
    			(offset 0)
    			(hide yes)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "SW"
    			(at 0 5.08 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Value" "SW_SPDT"
    			(at 0 -5.08 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Footprint" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 -7.62 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Switch, single pole double throw"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "switch single-pole double-throw spdt ON-ON"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "SW_SPDT_0_1"
    			(circle
    				(center -2.032 0)
    				(radius 0.4572)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy -1.651 0.254) (xy 1.651 2.286)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(circle
    				(center 2.032 2.54)
    				(radius 0.4572)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(circle
    				(center 2.032 -2.54)
    				(radius 0.4572)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "SW_SPDT_1_1"
    			(rectangle
    				(start -3.175 3.81)
    				(end 3.175 -3.81)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type background)
    				)
    			)
    			(pin passive line
    				(at 5.08 2.54 180)
    				(length 2.54)
    				(name "A"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin passive line
    				(at -5.08 0 0)
    				(length 2.54)
    				(name "B"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "2"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    			(pin passive line
    				(at 5.08 -2.54 180)
    				(length 2.54)
    				(name "C"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "3"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "power:GND"
    		(power global)
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 0)
    			(hide yes)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "#PWR"
    			(at 0 -6.35 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Value" "GND"
    			(at 0 -3.81 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Footprint" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Power symbol creates a global label with name \"GND\" , ground"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "global power"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "GND_0_1"
    			(polyline
    				(pts
    					(xy 0 0) (xy 0 -1.27) (xy 1.27 -1.27) (xy 0 -2.54) (xy -1.27 -1.27) (xy 0 -1.27)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "GND_1_1"
    			(pin power_in line
    				(at 0 0 270)
    				(length 0)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "power:+3V3"
    		(power global)
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 0)
    			(hide yes)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "#PWR"
    			(at 0 -3.81 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Value" "+3V3"
    			(at 0 3.556 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Footprint" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Power symbol creates a global label with name \"+3V3\""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "global power"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "+3V3_0_1"
    			(polyline
    				(pts
    					(xy -0.762 1.27) (xy 0 2.54)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0 2.54) (xy 0.762 1.27)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0 0) (xy 0 2.54)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "+3V3_1_1"
    			(pin power_in line
    				(at 0 0 90)
    				(length 0)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "power:+5V"
    		(power global)
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 0)
    			(hide yes)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "#PWR"
    			(at 0 -3.81 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Value" "+5V"
    			(at 0 3.556 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Footprint" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Power symbol creates a global label with name \"+5V\""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "global power"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "+5V_0_1"
    			(polyline
    				(pts
    					(xy -0.762 1.27) (xy 0 2.54)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0 2.54) (xy 0.762 1.27)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    			(polyline
    				(pts
    					(xy 0 0) (xy 0 2.54)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(symbol "+5V_1_1"
    			(pin power_in line
    				(at 0 0 90)
    				(length 0)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
    (symbol "power:PWR_FLAG"
    		(power global)
    		(pin_numbers
    			(hide yes)
    		)
    		(pin_names
    			(offset 0)
    			(hide yes)
    		)
    		(exclude_from_sim no)
    		(in_bom yes)
    		(on_board yes)
    		(in_pos_files yes)
    		(duplicate_pin_numbers_are_jumpers no)
    		(property "Reference" "#FLG"
    			(at 0 1.905 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Value" "PWR_FLAG"
    			(at 0 3.81 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Footprint" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Datasheet" ""
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "Description" "Special symbol for telling ERC where power comes from"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(property "ki_keywords" "flag power"
    			(at 0 0 0)
    			(show_name no)
    			(do_not_autoplace no)
    			(hide yes)
    			(effects
    				(font
    					(size 1.27 1.27)
    				)
    			)
    		)
    		(symbol "PWR_FLAG_0_0"
    			(pin power_out line
    				(at 0 0 90)
    				(length 0)
    				(name ""
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    				(number "1"
    					(effects
    						(font
    							(size 1.27 1.27)
    						)
    					)
    				)
    			)
    		)
    		(symbol "PWR_FLAG_0_1"
    			(polyline
    				(pts
    					(xy 0 0) (xy 0 1.27) (xy -1.016 1.905) (xy 0 2.54) (xy 1.016 1.905) (xy 0 1.27)
    				)
    				(stroke
    					(width 0)
    					(type default)
    				)
    				(fill
    					(type none)
    				)
    			)
    		)
    		(embedded_fonts no)
    	)
"""
