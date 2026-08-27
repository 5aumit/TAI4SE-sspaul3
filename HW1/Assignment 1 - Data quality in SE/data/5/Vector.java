package primitives;

public class Vector {
	private PointD3 head;

	//Constructors
	public Vector() {
		super();
		head=new PointD3();
		
	}
	public Vector(double x,double y,double z)
	{
		head=new PointD3(x, y, z);
	}
	public Vector(PointD3 head) {
		super();
		this.head =new PointD3(head);
	}
	public Vector(Vector v)
	{
		this.head=new PointD3(v.getHead());
	}

	//getter and setter
	public PointD3 getHead() {
		return head;
	}
	public void setHead(PointD3 head) {
		this.head = new PointD3(head);
	}
	

	public void add(Vector v)
	{
		this.head.add(v);
	}

	public void subtract(Vector v)
	{
		head.subtract(v);
	}

	public void scale(double scalingfactor) {

		head.getX().setX(head.getX().getX()*scalingfactor);
		head.getY().setX(head.getY().getX()*scalingfactor);
		head.getZ().setX(head.getZ().getX()*scalingfactor);
	}
	
	public double lenght()
	{
		double t1=Math.pow(this.head.getX().getX(),2);
		double t2=Math.pow(this.head.getY().getX(),2);
		double t3=Math.pow(this.head.getZ().getX(),2);
		return Math.sqrt(t1+t2+t3);	
	}
	
	public void normalize()
	{
		double length=this.lenght();
		if(length==0)
			throw new ArithmeticException();
		length=1/length;
		head.getX().setX(head.getX().getX()*length);
		head.getY().setX(head.getY().getX()*length);
		head.getZ().setX(head.getZ().getX()*length);	
	}
	
	public Vector crossProduct (Vector vector) {

		double myX=this.getHead().getX().getX();
		double myY=this.getHead().getY().getX();
		double myZ=this.getHead().getZ().getX();
		double vecX=vector.getHead().getX().getX();
		double vecY=vector.getHead().getY().getX();
		double vecZ=vector.getHead().getZ().getX();
		double perx=myY*vecZ-myZ*vecY;
		double pery=myX*vecZ-myZ*vecX;
		double perz=myX*vecY-myY*vecX;
		PointD3 pd3 =new PointD3(new Coordinate(perx),new Coordinate(-1*pery) , new Coordinate(perz));

		Vector v=new Vector(pd3);
		return v;

	}
	
	public double dotProduct(Vector vector) {
		double temp=head.getX().getX()*vector.head.getX().getX()+head.getY().getX()*vector.head.getY().getX()+head.getZ().getX()*vector.head.getZ().getX();
		return temp;
	}

	public  boolean equals(Object v)
	{

		Vector v1=(Vector)v;
		PointD3 p1=new PointD3(v1.getHead());
		PointD3 p2=new PointD3(this.getHead());
		if(p1.equals(p2)==true)
			return true;
		return false;
		//return true;
	}
	
	public String toString()
	{
		return this.getHead().toString();
	}
}





