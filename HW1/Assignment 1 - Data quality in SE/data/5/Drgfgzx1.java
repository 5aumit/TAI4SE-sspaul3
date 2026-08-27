package bean.zk;

import java.sql.Timestamp;
import java.util.Date;

import bean.Device;

import com.mysql.fabric.xmlrpc.base.Data;

public class Drgfgzx1 {

	private	int id;
	private	String one;
	private	String two;
	private	String three;
	private	String four;
	private	String five;
	private	String six;
	private	String seven;
	private	String eight;
	private	String nine;   
	private	String beizhu;
	private	String lururen;
	private	String bumen;
	private Device device_id;
	private	Timestamp   lurushijian;
	
	

	public Drgfgzx1() {
		super();
	}


	
	

	public Drgfgzx1(String one, String two, String three, String four,
			String five, String six, String seven, String eight, String nine,
			String beizhu, String lururen, String bumen, Device device_id,
			Timestamp lurushijian) {
		super();
		this.one = one;
		this.two = two;
		this.three = three;
		this.four = four;
		this.five = five;
		this.six = six;
		this.seven = seven;
		this.eight = eight;
		this.nine = nine;
		this.beizhu = beizhu;
		this.lururen = lururen;
		this.bumen = bumen;
		this.device_id = device_id;
		this.lurushijian = lurushijian;
	}





	public int getId() {
		return id;
	}



	public void setId(int id) {
		this.id = id;
	}



	public String getOne() {
		return one;
	}



	public void setOne(String one) {
		this.one = one;
	}



	public String getTwo() {
		return two;
	}



	public void setTwo(String two) {
		this.two = two;
	}



	public String getThree() {
		return three;
	}



	public void setThree(String three) {
		this.three = three;
	}



	public String getFour() {
		return four;
	}



	public void setFour(String four) {
		this.four = four;
	}



	public String getFive() {
		return five;
	}



	public void setFive(String five) {
		this.five = five;
	}



	public String getSix() {
		return six;
	}



	public void setSix(String six) {
		this.six = six;
	}



	public String getSeven() {
		return seven;
	}



	public void setSeven(String seven) {
		this.seven = seven;
	}



	public String getEight() {
		return eight;
	}



	public void setEight(String eight) {
		this.eight = eight;
	}



	public String getNine() {
		return nine;
	}



	public void setNine(String nine) {
		this.nine = nine;
	}



	public String getBeizhu() {
		return beizhu;
	}



	public void setBeizhu(String beizhu) {
		this.beizhu = beizhu;
	}



	public String getLururen() {
		return lururen;
	}



	public void setLururen(String lururen) {
		this.lururen = lururen;
	}



	public String getBumen() {
		return bumen;
	}



	public void setBumen(String bumen) {
		this.bumen = bumen;
	}



	public Device getDevice_id() {
		return device_id;
	}



	public void setDevice_id(Device device_id) {
		this.device_id = device_id;
	}



	public Date getLurushijian() {
		return lurushijian;
	}



	public void setLurushijian(Timestamp lurushijian) {
		this.lurushijian = lurushijian;
	}
	
	
	

	
	
	
	
	
	
}
