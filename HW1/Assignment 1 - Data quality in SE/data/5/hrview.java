package com.ssms.views.hr;

import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.Toolkit;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSeparator;
import javax.swing.border.LineBorder;

public class hrview {

	private JFrame frame;

	public hrview() {
		initComponents();
		createEvents();
	}

	public void show() {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					hrview window = new hrview();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}
	
	
	private void createEvents() {
		
	}

	private void initComponents() {
		frame = new JFrame();
		frame.setTitle("School Management System");
		frame.setIconImage(Toolkit.getDefaultToolkit().getImage("./resources/icons/books.png"));
		frame.setBounds(100, 100, 848, 516);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JPanel panelHrInfo = new JPanel();
		panelHrInfo.setBorder(new LineBorder(new Color(0, 0, 0), 1, true));
		panelHrInfo.setBounds(237, 31, 572, 423);
		frame.getContentPane().add(panelHrInfo);
		
		JPanel panelHr = new JPanel();
		panelHr.setLayout(null);
		panelHr.setBorder(new LineBorder(new Color(0, 0, 0), 1, true));
		panelHr.setBounds(27, 31, 191, 423);
		frame.getContentPane().add(panelHr);
		
		JButton btnStaffDirectory = new JButton("Staff Directory");
		btnStaffDirectory.setBounds(33, 79, 127, 31);
		panelHr.add(btnStaffDirectory);
		
		JButton btnStaffAttendance = new JButton("Staff Attendance");
		btnStaffAttendance.setBounds(33, 125, 127, 31);
		panelHr.add(btnStaffAttendance);
		
		JButton btnStaffAttendanceReport = new JButton("Attendance Report");
		btnStaffAttendanceReport.setBounds(33, 167, 127, 31);
		panelHr.add(btnStaffAttendanceReport);
		
		JButton btnLeaveType = new JButton("Leave Type");
		btnLeaveType.setBounds(33, 209, 127, 31);
		panelHr.add(btnLeaveType);
		
		JButton btnDepartment = new JButton("Department");
		btnDepartment.setBounds(33, 251, 127, 31);
		panelHr.add(btnDepartment);
		
		JButton btnDesignation = new JButton("Designation");
		btnDesignation.setBounds(33, 293, 127, 31);
		panelHr.add(btnDesignation);
		
		JLabel lblStudentInformation = new JLabel("Human Resource");
		lblStudentInformation.setFont(new Font("Times New Roman", Font.BOLD, 18));
		lblStudentInformation.setBounds(33, 11, 141, 31);
		panelHr.add(lblStudentInformation);
		
		JSeparator separatorNavigator = new JSeparator();
		separatorNavigator.setForeground(Color.BLUE);
		separatorNavigator.setBounds(33, 53, 127, 2);
		panelHr.add(separatorNavigator);
		
		JButton btnApplyLeave = new JButton("Apply Leave");
		btnApplyLeave.setBounds(33, 333, 127, 31);
		panelHr.add(btnApplyLeave);
		
		JButton btnApproveLeave = new JButton("Approve Leave");
		btnApproveLeave.setBounds(33, 375, 127, 31);
		panelHr.add(btnApproveLeave);
		
	}
}
