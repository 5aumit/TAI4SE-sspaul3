package com.smart.platform.filedb;

import java.io.File;
import java.net.URL;


public class CurrentdirHelper {
	static URL url=null;
	static{
		url=CurrentdirHelper.class.getResource("CurrentdirHelper.class");
	}
	public static File getappDir() {
		URL u = url;
		String url = u.toString();
		File outdir = new File(".");
		if (url.indexOf("!") > 0) {
			int p = url.indexOf("!");
			url = url.substring(0, p);
			if (url.startsWith("jar:"))
				url = url.substring(4);
			if (url.startsWith("file:"))
				url = url.substring(5);

			p = url.indexOf("/lib/");
			if (p > 0) {
				url = url.substring(0, p);
				outdir = new File(url);
			}

		} else {
			int p = url.indexOf("/classes/");
			if (p > 0) {
				url = url.substring(0, p);
				if (url.startsWith("file:"))
					url = url.substring(5);
				outdir = new File(url);
			}
		}
		return outdir;
	}
	
	/**
	 * 返回 classes/专项开发
	 * @return
	 */
	public static File getZxdir(){
		return new File(getappDir(),"classes/专项开发");
	}


	public static File getLibdir(){
		return new File(getappDir(),"lib");
	}

	public static File getClassdir(){
		return new File(getappDir(),"classes");
	}
}
