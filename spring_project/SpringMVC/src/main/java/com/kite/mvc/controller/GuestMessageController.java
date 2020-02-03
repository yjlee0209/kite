package com.kite.mvc.controller;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.kite.mvc.domain.GuestMessage;
import com.kite.mvc.domain.GuestMessageList;
import com.kite.mvc.domain.GuestMessageList2;

@Controller
public class GuestMessageController {

	@RequestMapping("/guestmessage/list.xml")
	@ResponseBody
	public GuestMessageList listXml() {
		return getMessageList();
	}
	
	@RequestMapping("/guestmessage/list.json")
	@ResponseBody
	public GuestMessageList2 listJson() {
		return getMessageList2();
	}

	private GuestMessageList getMessageList() {
		
		List<GuestMessage> message = new ArrayList<GuestMessage>();
		message.add(new GuestMessage(1, "메시지", new Date()));
		message.add(new GuestMessage(2, "메시지", new Date()));
		message.add(new GuestMessage(3, "메시지", new Date()));
		
		
		return new GuestMessageList(message);
	}
	
	private GuestMessageList2 getMessageList2() {
		
		List<GuestMessage> message = new ArrayList<GuestMessage>();
		message.add(new GuestMessage(1, "메시지", new Date()));
		message.add(new GuestMessage(2, "메시지", new Date()));
		message.add(new GuestMessage(3, "메시지", new Date()));
		
		
		return new GuestMessageList2(message);
	}
	
}
