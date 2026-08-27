package com.jt.payment.service;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.UUID;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.jt.payment.dto.PaymentDto;
import com.jt.payment.entity.Payment;
import com.jt.payment.repository.PaymentRepository;

@Service
public class PaymentService {

	@Autowired
	private PaymentRepository paymentRepository;

	private static final Logger LOGGER = LoggerFactory.getLogger(PaymentService.class);

	public PaymentDto doPayment(PaymentDto paymentDto) {
		Payment payment = new Payment(paymentDto.getId(), paymentDto.getPaymentStatus(), paymentDto.getTransactionId(),
				paymentDto.getOrderId(), paymentDto.getAmount());
		payment.setPaymentStatus(processPaymentStatus());
		payment.setTransactionId(UUID.randomUUID().toString());
		Payment savedPayment = paymentRepository.save(payment);
		LOGGER.info("Payment processed with id: {}", savedPayment.getId());

		return new PaymentDto(savedPayment.getId(), savedPayment.getPaymentStatus(), savedPayment.getTransactionId(),
				savedPayment.getOrderId(), savedPayment.getAmount());
	}

	private String processPaymentStatus() {
		// should be 3rd party payment gateway (paypapal, paytem.....)
		return new Random().nextBoolean() ? "success" : "failure";
	}

	public List<PaymentDto> findPaymentByOrderId(Integer orderId) {
		List<Payment> payments = paymentRepository.findByOrderId(orderId);
		if (payments == null) {
			return null;
		}
		List<PaymentDto> dtos = new ArrayList<>();
		payments.forEach(payment -> dtos.add(new PaymentDto(payment.getId(), payment.getPaymentStatus(),
				payment.getTransactionId(), payment.getOrderId(), payment.getAmount())));

		return dtos;
	}
}
