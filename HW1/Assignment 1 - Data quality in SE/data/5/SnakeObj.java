import java.awt.*;
import java.awt.event.ActionListener;

import javax.swing.*;

public class SnakeObj extends JComponent {
//	 @param length is the length of the snake
//	 @param xHead is the x coordinate of the head of the snake
//	 @param yHead is the y coordinate of the head of the snake
//	 @param xTail is x coordinate of the tail of the snake 
//	 @param yTail is the y coordinate of the tail of the snake 
//	 @param xDir is the x direction the snake is travelling in 1 - right, 0 none -1 left
//	 @param yDir is the y direction the snake is travelling in 1 - down, 0 none, -1 down
//	 @param SnakeArray is a 2D array representing potential locations for the
//	 snake, value of 1 tells us the snake is there, value of 0 tells us snake is not there

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	private static int length;
	private int xHead;
	private int yHead;
	private int xTail;
	private int yTail;
	private static int xDir;
	private static int yDir;
	private final int boardWidth = 100;
	private int[][] SnakeArray = new int[boardWidth][boardWidth];

	public SnakeObj() {
		SnakeObj.length = 3;
		xHead = (int) Math.random() * 100;
		yHead = (int) Math.random() * 100;
		xTail = xHead + length; 
		yTail = yHead + length; 
		xDir = 1;
		yDir = 0;
		for (int i = xHead; i > xHead - length; i--) {
			//handle snake going off the screen to the left or the right 
			if (i < 0) {
				i = boardWidth - 1; 
			} else if (i >= boardWidth) {
				i = 0; 
			}
			for (int j = yHead; j > yHead - length; j--) {
				//handle snake going off the screen at the top or the bottom 
				if (j < 0)  {
					j = boardWidth - 1; 
				} else if (j >= boardWidth) {
					j = 0; 
				}
				SnakeArray[i][j] = 1;
			}
		}
	}

	// increases the length of the snake if it eats food
	public void growSnake() {
		SnakeObj.length++;
		xHead++;
		yHead++; 
		SnakeArray[xHead][yHead] = 1; 
		this.repaint(); 
	}

	// decreases the length of the snake if it eats poison
	public void shrinkSnake() {
		SnakeObj.length--;
		SnakeArray[xTail][yTail] = 0; 
		xTail--;
		yTail--; 
		this.repaint(); 
	}

	// paints the snake
	public void paintComponent(Graphics gc) {
		// draw the head of the snake
		gc.setColor(Color.RED);
		gc.fillRect(xHead * 5, yHead * 5, 5, 5);
		
		gc.setColor(Color.BLACK);
		for (int i = 0; i < SnakeArray.length; i++) {
			for (int j = 0; j < SnakeArray[0].length; j++) {
				if (containsSnake(i, j)) {
					gc.fillRect(i * 5, j * 5, 20, 20);
				}
			}
		}
	}

	// checks the board to see if a snake is in a particular block of the board
	public boolean containsSnake(int xcoord, int ycoord) {
		return (SnakeArray[xcoord][ycoord] == 1);
	}

	public Dimension getPreferredSize() {
		return new Dimension(500, 500);
	}

	public void moveSnake(ActionListener a) {
		// handle collisions
		if (SnakeArray[xHead + xDir][yHead + yDir] == 1) {
			//handle it
		}
		
		// move the snake in the direction specified
		for (int i = xHead; i > xHead - length; i--) {
			for (int j = yHead; j > yHead - length; j--) {	
				
				SnakeArray[i][j] = 1;
				SnakeArray[i][j] = 0;
			}
		}
		// repaint the snake
		this.repaint();
	}

}

