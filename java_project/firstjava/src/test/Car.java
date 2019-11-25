package test;

public class Car {
	int gasolinegauge;

	public Car(int gasolinegauge) {
		//super();  // Object()
		this.gasolinegauge = gasolinegauge;
	}
	
}

class HybridCar extends Car {
	int electronicGauge;

	public HybridCar(int gasolinegauge) {
		super(gasolinegauge);
	}

	public HybridCar(int gasolinegauge, int electronicGauge) {
		super(gasolinegauge);
		this.electronicGauge = electronicGauge;
	}

}

class HybridWaterCar extends HybridCar {
	int waterGauge;
		
	public HybridWaterCar(int gasolinegauge, int electronicGauge, int waterGauge) {
		super(gasolinegauge/*, electronicGauge*/);
		this.waterGauge = waterGauge;
	}



	public void showCurrentGauge() {
	System.out.println("잔여 가솔린 : " + gasolinegauge);
	System.out.println("잔여 가솔린 : " + electronicGauge);
	System.out.println("잔여 가솔린 : " + waterGauge);
	}
}
	
	

