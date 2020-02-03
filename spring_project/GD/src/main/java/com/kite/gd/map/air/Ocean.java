package com.kite.gd.map.air;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class Ocean {

	@RequestMapping("/ocean/ocean")
	public String ocean() {
		
		String ocean = "ocean/ocean";
		
		return ocean;
	}
			
		
		
	
	
}
