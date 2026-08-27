package com.custardgames.framework.entities;

import com.custardgames.framework.Game;
import com.custardgames.framework.level.LevelHandler;
import com.custardgames.framework.level.tile.special.SpawnTile;

public abstract class Mob extends Sprite
{
	public int maxJump;
	public int currentJump;
	public boolean isJumping;
	public boolean facingRight;
	public SpawnTile spawnPoint;
	
	public boolean isAttacked;
	public int deathDelayCounter;
	public final int deathDelay = 2;
	
	public String soundPlaying;
	
	public Mob(LevelHandler level)
	{
		super(level);
		willBlock = true;
		fixed = false;
		isAttacked = false;
		deathDelayCounter = 0;
		maxJump = 0;
		reset();
	}
	
	public void reset()
	{
		super.reset();
		isJumping = false;
		currentJump = 0;
		soundPlaying = "";
	}
	
	public void setSpawn(SpawnTile spawnPoint)
	{
		this.spawnPoint.turnOff();
		this.spawnPoint = spawnPoint;
	}

	public void setMaxJump(double maxJump)
	{
		this.maxJump = (int) (maxJump * Game.ticksPerSecond);
	}

	public void jump(boolean keyPressed)
	{
		if (keyPressed)
		{
			if (currentJump < maxJump)
			{
				if (downCollision)
				{
					isJumping = true;
					currentVelocityY = 0;
				}
				currentJump++;
			}
			else
			{
				isJumping = false;
			}
		}
		else
		{
			isJumping = false;

			if (downCollision)
				currentJump = 0;
			else
				currentJump = maxJump;
		}

		if (isJumping)
			yDir = -1;
		else
			yDir = 0;
	}

	public void tick()
	{
		super.tick();
		tryToKill();
	}
	
	public void die()
	{
		reset();
		running = false;
	}
	
	public void tryToKill()
	{
		if (isAttacked == true)
			deathDelayCounter++;
		else
			deathDelayCounter = 0;
		
		if (deathDelayCounter >= deathDelay)
			die();
		
		isAttacked = false;
	}
	
	public void playSound(String id)
	{
		if (id != null)
		{
			level.soundHandler.playSound(id);
		}

	}
	
	public void changeSound(String id)
	{
		if (id == null)
		{
			level.soundHandler.stopSound(soundPlaying);
			soundPlaying = "";
		}
		else if (!soundPlaying.equals(id))
		{
			level.soundHandler.stopSound(soundPlaying);
			soundPlaying = id;
			level.soundHandler.playSoundLoop(soundPlaying);
		}
	}
	
	public void spawn()
	{
		setCenter(spawnPoint.getCenterX(), spawnPoint.getCenterY());
		running = true;
	}
}
