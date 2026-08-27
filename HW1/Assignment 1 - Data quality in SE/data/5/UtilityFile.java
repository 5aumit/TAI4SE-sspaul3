package com.aurovind.AE.automation.utilities;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

import org.junit.Assert;
import org.testng.Reporter;

public class UtilityFile {
	
	public static String runMacro(String macroName, String jobName, String statusFile) {
		String jobStatus = null;
		try {
			TimeUnit.SECONDS.sleep(2);
			execCommandLine(macroName , jobName);
		}
		catch(InterruptedException e) {
			e.printStackTrace();
		}
		
		return jobStatus;
	}

	
	
	public static void execCommandLine(String command , String jobName) {
		try {
			Process process = Runtime.getRuntime().exec(command);
			ReportLog("[UtilityFile] Executing VB/Batch Script : "+jobName);
			BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
			String s;
			while((s = reader.readLine()) != null) {
				
			}
		}
		catch(IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void runBatFile(String batFileName , String description , String downloadedFilePath) {
		try {
			TimeUnit.SECONDS.sleep(2);
			execCommandLine(batFileName, description);
			isFilePresent(downloadedFilePath);
		}
		catch(InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	
	public static void isFilePresent(String FileName) {
		int timeout = 20;
		int i = 0;
		File file = new File(FileName);
		
		double bytes = file.length();
		double kilobytes = (bytes / 1024);
		double megabytes = (kilobytes / 1024);
		
		for(i=0; i <= timeout; i++)
		{
			try {
				if(file.exists() && !file.isDirectory() && bytes != 0.0);
				break;
			}
			catch(Exception e1) 
			{
				try 
				{
					TimeUnit.SECONDS.sleep(2);
				}
				catch(InterruptedException e) 
				{
					Result("FAIL", "[UtilityFile] Sleep Should Work","[UtilityFile] Sleep is Not Working");
					e.printStackTrace();
				}
			}
		}
	}



	public static void ReportLog(String sMessage)
	{
		Date sDate = new Date();
		SimpleDateFormat dStartDate = new SimpleDateFormat("HH:mm:ss");
		String time = dStartDate.format(sDate);
		Reporter.log("["+time+"]" + " " + sMessage + "\n" , true);
		
	}
	
	public static void Result(String strResult, String strExpected, String strActual) 
	{
		if(strResult.trim().toUpperCase().contains("PASS")) 
		{
			ReportLog("Expected : " + strExpected+ "\n");
			ReportLog("Actual : " + strActual+ "\n");
			ReportLog("----Failed----"+ "\n");
		}
		else {
			ReportLog("----Warning----" + "Expected : " + strExpected + "\n");
			ReportLog("----Warning----" + "Actual : " + strActual + "\n");
			Assert.fail("Expected : " + strExpected + "\n" + "Actual : " + strActual + "\n");
			
		}
	}
	
}

