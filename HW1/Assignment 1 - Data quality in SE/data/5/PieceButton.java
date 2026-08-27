import javax.swing.AbstractButton;
import javax.swing.JButton;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;


public class PieceButton extends JButton {
	private Piece piece;
	private int x, y;

	public PieceButton(Piece piece, int x, int  y) {
		super();
		this.x = x;
		this.y = y;
		this.piece = piece;
		piece.setButton(this);
		if(piece.getType() != 0)
			this.setText("" + piece.getType());
	}

	public int getArrayX(){
		return x;
	}
	public int getArrayY(){
		return y;
	}
	
	public int getType(){
		return piece.getType();
	}
	public Piece getPiece() {
		return piece;
	}

	public void setPiece(Piece piece) {
		this.piece = piece;
		this.update();
	}
	public void update(){
		if(piece.getType() != 0){
			this.setText("" + piece.getType());
		}else{
			this.setText("");
		}
	}
	
	public int getPosition()
	{
		return (y * 10) + x + 1; //fix constant value
	}
}
