package test;

import java.util.HashSet;
import java.util.Iterator;

public class SimpleNumber {

	int num;

	public SimpleNumber(int num) {
		this.num = num;
	}

	// hashCode 생성 : Object 클래스의 hashCode() 오버라이딩
	@Override
	public int hashCode() {
		return num % 3;
	}

	// equals() 오버라이딩
	@Override
	public boolean equals(Object obj) {

		boolean result = false;

		if (obj != null && obj instanceof SimpleNumber) {
			SimpleNumber sNum = (SimpleNumber) obj;
			if (sNum.num == num) {
				result = true;
			}
		}
		return result;
	}

	@Override
	public String toString() {
		return "SimpleNumber [num=" + num + "]";
	}

	public static void main(String[] args) {
		HashSet<SimpleNumber> hSet = new HashSet<SimpleNumber>();

		hSet.add(new SimpleNumber(10));
		hSet.add(new SimpleNumber(20));
		hSet.add(new SimpleNumber(10));

		System.out.println("저장된 데이터의 개수 : " + hSet.size());
		
		Iterator<SimpleNumber> itr = hSet.iterator();
		
		while(itr.hasNext()) {
			System.out.println(itr.next());
		}
	}

}
