package ver01;

public class PhoneInfor {

	// 이름             name            String
	// 전화번호       phoneNumber     String
	// 생년월일       birthday        String 
	public String name;
	public String phoneNumber;		// 010 으로 시작해서 숫자타입 불가, 맨앞 0을 빼면 가능
	public String birthday;        // 2019-11-12 형식으로 저장

	// 데이터 초기화
	public PhoneInfor(String name, String phoneNumber, String birthday){
		this.name = name;
		this.phoneNumber = phoneNumber;
		this.birthday = birthday;
	}
	// 오버로딩
	public PhoneInfor(String name, String phoneNumber){
		this(name, phoneNumber, null);  //다른(오버로딩 된) 생성자 호출
 	}
	
	// 데이터 출력하는 메서드
	public void showInfo() {
		System.out.println("이름 : " + name);
		System.out.println("전번 : " + phoneNumber);
		if(birthday == null) {
			System.out.println("생일 : 입력된 데이터가 없습니다");	
		}else {
			System.out.println("생일 : " + birthday);	
		}
	}
	
	
	
}
