package com.guifaleiros.comercial.controllers;

import java.net.URI;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.guifaleiros.comercial.dto.CategoryDTO;
import com.guifaleiros.comercial.models.Category;
import com.guifaleiros.comercial.models.Request;
import com.guifaleiros.comercial.services.RequestService;

@RestController
@RequestMapping(value = "/requests")
public class RequestController {
	
	@Autowired
	RequestService requestService;
	
	@RequestMapping(value="/{id}", method=RequestMethod.GET)
	public ResponseEntity<Request> find(@PathVariable Integer id) {
		Request response = requestService.find(id);
		return ResponseEntity.ok().body(response);
	}
	
	@RequestMapping(method = RequestMethod.POST)
	public ResponseEntity<Void> insert(@Valid @RequestBody Request obj){
		obj = requestService.insert(obj);
		URI uri = ServletUriComponentsBuilder
				.fromCurrentRequest().path("/{id}").buildAndExpand(obj.getId()).toUri();
		return ResponseEntity.created(uri).build();
	}
}
