package aqua.common.web;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Random;

public class WebTarget
{
	private URLConnection connection = null;
	private OutputStream os = null;
	private static Random random = new Random();
	private static String boundary = "---------------------------" + randomString() + randomString() + randomString();

	private static String randomString()
	{
		return Long.toString(random.nextLong(), 36);
	}

	public WebTarget(URL url) throws IOException
	{
		if(connection != null && connection.getURL().equals(url))
			return;
		
		connection = url.openConnection();
		connection.setDoOutput(true);
		connection.setRequestProperty("Content-Type", "multipart/form-data; boundary=" + boundary);
	}

	private void connect() throws IOException
	{
		if (os == null)
			os = connection.getOutputStream();
	}

	private void write(String s) throws IOException
	{
		connect();
		os.write(s.getBytes());
	}

	private void writeln(String s) throws IOException
	{
		write(s + "\r\n");
	}

	private void newline() throws IOException
	{
		write("\r\n");
	}

	private void boundary() throws IOException
	{
		write("--");
		write(boundary);
	}

	private void writeName(String name) throws IOException
	{
		newline();
		write("Content-Disposition: form-data; name=\"" + name + '"');
	}

	private void setParameter(String name, String value) throws IOException
	{
		boundary();
		writeName(name);
		newline();
		newline();
		writeln(value);
	}

	private void pipe(InputStream in, OutputStream out) throws IOException
	{
		byte[] buf = new byte[500000];
		
		synchronized(in)
		{
			while(true)
			{
				int nread = in.read(buf, 0, buf.length);
				
				if(nread < 0)
					break;
				
				out.write(buf, 0, nread);
			}
		}
		
		out.flush();
		in.close();
		buf = null;
	}

	private void setParameter(String name, String filename, InputStream is) throws IOException
	{
		boundary();
		writeName(name);
		writeln("; filename=\"" + filename + '"');
		
		String type = URLConnection.guessContentTypeFromName(filename);
		
		if(type == null)
			type = "application/octet-stream";
		
		writeln("Content-Type: " + type);
		
		newline();
		pipe(is, os);
		newline();
	}

	private void setParameter(String name, File file) throws IOException
	{
		setParameter(name, file.getPath(), new FileInputStream(file));
	}

	private void setParameter(String name, Object object) throws IOException
	{
		if(object instanceof File)
			setParameter(name, (File) object);
		else 
			setParameter(name, object.toString());
	}

	private void setParameters(Object[] parameters) throws IOException
	{
		if(parameters == null)
			return;
		
		for(int i = 0; i < parameters.length - 1; i += 2)
			setParameter(parameters[i].toString(), parameters[i + 1]);
	}

	private void post() throws IOException
	{
		boundary();
		writeln("--");
		os.close();
	}

	public void post(Object[] parameters) throws IOException
	{
		setParameters(parameters);
		post();
	}

	public String getResponse()
	{
		try
		{
			System.out.println("Openning stream: " + connection.getURL());

			BufferedReader rd = new BufferedReader(new InputStreamReader(connection.getInputStream()));

			StringBuffer response = new StringBuffer();
			
			while(true)
			{
				String line = rd.readLine();	
				if(line == null)break;	
				response.append(line);
			}
			
			rd.close();

			String str = response.toString().trim();
			
			System.out.println("Stream opened for " + connection.getURL() + " completed");
			return str;
		}
		catch(Exception e)
		{
			System.out.println("Error: Stream for " + connection.getURL() + " not ensablished");
			return null;
		}
	}
}
