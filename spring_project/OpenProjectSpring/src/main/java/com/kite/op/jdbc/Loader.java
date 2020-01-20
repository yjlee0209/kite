package com.kite.op.jdbc;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;


public class Loader extends HttpServlet {

	public void init(ServletConfig config) throws ServletException {
		
		String jdbcDriver = config.getInitParameter("jdbcDriver");
		
		try {
			//데이터베이스 드라이버 로드
			Class.forName(jdbcDriver);
			System.out.println("데이터베이스 드라이버 로드에 성공하였습니다!");
		} catch (ClassNotFoundException cne) {
			System.out.println("데이터베이스 드라이버 로드에 실패하였습니다!");
			cne.printStackTrace();
		}
		
		
		
		
		
	}

}
