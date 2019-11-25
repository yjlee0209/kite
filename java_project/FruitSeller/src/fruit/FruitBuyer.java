package fruit;

public class FruitBuyer {

	// 상태 값 : 보유 금액, 사과의 개수
//	int myMoney = 10000;     // 보유 금액 : 초기값은 10000
//	int numofApple = 0;      // 보유한 사과의 개수 : 초기값은 0
	
	private int myMoney;     
	private int numofApple;      
	
	public FruitBuyer(int money) {
		myMoney = money;
	}
	
	// 기능 : 구매, 구매 현황	

	// 구매 : 구매할 셀러, 구매할 금액 -> 셀러에게 판매요청(금액) -> 반환 받은 사과의 개수로 보유한 사과의 개수 변경 -> 보유한 금액 변경
	public void buyApple(FruitSeller seller, int money) {
		// 구매한 사과의 개수(num)
		int num = seller.saleApple(money);
		//numofApple = numofApple + num;
		numofApple += num;    // 사과의 개수 변경
		myMoney -= money;     // 보유한 금액 변경
		
	}
	
	public void showBuyResult() {
		System.out.println("현재 보유 금액 : " + myMoney);
		System.out.println("사과의 개수 : " + numofApple);
	}
	
}
