package ver05;

// 상속의 목적 : 추상클래스 -> 인스턴스 생성이 불가
public abstract class PhoneInfor {

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
	
	abstract void showInfor();

	@Override
	public boolean equals(Object obj) {
		
		if(obj != null && obj instanceof PhoneInfor) {
			PhoneInfor pi = (PhoneInfor) obj;
			return phoneNumber.equals(pi.phoneNumber);
		} else {
			return false;
		}
		
	}

	@Override
	public int hashCode() {
		int code = phoneNumber.charAt(phoneNumber.length()-1)%5;
		return code;
	}
	
	
	
	
	
	
	
}
