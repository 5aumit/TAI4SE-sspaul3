package com.anjanda.letsmeet.alarm.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.anjanda.letsmeet.alarm.service.AlarmService;
import com.anjanda.letsmeet.repository.dto.Alarm;

@RestController
@RequestMapping("/alarm")
public class AlarmController {

	@Autowired
	private AlarmService alarmService;
	
	/* C :: 알람 1줄 생성 */
	@PostMapping("/create")
	public ResponseEntity<String> createAlarm(Alarm alarm) throws Exception {
		System.out.println(alarm.toString());
		if(alarmService.createAlarm(alarm) > 0) {
			return new ResponseEntity<String>("알람 생성 성공", HttpStatus.OK);
		}
			return new ResponseEntity<String>("알람 생성 실패", HttpStatus.NO_CONTENT);
	}
	
	/* R :: 사용자의 알람 전체 조회 */
	@GetMapping("")
	public ResponseEntity<List<Alarm>> reviewAlarm(int uNo) throws Exception {
		return new ResponseEntity<List<Alarm>>(alarmService.reviewAlarm(uNo), HttpStatus.OK);
	}
	
	/* D :: 사용자의 알람 삭제 */
	@DeleteMapping("/delete")
	public ResponseEntity<String> deleteAlarm(Alarm alarm) throws Exception {
		if(alarmService.deleteAlarm(alarm)) {
			return new ResponseEntity<String>("약속방 삭제 성공", HttpStatus.OK);
		}
		return new ResponseEntity<String>("약속방 삭제 실패", HttpStatus.NO_CONTENT);
	}
}
