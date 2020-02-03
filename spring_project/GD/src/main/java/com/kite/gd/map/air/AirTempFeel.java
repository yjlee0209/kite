package com.kite.gd.map.air;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class AirTempFeel {

	@RequestMapping("/air/tempFeel")
	public String tempf() {
		
		String tempf = "air/tempFeel";
		
		return tempf;
	}
		
	
	
}
