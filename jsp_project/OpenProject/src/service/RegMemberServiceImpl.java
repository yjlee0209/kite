package service;

import java.sql.Connection;
import java.sql.SQLException;

import javax.servlet.http.HttpServletRequest;

import dao.MemberDao;
import jdbc.ConnectionProvider;
import model.OpMember;

public class RegMemberServiceImpl implements MemberService {

	@Override
	public String process(HttpServletRequest request) {
	
		// 사용자 요청 데이터를 받는다.
		// DAO에 저장 요청 -> DAO 클래스 생성, 기능 메서드를 생성
		// Connection 객체를 생성해서 메서드에 전달
		// DAO의 응답은 처리 횟수 : 결과 데이터 -> view 전달 request에 저장
		// view 응답 데이터를 받아서 
		
		String viewPage = "/WEB-INF/memberReg.jsp";
		
		// 데이터 받기
		String uid = request.getParameter("uid");
		String pw = request.getParameter("pw");
		String uname = request.getParameter("uname");
		String byear = request.getParameter("byear");
		String gender = request.getParameter("gender");
		String uphoto = request.getParameter("pfile");
		
		OpMember member = new OpMember(0, uid, pw, uname, Integer.parseInt(byear), gender, uphoto);
		
		Connection conn = null;
		int resultCnt = 0;
		
		MemberDao dao = new MemberDao();
		
		try {
			conn = ConnectionProvider.getConnection();
			
			resultCnt = dao.insertMember(conn, member);
			
		} catch(SQLException se) {
			resultCnt = -1;
		}
		
		request.setAttribute("resultCnt", resultCnt);
		
		
		
		
		return null;
	}

}
