package com.callor.score.service.impl;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import com.callor.score.service.ScoreService;
import com.youngjin.standard.InputService;
import com.youngjin.standard.MenuService;
import com.youngjin.standard.impl.InputServiceImplV1;
import com.youngjin.standard.impl.MenuServiceImplV1;

public class ScoreServiceImplV1 implements ScoreService {

	protected MenuService menuService;
	protected InputService inService;
	protected Scanner scan;

	public ScoreServiceImplV1() {

		inService = new InputServiceImplV1();
		scan = new Scanner(System.in);

	}

	@Override
	public void selectMenu() {
		List<String> menuList = new ArrayList<String>();
		menuList.add("학생정보 등록");
		menuList.add("성적 등록");
		menuList.add("성적정보 열기");
		menuList.add("성적정보 저장");
		menuList.add("성적정보 출력");

		menuService = new MenuServiceImplV1("대한 고등학교 성적처리 시스템 2021", menuList);

		while (true) {

			Integer intMenu = menuService.selectMenu();
			if(intMenu == null) {
				System.out.println("입력 종료");
				break;
			}
			if (intMenu == 1) {
				
			} else if (intMenu == 2) {
				this.inputScore();
			} else if (intMenu == 3) {
				this.readScore();
			} else if (intMenu == 4) {
				this.saveScore();
			} else if (intMenu == 5) {
				this.printScore();
			}

		}

	}

	@Override
	public void inputScore() {
		// TODO Auto-generated method stub

	}

	@Override
	public void printScore() {
		// TODO Auto-generated method stub

	}

	@Override
	public void saveScore() {
		// TODO Auto-generated method stub

	}

	@Override
	public void readScore() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void checkScore() {
		// TODO Auto-generated method stub
		
	}

}
