
package com.kite.gd.map.weather;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class WeatherController {

	@RequestMapping("/weather/weather")
	public String temp() {

		String weather = "weather/weather";

		return weather;
	}

}
