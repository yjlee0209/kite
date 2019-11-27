package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCTest3 {

	public static void main(String[] args) {

		Connection conn = null;

		try {
			// 1. 드라이버 로드
			Class.forName("oracle.jdbc.driver.OracleDriver");
			System.out.println("오라클 드라이버 로드 완료");

			// 호스트, port, db name
			String jdbcUrl = "jdbc:oracle:thin:@localhost:1521:orcl";
			// 계정
			String user = "scott";
			// 비밀번호
			String pw = "tiger";

			// 2. 데이터베이스에 접속
			conn = DriverManager.getConnection(jdbcUrl, user, pw);

			System.out.println("데이터베이스에 정상적으로 접속되었습니다.");
			
			//conn.setAutoCommit(false);
			
			// 3. 데이터의 검색과 변경처리 : select / DML
			
			Dao dao = Dao.getInstance();
			
			
			// 부서 정보 입력
			//dao.insertDept(conn, 90, "design", "seoul");
			
			// 부서 정보 수정
			dao.editDept(conn, 80, "MARKETING", "NEWYORK");
			dao.editDept(conn, 60, "MARKETING", "NEWYORK");
			
			// 부서 리스트 출력
			dao.listDept(conn);
			
			
			
			
			
			
			
			//conn.close();
			
			
			
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
			//System.out.println("입력오류!");
		}	

	}
/*	
	// 부서정보 리스트 출력
	public static void listDept(Connection conn) throws SQLException {
		Statement stmt = conn.createStatement();
	
		String sql1 = "select * from dept";
	
		ResultSet rs = stmt.executeQuery(sql1);
		
		System.out.println("부서(DEPT) 리스트");
		System.out.println("-------------------------");
		
		while(rs.next()) {
			
//			int deptno = rs.getInt("deptno");
//			String dname = rs.getString("dname");
//			String loc = rs.getString("loc");
			int deptno = rs.getInt(1);
			String dname = rs.getString(2);
			String loc = rs.getString(3);

			System.out.println(deptno + " | " + dname + " | " + loc);
			
		}
		System.out.println("-------------------------");
		
		rs.close();
		stmt.close();
		
	}
	
	// DB 부서정보 입력
	public static void insertDept(Connection conn, int deptno, String dname, String loc) throws SQLException {
		// SQL
		String sql = "insert into dept(deptno, dname, loc) values (?,?,?)";
		
		// PreparedStatement
		PreparedStatement pstmt = conn.prepareStatement(sql);
		
		// Mapping
		pstmt.setInt(1, deptno);
		pstmt.setString(2, dname);
		pstmt.setString(3, loc);
		
		// executeUpdate
		int rCnt = pstmt.executeUpdate();
		if(rCnt>0) {
			System.out.println("데이터 입력이 정상적으로 처리되었습니다.");
		} else {
			System.out.println("입력이 되지 않았습니다. 관리자에게 문의하세요.");
		}

		pstmt.close();
		
		
	}
*/	
	
	
	
	

}
