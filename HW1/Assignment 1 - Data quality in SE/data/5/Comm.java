package simulator;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;

import gnu.io.CommPortIdentifier; 
import gnu.io.SerialPort;
import gnu.io.SerialPortEvent; 
import gnu.io.SerialPortEventListener;

import java.util.Enumeration;
import java.util.LinkedList;
import java.util.Queue;

import org.lwjgl.glfw.*;

public class Comm implements SerialPortEventListener {
	SerialPort serialPort;
	private static final String PORT_NAMES[] = { 
			"/dev/tty.usbserial-A9007UX1", // Mac OS X
                        "/dev/ttyACM0", // Raspberry Pi
			"/dev/ttyUSB0", // Linux
			"COM3", // Windows
	};
	private BufferedReader input;
	private OutputStream output;
	private static final int TIME_OUT = 2000;
	private static final int DATA_RATE = 115200;

	private String inputLeftover;
	private Queue<Block> inputBlockBuffer;
	
	public class Block {
		public String string;
		public double time;
		public Block(String string, double time) {
			super();
			this.string = string;
			this.time = time;
		}
	}
	
	public void initialize() {
		inputLeftover = "";
		inputBlockBuffer = new LinkedList<Block>();
		
		CommPortIdentifier portId = null;
		Enumeration portEnum = CommPortIdentifier.getPortIdentifiers();

		while (portEnum.hasMoreElements()) {
			CommPortIdentifier currPortId = (CommPortIdentifier) portEnum.nextElement();
			for (String portName : PORT_NAMES) {
				if (currPortId.getName().equals(portName)) {
					portId = currPortId;
					break;
				}
			}
		}
		if (portId == null) {
			System.out.println("Could not find COM port.");
			return;
		}

		try {
			serialPort = (SerialPort) portId.open(this.getClass().getName(),
					TIME_OUT);

			// set port parameters
			serialPort.setSerialPortParams(DATA_RATE,
					SerialPort.DATABITS_8,
					SerialPort.STOPBITS_1,
					SerialPort.PARITY_NONE);
			// open the streams
			input = new BufferedReader(new InputStreamReader(serialPort.getInputStream()));
			output = serialPort.getOutputStream();

			// add event listeners
			serialPort.addEventListener(this);
			System.out.println();
			serialPort.notifyOnDataAvailable(true);
			 Thread.sleep(1500);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public synchronized void close() {
		if (serialPort != null) {
			serialPort.removeEventListener();
			serialPort.close();
		}
	}

	/**
	 * Handle an event on the serial port. Read the data and print it.
	 */
	
	public void serialEvent(SerialPortEvent oEvent) {
		if (oEvent.getEventType() == SerialPortEvent.DATA_AVAILABLE) {
			try {
				String rawInput = inputLeftover;
				while(input.ready())
					rawInput += (char)input.read();
				//System.out.println("input:"+rawInput);
				String[] inputLines = rawInput.split("\n");
				for(int c=0; c<inputLines.length-1; c++){
					String[] inputBlocks = inputLines[c].split("\t");
					for(String inputBlock : inputBlocks){
						if(inputBlock.length() == 0)
							continue;
						/*for(char ch : inputBlock.toCharArray()){
							System.out.println((int)ch);
						}*/
						inputBlockBuffer.add(new Block(inputBlock, GLFW.glfwGetTime()));
					}
				}
				inputLeftover = inputLines[inputLines.length-1];
				
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		// Ignore all the other eventTypes, but you should consider the other ones.
	}
	
	public synchronized boolean serialWrite(String message) throws UnsupportedEncodingException, IOException{
		output.write(message.getBytes("US-ASCII"));
		return true;
	}

	public boolean stringBlockReady(){
		return inputBlockBuffer.size() > 0;
	}
	
	public Block dequeueStringBlock() {
		return inputBlockBuffer.poll();
	}
	
}
