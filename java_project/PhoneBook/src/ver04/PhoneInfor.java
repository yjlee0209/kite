package ver04;

// 상속의 목적
public class PhoneInfor {

	//	이름             name             String
	//	전화번호       phoneNumber      String
	//	이메일          email            String
	String name;
	String phoneNumber;
	String email;
	
	// 생성자 : 초기화 메서드
	// 기본 데이터 초기화
	public PhoneInfor(String name, String phoneNumber, String email) {
		super();
		this.name = name;
		this.phoneNumber = phoneNumber;
		this.email = email;
	}
	
	void showBasicInfor() {
		System.out.println("이름 : " + this.name);
		System.out.println("전번 : " + this.phoneNumber);
		System.out.println("이멜 : " + this.email);
	}
	
	void showInfor() {}
	
	
}
