package baseDeDatos;

import java.util.ArrayList;
import java.util.Scanner;

import subasta.Subasta;
import subasta.Usuario;

public class TestAuction {

	public static void main(String[] args) {
		Scanner teclado = new Scanner(System.in);
		
		int op = 0;
		do {
			op = menu();

			switch (op) {
			case 1:
				
				break;
			case 2:
				
				break;
			case 3:
				
				break;
			case 4:
				
				break;
				
			}
		} while (op != 5);
	}

	public static int menu() {
		Scanner teclado = new Scanner(System.in);
		System.out.println("1-. Crear nuevo usuario.");
		System.out.println("2-. .");
		System.out.println("3-. .");
		System.out.println("4-. .");
		System.out.println("5-. Sal del sistema");

		int op = teclado.nextInt();
		return op;
	}
}