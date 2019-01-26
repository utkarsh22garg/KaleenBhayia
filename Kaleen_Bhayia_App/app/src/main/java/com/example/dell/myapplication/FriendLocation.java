package com.example.dell.myapplication;

public class FriendLocation  {
    public String latitude;
    public String longitude;
    public String name;
    public FriendLocation(){

    }

    public FriendLocation(String lati,String longi,String name)
    {
        this.name=name;
        setLatitude(lati);
        setLongitude(longi);
    }
    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }
}
