package ver01;

public class PhoneBookMain {

	public static void main(String[] args) {
		
		// 데이터 저장 : 인스턴스 생성
		PhoneInfor pi_1 = new PhoneInfor("홍길동", "010-1234-5678", "2000-01-01");		
		pi_1.showInfo();
		
		PhoneInfor pi_2 = new PhoneInfor("임꺽정", "010-8765-4321");		
		pi_2.showInfo();
		
		
	}

}
