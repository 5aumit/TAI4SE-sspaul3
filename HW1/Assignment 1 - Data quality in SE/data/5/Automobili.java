package automobili;

public class Automobili {
	private String marka;
	private String model;
	private String pogonskoGorivo;
	private int brojVrata;
	private int godinaProizvodnje;
	private double potrosnjaNaStoKilometara;
	
	public Automobili(String marka, String model, String pogonskoGorivo, int brojVrata, int godinaProizvodnje, double potrosnja) {
		this.marka = marka;
		this.model = model;
		this.pogonskoGorivo = pogonskoGorivo;
		this.brojVrata = brojVrata;
		this.godinaProizvodnje = godinaProizvodnje;
	}
	
	public Automobili() {
		
	}
	
		
	public double getPotrosnjaNaStoKilometara() {
		return potrosnjaNaStoKilometara;
	}

	public void setPotrosnjaNaStoKilometara(double potrosnjaNaStoKilometara) {
		this.potrosnjaNaStoKilometara = potrosnjaNaStoKilometara;
	}
		
	public String getMarka() {
		return marka;
	}
	
	public String getModel() {
		return model;
	}

	public void racunanjePotrosnje() {
		if (this.brojVrata == 3) {
			setPotrosnjaNaStoKilometara(5);
		} else if (this.brojVrata == 5) {
			setPotrosnjaNaStoKilometara(6);
		}
	}
	
	public void stampaOAutomobilima() {
		System.out.println("Automobil " + this.marka + " " + this.model + " ide na " + this.pogonskoGorivo +
				", ima " + this.brojVrata + " vrata i proizveden je " + this.godinaProizvodnje + ". godine.");
	}
	
	

}
