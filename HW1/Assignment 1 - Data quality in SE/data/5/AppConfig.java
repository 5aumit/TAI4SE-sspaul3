package com.vbt.app;

import java.util.Properties;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.web.servlet.HandlerExceptionResolver;
import org.springframework.web.servlet.handler.SimpleMappingExceptionResolver;

//@EnableWebMvc
@ComponentScan("com.vbt")
public class AppConfig {

    @Bean
    HandlerExceptionResolver errorHandler () {
        SimpleMappingExceptionResolver s =
                  new SimpleMappingExceptionResolver();

        //exception to view name mapping
        Properties p = new Properties();
        p.setProperty(Exception.class.getName(), "generic_error");
        
        s.setExceptionMappings(p);

        //mapping status code with view response.
        s.addStatusCode("generic_error", 404);

        //setting default error view
        s.setDefaultErrorView("defaultErrorView");
        //setting default status code
        s.setDefaultStatusCode(400);

        return s;
    } 
}