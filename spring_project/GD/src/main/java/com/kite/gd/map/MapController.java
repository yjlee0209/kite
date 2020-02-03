package com.kite.gd.map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MapController {

	@RequestMapping("/map/map")
	public String map() {
		
		String map = "map/map";
		
		return map;
	}
	
}
