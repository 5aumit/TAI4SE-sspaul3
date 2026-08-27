package component.renderable;

import message.CMessage;
import message.Message;

import org.newdawn.slick.Color;
import org.newdawn.slick.GameContainer;
import org.newdawn.slick.Graphics;
import org.newdawn.slick.state.StateBasedGame;

import component.CHealth;

public class CHealthDisplay extends CRenderable {
	
	CHealth health = new CHealth();
	
	public CHealthDisplay(){
		this.id = "HealthDisplay";
	}

	@Override
	public void setDimensions() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void render(GameContainer gc, StateBasedGame sb, Graphics gr) {
		gr.setColor(Color.red);
		gr.fillRect(owner.getPosition().getX(), owner.getPosition().getY() - 20, health.getHealth()*40/100, 5);
		
	}

	@Override
	public void setDependencies() {
		this.health = (CHealth) owner.getComponent("Health");
		
	}

	@Override
	public void readMessage(Message message) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void readMessage(CMessage message) {
		if (message.getText() == "ComponentAdded"){
			if (message.getSource().getId() == "Health") this.health = (CHealth) message.getSource();
		}
	}

	@Override
	public void update(GameContainer gc, StateBasedGame sb, int delta) {
		// TODO Auto-generated method stub
		
	}
	
	

}
