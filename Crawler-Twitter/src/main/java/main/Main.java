package main;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.util.Calendar;

import twitter4j.FilterQuery;
import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.User;
import twitter4j.conf.ConfigurationBuilder;
import util.SettingsDB;
import util.SettingsTwitter;

public class Main {
	
	public static String hashtag;	
	public static ConfigurationBuilder cb = SettingsTwitter.configureProfile();
	public static TwitterStream twitterStream = new TwitterStreamFactory(cb.build()).getInstance();
	public static String twets;
	
	public static String insert = SettingsDB.queryExecute();
	public static Connection connection = SettingsDB.getConnection();
	public static PreparedStatement preparedStmt = SettingsDB.createPreStmt(connection, insert);

	public static void main(String[] args) {
		
		try {
			inputKeyword();
	        FilterQuery fq = new FilterQuery();
	        
	        String keywords[] = {hashtag};

	        fq.track(keywords);

	        twitterStream.addListener(listener);
	        twitterStream.filter(fq);
		}catch(Exception e) {
			
		}

		
		
	}
	
	private static void inputKeyword(){
        try {															  
        	
			
        	System.out.print("Introduce el Hashtag que desee: ");
        	BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));    	
        	hashtag = bufferRead.readLine();

        }catch (Exception e) {
			// TODO: handle exception
		}
	}
	
        
    static StatusListener listener = new StatusListener() {
    Integer cont = 0;  
    

        public void onStatus(Status status) {
    		
    		Calendar calendar = Calendar.getInstance();
    		java.sql.Date startDate = new java.sql.Date(calendar.getTime().getTime());
    		
    		try {
                User user = status.getUser();
                cont = cont++;                
                String username = status.getUser().getScreenName();                 
                String profileLocation = user.getLocation();
                String twet = status.getText();

                
                preparedStmt.setLong (1, cont);
    		    preparedStmt.setString (2, twet);
    		    preparedStmt.setString(3, profileLocation);
    		    preparedStmt.setDate(4, startDate);                
                //long tweetId = status.getId(); 
                
    		    preparedStmt.execute();
    		}catch(Exception e) {
    			
    		}  

        }

		public void onException(Exception arg0) {
			// TODO Auto-generated method stub
			
		}

		public void onDeletionNotice(StatusDeletionNotice arg0) {
			// TODO Auto-generated method stub
			
		}

		public void onScrubGeo(long arg0, long arg1) {
			// TODO Auto-generated method stub
			
		}

		public void onStallWarning(StallWarning arg0) {
			// TODO Auto-generated method stub
			
		}

		public void onTrackLimitationNotice(int arg0) {
			// TODO Auto-generated method stub
			
		}

    };    
}
