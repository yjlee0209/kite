package com.kite.jdbc.dao;

import java.util.List;

import com.kite.jdbc.domain.Member;
import com.kite.jdbc.domain.RequestMemberReg;

public interface MemberDaoInterface {
	
	//  전체 리스트
	public List<Member> getMemberList();
	
	// ID로 검색
	public Member getMemberById(Integer id);
	
	// Email로 검색
	public Member getMemberByEmail(String email);
	
	// 회원 정보 입력
	public int insertMember(RequestMemberReg request);
	
	
}
