package util;

import twitter4j.conf.ConfigurationBuilder;

public class Settings {
	
	//Contraseñas de acceso de Twitter Develops
	
	private final static String CONSUMER_KEY = "eMN8c6q5ZcLL1VsBHwj3jRjx0";
	private final static String CONSUMER_SECRET = "qa5l7YW7crUYq4SYtUuar5APb9VPjCMIpXtiqCwzRerGQ9t5YB";
	private final static String ACCESS_TOKEN = "439449780-4Lt4KUqocSe52hIkdYjVewhxtrOcO8W0EQNnQFCm";
	private final static String ACCESS_TOKEN_SECRET = "Pzx7R37vabdM6v4TeuUQOZYVRus9wFGa9JLS4Us8xx3ni";
	
	public static void configureProfile() {
		
		ConfigurationBuilder cb = new ConfigurationBuilder();

		cb.setDebugEnabled(true).setOAuthConsumerKey(CONSUMER_KEY)
				.setOAuthConsumerSecret(CONSUMER_SECRET)
				.setOAuthAccessToken(ACCESS_TOKEN)
				.setOAuthAccessTokenSecret(ACCESS_TOKEN_SECRET);
		
	}
}
