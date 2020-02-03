package com.kite.gd.map.weather;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.client.RestTemplate;

@Controller
public class WeatherController2 {

	
	@CrossOrigin
	@RequestMapping("/weather/weather2")
	public String getInfo(Model model) throws UnsupportedEncodingException {
		
		RestTemplate restTemplate = new RestTemplate();
		String appkey = "l7xx9cff6a0f1f314d908904d1e97b8d86db";
		String dcodeKey = URLDecoder.decode(appkey, "UTF-8");
		
		String url = "http://apis.openapi.sk.com/weather/current/minutely"
				+ "?version=2"
				+ "&city=서울"
				+ "&county=강서구"
				+ "&village=화곡동"
				+ "&appKey=" + appkey;
		
		String result = restTemplate.getForObject(url, String.class);
		
		model.addAttribute("result", result);
		
		return "weather/weather2";
		
	}
}
