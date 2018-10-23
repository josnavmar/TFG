package util;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.Scanner;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import main.Coordinate;

public class Geocode{

	private static String readAll(Reader rd) throws IOException {
	    StringBuilder sb = new StringBuilder();
	    int cp;
	    while ((cp = rd.read()) != -1) {
	      sb.append((char) cp);
	    }
	    return sb.toString();
	  }
	
	public static JSONObject readJsonFromUrl(String url) throws IOException, JSONException {
	    InputStream is = new URL(url).openStream();
	    try {
	      BufferedReader rd = new BufferedReader(new InputStreamReader(is, Charset.forName("UTF-8")));
	      String jsonText = readAll(rd);
	      JSONObject json = new JSONObject(jsonText);
	      return json;
	    } finally {
	      is.close();
	    }
	}
	
public static void main(String[] args) {

       System.out.println ("Por favor introduzca una localización:");

       String entradaTeclado = "";

       @SuppressWarnings("resource")
       Scanner entradaEscaner = new Scanner (System.in); //Creación de un objeto Scanner

       entradaTeclado = entradaEscaner.nextLine (); //Invocamos un método sobre un objeto Scanner

       String datos = "https://maps.googleapis.com/maps/api/geocode/json?address="+entradaTeclado.replaceAll("\\s","")+"&key=AIzaSyAKJoDxHiADxtdSi70NH88wy3eGnQb_rI4";
	
	
	try {
		JSONObject json = readJsonFromUrl(datos);
	
		
		JSONArray results = json.getJSONArray("results");
        JSONObject item = results.getJSONObject(0);//read first item of results
        JSONObject geometry = item.getJSONObject("geometry");//location is inside geometry object
        JSONObject location = geometry.getJSONObject("location");
        float latitude = location.getFloat("lat");
        float longitude = location.getFloat("lng");
        
   
        Coordinate coordinates = new Coordinate(latitude,longitude);
        
        System.out.println("Coordenadas: "+ coordinates.toString());
	
	} catch (JSONException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	
}

}