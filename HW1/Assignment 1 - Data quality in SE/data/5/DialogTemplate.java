package kyPkg.frame;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

import kyPkg.panel.RezPanel;

public class DialogTemplate extends JDialog {
	private static final long serialVersionUID = 8689974610721637381L;
	private JDialog thisFrame;
	private Container container;
	private RezPanel srcPanel;
	private RezPanel dstPanel;

	// -------------------------------------------------------------------------
	// Constructor
	// -------------------------------------------------------------------------
	public DialogTemplate(String title, int width, int height, RezPanel dst,
			RezPanel src) {
		super((Frame) null, title, true);
		this.thisFrame = this;
		this.dstPanel = dst;
		this.srcPanel = src;
		this.container = this.getContentPane();
		srcPanel.init();
		setSize(width, height);
		centering();
		container.setLayout(new BorderLayout());
		JButton btnOK = new JButton("OK");
		btnOK.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ae) {
				srcPanel.update();
				dstPanel.init();
				thisFrame.setVisible(false);
			}
		});
		container.add(src, BorderLayout.CENTER);
		container.add(btnOK, BorderLayout.SOUTH);
		thisFrame.setVisible(true);
	}

	// ---------------------------------------------------------------------
	// ウィンドウを中央に配置
	// ---------------------------------------------------------------------
	private void centering() {
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		Dimension thisSize = thisFrame.getSize();
		if (thisSize.height > screenSize.height)
			thisSize.height = screenSize.height;
		if (thisSize.width > screenSize.width)
			thisSize.width = screenSize.width;
		this.setLocation((screenSize.width - thisSize.width) / 2,
				(screenSize.height - thisSize.height) / 2);
	}

}
