package com.kite.jdbc.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.kite.jdbc.domain.Member;
import com.kite.jdbc.domain.RequestMemberReg;
import com.kite.jdbc.service.MemberRegService;

@Controller
@RequestMapping("/member/reg")
public class MemberRegController {
	
	@Autowired
	MemberRegService service;

	@RequestMapping(method = RequestMethod.GET)
	public String getRegForm() {
		return "member/regForm";
	}

	@RequestMapping(method = RequestMethod.POST)
	public String MemberReg(RequestMemberReg request, Model model) {
		
		System.out.println(request);
		
		model.addAttribute("result", service.regMember(request));
		
		return "member/reg";
	}
	
	
	
}
