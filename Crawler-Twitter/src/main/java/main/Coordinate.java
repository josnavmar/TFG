package main;

public class Coordinate {

	 private double lat;
	    private double lng;

	    public Coordinate(double latitude, double longitude)
	    {
	        lat = latitude;
	        lng = longitude;

	    }

		public double getLat() {
			return lat;
		}

		public void setLat(double lat) {
			this.lat = lat;
		}


		public double getLng() {
			return lng;
		}

		public void setLng(double lng) {
			this.lng = lng;
		}
		
		@Override
		public String toString() {
			return "Coordinate [lat=" + lat + ", lng=" + lng + "]";
		}

	  
}
