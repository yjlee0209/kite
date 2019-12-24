package service;

import java.sql.Connection;
import java.sql.SQLException;

import javax.servlet.http.HttpServletRequest;

import dao.MemberDao;
import jdbc.ConnectionProvider;
import model.OpMember;

public class EditFormMemberService implements MemberService {

	@Override
	public String process(HttpServletRequest request) {
		
		String viewPage = "/WEB-INF/views/editForm.jsp";
		
		String idx = request.getParameter("midx");
		
		OpMember member = null;
		
		Connection conn = null;
		
		MemberDao dao = new MemberDao();
		
		try {
			conn = ConnectionProvider.getConnection();
			
			member = dao.selecyByIdx(conn, Integer.parseInt(idx));
			
		} catch (SQLException e) {
			
			e.printStackTrace();
		}
		
		request.setAttribute("member", member);
		
		
		return viewPage;
	}

}
