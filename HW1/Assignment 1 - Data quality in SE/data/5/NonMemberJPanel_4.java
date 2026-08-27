package project1.ui;

import javax.swing.JPanel;

import java.awt.CardLayout;
import java.awt.Color;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextPane;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.SwingConstants;
import java.awt.Font;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;

public class NonMemberJPanel_4 extends JPanel {
	private JTextField noTF;
	private JTextField chargeTF;
	private JTextField timeTF;
	private PcposJFrameMain mainFrame;
	private JButton bt_randReset;  //리셋버튼
	
	
	public void setMainFrame(PcposJFrameMain mainFrame) {
		this.mainFrame = mainFrame;
	}
	
	/**
	 * Create the panel.
	 */
	public NonMemberJPanel_4() {
		addComponentListener(new ComponentAdapter() {
			@Override
			public void componentShown(ComponentEvent e) {
				showData();
				showNo();
				showtime();
				
				
			}
		});
		setBackground(new Color(255, 255, 255));
		setLayout(null);
		
		JPanel panel_1 = new JPanel();
		panel_1.setLayout(null);
		panel_1.setBackground(new Color(153, 204, 255));
		panel_1.setBounds(205, 89, 350, 540);
		add(panel_1);
		
		noTF = new JTextField();
		noTF.setHorizontalAlignment(SwingConstants.CENTER);
		noTF.setFont(new Font("나눔스퀘어라운드 ExtraBold", Font.PLAIN, 12));
		noTF.setText("\uC120\uD0DD\uD55C \uC694\uAE08");
		noTF.setColumns(10);
		noTF.setBounds(51, 80, 233, 73);
		panel_1.add(noTF);
		
		chargeTF = new JTextField();
		chargeTF.setHorizontalAlignment(SwingConstants.CENTER);
		chargeTF.setFont(new Font("나눔스퀘어라운드 ExtraBold", Font.PLAIN, 12));
		chargeTF.setText("\uCDA9\uC804 \uAE08\uC561");
		chargeTF.setColumns(10);
		chargeTF.setBounds(51, 233, 233, 73);
		panel_1.add(chargeTF);
		
		timeTF = new JTextField();
		timeTF.setHorizontalAlignment(SwingConstants.CENTER);
		timeTF.setFont(new Font("나눔스퀘어라운드 ExtraBold", Font.PLAIN, 12));
		timeTF.setText("\uCDA9\uC804 \uC2DC\uAC04");
		timeTF.setColumns(10);
		timeTF.setBounds(51, 386, 233, 73);
		panel_1.add(timeTF);
		
		JButton done = new JButton("\uC644\uB8CC");
		done.setFont(new Font("나눔스퀘어라운드 ExtraBold", Font.PLAIN, 12));
		done.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {		//완료버튼
				
				mainFrame.changePanel("main");
			}
		});
		done.setBounds(837, 404, 200, 75);
		add(done);
		
		JLabel lblNewLabel_1 = new JLabel("\uACB0\uC81C\uAC00 \uC644\uB8CC \uB418\uC5C8\uC2B5\uB2C8\uB2E4.");
		lblNewLabel_1.setFont(new Font("나눔스퀘어라운드 ExtraBold", Font.PLAIN, 12));
		lblNewLabel_1.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel_1.setBounds(827, 181, 220, 80);
		add(lblNewLabel_1);
		
		JLabel label = new JLabel("\uC774\uC6A9\uD574 \uC8FC\uC154\uC11C \uAC10\uC0AC\uD569\uB2C8\uB2E4.");
		label.setFont(new Font("나눔스퀘어라운드 ExtraBold", Font.PLAIN, 12));
		label.setHorizontalAlignment(SwingConstants.CENTER);
		label.setBounds(827, 241, 220, 80);
		add(label);
		
		JLabel lblNewLabel = new JLabel("\uBE44\uD68C\uC6D0");
		lblNewLabel.setFont(new Font("나눔스퀘어라운드 ExtraBold", Font.PLAIN, 15));
		lblNewLabel.setBounds(12, 10, 57, 15);
		add(lblNewLabel);

	}
	
	public void showData() {
		chargeTF.setText(PcposJFrameMain.money + "원");
	}
	public void showNo() {
		noTF.setText(NonMemberJPanel_1.no + "번");
	}
	public void showtime() {
		timeTF.setText(PcposJFrameMain.time+"");
	}
	
	
	
}



