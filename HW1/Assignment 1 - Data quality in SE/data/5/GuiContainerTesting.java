package com.curle.ddock.gui;

import com.curle.ddock.block.container.ContainerTesting;
import com.curle.ddock.block.tile.TileEntityContainerTesting;
import com.curle.ddock.utility.Utils;

import net.minecraft.client.gui.inventory.GuiContainer;
import net.minecraft.util.ResourceLocation;

public class GuiContainerTesting extends GuiContainer {
	
	public static final int WIDTH = 180;
	public static final int HEIGHT = 152;
	
	private static final ResourceLocation background = new ResourceLocation(Utils.MODID, "textures/gui/containertesting.png");
	
	public GuiContainerTesting(TileEntityContainerTesting te, ContainerTesting cont) {
		super(cont);
		xSize = WIDTH;
		ySize = HEIGHT;
	}
	
	@Override
	protected void drawGuiContainerBackgroundLayer(float partialTicks, int mouseX, int mouseY) {
		mc.getTextureManager().bindTexture(background);
		drawTexturedModalRect(guiLeft, guiTop, 0, 0, xSize, ySize);
	}
}
