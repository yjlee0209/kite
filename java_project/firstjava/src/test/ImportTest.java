package test;

import java.text.SimpleDateFormat;

public class ImportTest {

	public static void main(String[] args) {
		
		java.util.Date today = new java.util.Date();
		
		System.out.println(today);

		SimpleDateFormat sdf = new SimpleDateFormat("yyyy/MM/dd hh:mm");
		String todayStr = sdf.format(today);

		System.out.println(todayStr);

		
		
	}

}
