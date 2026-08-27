package cf222jf_lab3;

public class Point {
	private int x;
	private int y;


	public Point(int x1, int y1){
		x = x1;
		y = y1;
		}
	public Point(){
		x = 0;
		y = 0;
		}


	public boolean isEqualTo(Point p2){
		boolean answer = false;
		if (p2.x == this.x && p2.y == this.y){
			answer = true;
			
		}
		return answer;

	}
	
	public String toString(){
		String p = "(" + x+','+y+")";
		return p;
	}
	
	public double distanceTo(Point p2){
		double distance = Math.sqrt( Math.pow(this.x-p2.x,2) + Math.pow(this.y-p2.y,2));
		return distance;
		
	}
	public void move(int X, int Y){
		this.x = this.x + X;
		this.y = this.y + Y;
				
	}
	public void moveToXY(int X, int Y){
		this.x = X;
		this.y = Y;
		
	}
}
