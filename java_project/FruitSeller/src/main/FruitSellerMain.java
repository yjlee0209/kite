package main;

import fruit.FruitBuyer;
import fruit.FruitSeller;

public class FruitSellerMain {

	public static void main(String[] args) {
		
		// 셀러1 생성
		FruitSeller seller;  // 참조 변수 생성 : 인스턴스의 주소를 저장
		//seller = new FruitSeller(0,30,1500);  // 인스턴스 생성 -> 인스턴스 메모리에 주소값을 반환
		seller = new FruitSeller();
		
		// 셀러2 생성
		//FruitSeller seller2 = new FruitSeller(0, 10, 1000);
		FruitSeller seller2 = new FruitSeller(seller);
		
		// 바이어 생성
		FruitBuyer buyer = new FruitBuyer(10000);

		// 구매자가 5000원 어치 사과를 구매
		buyer.buyApple(seller, 3000);
		buyer.buyApple(seller2, 3000);
		
		System.out.println("판매자1의 현재 상황");
		seller.showSaleResult();
		System.out.println("........................");
		System.out.println("판매자2 현재 상황");
		seller2.showSaleResult();
		
		System.out.println("========================");
		
		System.out.println("구매자의 현재 상황");
		buyer.showBuyResult();
		
	}

}
