package com.example.dell.myapplication;

public class FriendLocation  {
    public Double latitude;
    public Double longitude;
    public String name;
    public FriendLocation(){

    }

    public FriendLocation(Double lati,Double longi,String name)
    {
        this.name=name;
        setLatitude(lati);
        setLongitude(longi);
    }
    public void setLatitude(Double latitude) {
        this.latitude = latitude;
    }

    public void setLongitude(Double longitude) {
        this.longitude = longitude;
    }
}
