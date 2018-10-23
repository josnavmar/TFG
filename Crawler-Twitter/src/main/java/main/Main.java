package main;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.PreparedStatement;

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
	        fq.language(new String[]{"es"});
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
   

        public void onStatus(Status status) {
    	
    		
    		try {
    			
    			User user = status.getUser();
    			String name = status.getUser().getName();
				String aliasName = status.getUser().getScreenName();
				String profileLocation = user.getLocation();
				String twet = status.getText();
					
				
				if (status.isRetweet() == false && status.isRetweeted() == false && status.isRetweetedByMe() == false && user.getFollowersCount() > 100) {
					preparedStmt.setString(1, aliasName);
					preparedStmt.setString(2, name);
					preparedStmt.setString(3, twet);
					preparedStmt.setString(4, profileLocation);
					preparedStmt.setString(5, status.getCreatedAt().toString());
					// long tweetId = status.getId();
					preparedStmt.execute();
				}
				

					

				
    			
				
               
                
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
