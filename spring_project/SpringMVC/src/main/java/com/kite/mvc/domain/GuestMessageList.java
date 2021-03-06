package com.kite.mvc.domain;

import java.util.List;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlRootElement(name = "message-list")
public class GuestMessageList {

	@XmlElement(name = "message")
	private List<GuestMessage> message;

	public GuestMessageList(List<GuestMessage> message) {
		this.message = message;
	}

	public GuestMessageList() {
	
	}

	public List<GuestMessage> getMessage() {
		return message;
	}

	public void setMessage(List<GuestMessage> message) {
		this.message = message;
	}
	
	
	
	
	
}
