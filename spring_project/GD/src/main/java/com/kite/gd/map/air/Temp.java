package com.kite.gd.map.air;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class Temp {

	@RequestMapping("/air/temp")
	public String temp() {
		
		String temp = "air/temp";
		
		return temp;
	}
		
	
	
}
