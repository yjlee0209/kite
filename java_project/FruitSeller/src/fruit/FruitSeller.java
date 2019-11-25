package fruit;

public class FruitSeller {

	// 상태값 : 사과의 개수, 수익금, 사과의 가격
//	int numofApple = 20;  // 사과의 개수
//	int myMoney = 0;      // 판매 금액
//	final int APPLE_PRICE = 1000;  // 사과 1개의 금액
	
	private int numofApple;  // 사과의 개수
	private int myMoney;      // 판매 금액
	final int APPLE_PRICE;  // 사과 1개의 금액

	// 생성자 만들기
	// 이름은 클래스 이름과 동일하게, 메서드와 같이 매개변수를 정의 할 수 있다.
	// return이 없다, 반환형 타입을 정의하지 않는다.
	// 인스턴스 생성시에 단 한번 실행 -> 멤버 변수의초기화 할깨 사용 : 초기화 메서드 
	// 디폴트 생성자는 생략 가능

	public FruitSeller(int numofApple, int myMoney, int aPPLE_PRICE) {	   // 생성자
		this.numofApple = numofApple;
		this.myMoney = myMoney;
		APPLE_PRICE = aPPLE_PRICE;
	}	
	
	public FruitSeller(FruitSeller fs) {
		this.numofApple = fs.numofApple;
		this.myMoney = fs.myMoney;
		this.APPLE_PRICE = fs.APPLE_PRICE;
	}
	
	public FruitSeller() {
		this(20, 0, 500);   // 다른 생성자 호출; 기준(매개변수)
	}
	


	// 기능 : 판매, 판매 데이터 출력
	
	// 판매 기능 : 돈을 받고 -> 사과의 개수를 계산 -> 사과의 개수를 변경 -> 돈의 수치 변경 -> 사과의 개수를 변환
	
	
	int saleApple(int money) {
		// 판매한 사과의 개수
		int num = money / APPLE_PRICE;
		numofApple = numofApple - num;   // 보유한 사과의 개수 변경
		myMoney = myMoney + money;       // 보유한 돈의 데이터 변경
		return num;
	}
	
	// 판매 결과를 출력
	public void showSaleResult() {
		System.out.println("남은 사과의 개수 : " + numofApple);
		System.out.println("판매 수익 : " + myMoney);		
	}
	
	
	
	
	
}
