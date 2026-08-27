package com.example.demo.controller;

import java.io.FileNotFoundException;
import java.util.List;
import com.example.demo.service.CustomerService;
import net.sf.jasperreports.engine.JRException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.demo.model.Customer;
import com.example.demo.repository.CustomerRepository;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api/v1")
public class CustomerController {

	@Autowired
	private CustomerService customerService;

	@GetMapping("/customer")
	public List<Customer> getAllCustomers(){
		return customerService.getAllCustomers();
	}

	@PostMapping("/customer")
	public ResponseEntity<Object> addCustomer(@RequestBody Customer customer) {
		boolean status = customerService.addCustomer(customer);
		return new ResponseEntity<Object>(new Status(status), HttpStatus.ACCEPTED);
	}

	@GetMapping("/customer/{id}")
	public ResponseEntity<Customer> getCustomerById(@PathVariable Integer id) {
		return ResponseEntity.ok(customerService.getCustomerById(id));
	}

	@PutMapping("/customer/{id}")
	public ResponseEntity<Object> updateCustomer(@PathVariable Integer id,@RequestBody Customer customer){
		boolean status = customerService.updateCustomer(id, customer);
		return new ResponseEntity<Object>(new Status(status), HttpStatus.ACCEPTED);
	}
	
	@DeleteMapping("/customer/{id}")
	public ResponseEntity<Object>  deleteCustomer(@PathVariable Integer id) {
		boolean status = customerService.deleteCustomerById(id);
		return new ResponseEntity<Object>(new Status(status), HttpStatus.ACCEPTED);
	}

	@GetMapping("/customer/report")
	public ResponseEntity<Object> createPdfReport() throws FileNotFoundException, JRException {
		boolean status = customerService.createReports();
		return new ResponseEntity<Object>(new Status(status),HttpStatus.ACCEPTED);
	}
}
