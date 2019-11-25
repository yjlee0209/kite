package test;

import java.util.HashSet;
import java.util.Iterator;

public class HashSetTest {

	public static void main(String[] args) {
	
		HashSet<String> hSet = new HashSet<String>();
		
		// 데이터 저장 : add
		hSet.add("First");
		hSet.add("Second");
		hSet.add("Third");
		hSet.add("First");
		hSet.add("Third");
	
		System.out.println("저장된 데이터의 개수 : " + hSet.size());
	
		Iterator<String> itr = hSet.iterator();
		
		while(itr.hasNext()) {
			System.out.println(itr.next());
		}
	}

}
