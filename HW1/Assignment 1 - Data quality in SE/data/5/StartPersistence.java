package run;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import repository.interfaces.IPageRepository;
import repository.interfaces.ISiteRepository;
import repository.interfaces.IUserRepository;

@SpringBootApplication
@ComponentScan(basePackages = { "rest.controllers", "repository.implementations"})
@EntityScan({ "entities.domain" })
@EnableJpaRepositories(basePackageClasses = { IUserRepository.class, IPageRepository.class,
		ISiteRepository.class }, considerNestedRepositories = true)
public class StartPersistence {

	public static void main(String[] args) {

		SpringApplication.run(StartPersistence.class, args);

	}
}
