package io.ztech.hrmanagement.controllers;

import java.math.BigInteger;
import java.util.ArrayList;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import io.ztech.hrmanagement.beans.objects.ErrorObject;
import io.ztech.hrmanagement.beans.objects.Profile;
import io.ztech.hrmanagement.beans.objects.ResponseObject;
import io.ztech.hrmanagement.delegates.SearchEmployeeDelegate;
import io.ztech.hrmanagement.utils.PersistenceException;

@RestController
public class ProfileController {
	
	@GetMapping("/profiles")
	ResponseObject getAllProfiles() {
		ResponseObject responseObject = new ResponseObject();
		SearchEmployeeDelegate searchEmployeeDelegate = new SearchEmployeeDelegate();
		ArrayList<Object> objects = new ArrayList<>();
		
		try {
			ArrayList<Profile> profiles = searchEmployeeDelegate.findAllProfiles();
			if(profiles == null) {
				responseObject.setStatus(401);
				objects.add(new ErrorObject("No Profiles found"));
			} else {
				responseObject.setStatus(200);
				System.out.println(profiles.get(0).getEmployee().getEmp_name());
				objects.add(profiles);
				responseObject.setObjects(objects);
			}
		} catch (PersistenceException e) {
			e.printStackTrace();
			responseObject.setStatus(500);
			objects.add(new ErrorObject("Internal Server Error"));
		}
		
		return responseObject;
	}
	
	@GetMapping("/profiles/{empId}")
	@ResponseBody
	ResponseObject getProfileOfID(@PathVariable BigInteger empId) {
		ResponseObject responseObject = new ResponseObject();
		SearchEmployeeDelegate searchEmployeeDelegate = new SearchEmployeeDelegate();
		ArrayList<Object> objects = new ArrayList<Object>();
		
		try {
			Profile profile = searchEmployeeDelegate.findEmployeeByID(empId);
			if(profile == null) {
				responseObject.setStatus(401);
				objects.add(new ErrorObject("No Profile found"));
			} else {
				responseObject.setStatus(200);
				objects.add(profile);
				responseObject.setObjects(objects);
			}
		} catch (PersistenceException e) {
			responseObject.setStatus(500);
			objects.add(new ErrorObject("Internal Server Error"));
			e.printStackTrace();
		}
		
		return responseObject;
	}
}
