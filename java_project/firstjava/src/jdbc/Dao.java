package jdbc;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

// Data Access object : 데이터베이스의 데이터 조작을 위한 클래스
public class Dao {
	
	// 싱글톤 패턴으로 인스턴스 생성을 제한
	
	// 1. 생성자 호출을 막아서 인스턴스 생성을 막는다.
	private Dao() { }
	
	// 2. 사용할 인스턴스를 생성
	private static Dao dao = new Dao();    // Dao.dao = null;
	
	// 3. 외부 참조용 메서드 : 인스턴스를 반환해주는 메서드
	public static Dao getInstance() {
		return dao;
	}
	
	
	
	// 부서정보 리스트 출력
	public void listDept(Connection conn) throws SQLException {
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
	public void insertDept(Connection conn, int deptno, String dname, String loc) throws SQLException {
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

	// 부서정보 수정
	// 부서이름, 부서위치, 부서 선택의 조건 부서번호(PK)로 한다. 
	public void editDept(Connection conn, int deptno, String dname, String loc) throws SQLException {
		
		String sql = "update dept set dname=?, loc=? where deptno=? ";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		pstmt.setString(1, dname);
		pstmt.setString(2, loc);
		pstmt.setInt(3, deptno);
		int rCnt = pstmt.executeUpdate();
		
		if(rCnt>0) {
			System.out.println("수정되었습니다.");
		} else {
			System.out.println("찾으시는 데이터가 존재하지 않습니다.");
		}
		
		
	}
	
	
	
	
	
	
	
	
	
	
	
	


}
