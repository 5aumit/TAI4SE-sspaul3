package main.Menu;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.ImageObserver;

import main.Game;
import main.Audio.SoundPlayer;

public abstract class MenuButton implements ImageObserver {

	Game game;
	String tag;
	int x, y, width, height;
	Image sprite;
	String soundFile;
	
	public MenuButton(Game game, int x, int y, Image image){
		this.game = game;
		this.x = x;
		this.y = y;
		this.sprite = image;
		this.width = sprite.getWidth(this);
		this.height = sprite.getHeight(this);
	}
	
	public boolean isClicked(int mX, int mY){
		
		if(mX >= x && mX < x+width && mY >= y && mY <= y+height){
			return true;
		}
		return false;
	}
	
	public abstract void function();

	public void render(Graphics g) {
		g.drawImage(sprite, x, y, this);		
	}
	
	@Override
	public boolean imageUpdate(Image img, int infoflags, int x, int y, int width, int height) {
		return false;
	}
	
	public void playSound(){
		try{
			SoundPlayer.playSound(soundFile);
		}catch (NullPointerException e){
			System.out.println("Sound file missing");
		}
	}
	
}
