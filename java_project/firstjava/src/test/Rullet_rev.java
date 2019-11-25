package test;

import java.util.Scanner;

public class Rullet_rev {

	public static void main(String[] args) {
		
		int ran = 0;
		Scanner kb = new Scanner(System.in);
		
		String[]name = {
				"고현주", "구자윤", "김난형", "김동진", "김주연",
				"문영기", "박준섭", "박지은", "방창용", "양햇살",
				"엄예빈", "위은주", "이용재", "이진형", "이택수",
				"장한솔", "정엄지", "정용기", "조지윤", "조성빈",
				"최찬영", "하재운", "홍지수", "황다울"};
		
		System.out.println("제비뽑기를 시작하려면 1을 누르세요");
		int menu = Integer.parseInt(kb.nextLine());
		
		if(menu == 1) {
			ran = (int)(Math.random() * 24);
			System.out.println("축하합니다. 반장은 "+ name[ran] +" 입니다.");
		}
		kb.close();
	}
}
