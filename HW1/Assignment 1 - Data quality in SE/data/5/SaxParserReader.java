package Reader;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.*;


import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.Attributes;

import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import org.xml.sax.helpers.DefaultHandler;

public class SaxParserReader {
	public SaxParserReader(String[] args) {
		FileEval evaluator = new FileEval(args[2]);
		String xmlFileName1 = args[0];
		String xmlFileName2 = args[1];
		try {
			SAXParserFactory factory = SAXParserFactory.newInstance();
			SAXParser saxParser1 = factory.newSAXParser();
			SAXParser saxParser2 = factory.newSAXParser();
			ConfigHandler handler1 = new ConfigHandler(evaluator);
			ConfigHandler handler2 = new ConfigHandler(evaluator);
			saxParser1.parse(new FileInputStream(xmlFileName1), handler1);
			saxParser2.parse(new FileInputStream(xmlFileName2), handler2);

		} catch (IOException e) {
			System.out.println("Error reading URI: " + e.getMessage());
		} catch (SAXException e) {
			System.out.println("Error in parsing: " + e.getMessage());
		} catch (ParserConfigurationException e) {
			System.out.println("Error in XML parser configuration: "
					+ e.getMessage());
		}
	}

	public static void main(String[] args) {
		System.setProperty("entityExpansionLimit", "2500000");
		if (args.length < 1) {
			System.exit(0);
		}
		new SaxParserReader(args);
	}

	class ConfigHandler extends DefaultHandler {
		private String streamName = "";
		int i = 0;
		FileEval eval;
		Map<String, StreamWithRatio[]> xmlMap = new HashMap<String, StreamWithRatio[]>();
		public ConfigHandler(FileEval e) {
			this.eval = e;
		}
		public void startElement(String namespaceURI, String localName,
				String rawName, Attributes atts) throws SAXException {

			if (atts.getValue("key") != null) {
				streamName = atts.getValue("key");			
			}
			if (atts.getValue("name") != null && atts.getValue("ratio") != null){
				if(i == 0 || !xmlMap.containsKey(streamName)){xmlMap.put(streamName, new StreamWithRatio[10]); i = 0;}
				xmlMap.get(streamName)[i++] = new StreamWithRatio( atts.getValue("name"),atts.getValue("ratio"));		
			}
		}
		public void endElement(String namespaceURI, String localName,
				String rawName, Attributes atts) throws SAXException {
			if(rawName.equals("stream")){
				i = 0;
			}
		}
		@Override
		public void startDocument() {
			System.out.println("Document starts.");
		}

		@Override
		public void endDocument() {
			System.out.println("Document ends.");
			eval.inputMap(xmlMap);
		}

		@Override
		public void characters(char[] ch, int start, int length)
				throws SAXException {
		}

		private void Message(String mode, SAXParseException exception) {
			System.out.println(mode + " Line: " + exception.getLineNumber()
					+ " URI: " + exception.getSystemId() + "\n" + " Message: "
					+ exception.getMessage());
		}

		public void warning(SAXParseException exception) throws SAXException {

			Message("**Parsing Warning**\n", exception);
			throw new SAXException("Warning encountered");
		}

		public void error(SAXParseException exception) throws SAXException {

			Message("**Parsing Error**\n", exception);
			throw new SAXException("Error encountered");
		}

		public void fatalError(SAXParseException exception) throws SAXException {

			Message("**Parsing Fatal Error**\n", exception);
			throw new SAXException("Fatal Error encountered");
		}

	}
	
}
class StreamWithRatio{
	String name;
	double ratio;
	StreamWithRatio(String inputName, String inputRatio){
		this.name = inputName;
		this.ratio = Double.parseDouble(inputRatio);
	}
	boolean compare(StreamWithRatio stream){
		if (this.name.equals(stream.name)){
			return true;
		}
		return false;
	}
}