package Airline;

import java.text.SimpleDateFormat;
import java.util.Date;

/****************************************************************************
 * Get Flight details given Passenger ID, Flight ID, Flight date and time
 ***************************************************************************/

public class Flight {
	
	String passengerID;
	String flightID;
	String from;
	String to;
	String unixArrival;
	String arrivalTime;
	int flightTime;
	String deptFAA;
	String destFAA;

	//The flight constructor - takes all defined variables as parameters.
	public Flight(String _passID, String _flightID, String _from, String _to, String _unixArrival, String _flightTime) {
		passengerID = _passID;
		flightID = _flightID;
		
		from = _from;
		to = _to;
		
		unixArrival = _unixArrival;
		arrivalTime = unixToHHMMSS(unixArrival);
		
		flightTime = Integer.parseInt(_flightTime);
	}
	
	//Convert date and time format
	private String unixToHHMMSS(String unixTime){
		long unixSeconds = Long.parseLong(unixTime);
		Date date = new Date(unixSeconds*1000L);                 // convert seconds to milliseconds
		SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss"); // date format

		String formattedDate = sdf.format(date);
		return formattedDate;
	}
	
	//Get PassengerID
	public String getPassengerID(){
		return passengerID;
	}
	
	//Get flightID
	public String getFlightID(){
		return flightID;
	}
		
	public String getFrom(){
		return from;
	}
	
	public String getTo(){
		return to;
	}
	
	//Get Arrival Time
	String convertArrivalTime(String seconds){
		//Convert unix epoch time to HH:MM:SS
		return new String(seconds);
	}
	
        //Get deptFAA
	public String getDeptFAA()
	{
		return deptFAA;
	}
	
	//Get destFAA
	public String getDest()
	{
		return destFAA;
	}
	

	public String toString(){
		return passengerID + " " + to + " " + from + " " + arrivalTime + " " + flightTime + " mins";
	}
	
}
