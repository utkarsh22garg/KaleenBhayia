package com.example.dell.myapplication;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.media.MediaPlayer;
import android.os.AsyncTask;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v4.app.ActivityCompat;
import android.telephony.SmsManager;
import android.util.Config;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.google.firebase.FirebaseApp;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.Map;
public class MyFirebaseInstanceIDService extends FirebaseMessagingService implements LocationListener {
    public static String message_toSpeak="";
    JSONObject object;
    String latitude;
    String longitude;
    double latitude1;
    double longitude1;
    String name;


    public void onNewToken(String id) {

        Log.d("json_value", id);
    }

    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        Map<String, String> params = remoteMessage.getData();
        object = new JSONObject(params);
        String type = null;

        try {
            type = object.getString("type");
            type = type.toLowerCase();
            if (type.equalsIgnoreCase("message"))
                new Background().execute();
            else if (type.contains("find")) {
                //new MainActivity().Player_alarm();
                Intent intent = new Intent(getApplicationContext(), Player.class);
                startActivity(intent);
            } else if (type.contains("where")) {
                Log.d("TAGGG", "friendlocation: here "+name);
               // friendlocation();
                location();
                Log.e("asdf", "asdf");
            }
        } catch (JSONException e) {
            Log.e("ERROR_HAI", e.toString());
            e.printStackTrace();
        }

        super.onMessageReceived(remoteMessage);
    }
    public void getcoordi()
    {
        boolean isGPSEnabled=false;
        LocationManager locationManager = (LocationManager)
                getSystemService(Context.LOCATION_SERVICE);
        isGPSEnabled = locationManager
                .isProviderEnabled(LocationManager.GPS_PROVIDER);
        if (!isGPSEnabled) {
            Toast.makeText(getApplicationContext(), "Gps is not Enabled", Toast.LENGTH_LONG).show();
        } else {
            if (locationManager != null) {
                if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                    // TODO: Consider calling
                    //    ActivityCompat#requestPermissions
                    // here to request the missing permissions, and then overriding
                    //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
                    //                                          int[] grantResults)
                    // to handle the case where the user grants the permission. See the documentation
                    // for ActivityCompat#requestPermissions for more details.
                    return;
                }
                Location location = locationManager
                        .getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
                if (location != null) {
                    latitude1 = location.getLatitude();
                    longitude1 = location.getLongitude();
                }
            }
        }
    }


    public void location() {
        DatabaseReference mFirebaseDatabase;
        FirebaseDatabase mFirebaseInstance;
        mFirebaseInstance = FirebaseDatabase.getInstance();
        mFirebaseDatabase = mFirebaseInstance.getReference();
        mFirebaseDatabase.child("latitude").removeValue();
        mFirebaseDatabase.child("longitude").removeValue();
        getcoordi();
        new PushBackground().execute();



    }
    @Override
    public void onLocationChanged(Location location) {
        Log.d("TAGGG", "onLocationChanged: ");

    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {

    }

    @Override
    public void onProviderEnabled(String provider) {

    }

    @Override
    public void onProviderDisabled(String provider) {

    }

    public class Background extends AsyncTask{
        @Override
        protected Object doInBackground(Object[] objects) {
            try {
                String no = object.getString("no");
                String msg=object.getString("message");
                String time =object.getString("time");
                if(!time.equalsIgnoreCase("now"))
                Thread.sleep(Integer.parseInt(time)*1000);
                SmsManager smsManager = SmsManager.getDefault();
                smsManager.sendTextMessage(no, null, msg, null, null);
                Log.e("JSON_DATA",no+" "+msg+" "+time);

            } catch (JSONException e) {
                e.printStackTrace();
                Log.e("ERROR_hai",e.toString());
            } catch (InterruptedException e) {
                Log.e("ERROR_hai",e.toString());
                e.printStackTrace();
            }
            return null;
        }
    }
    public class PushBackground extends AsyncTask
    {

        @Override
        protected Object doInBackground(Object[] objects) {
            DatabaseReference mFirebaseDatabase;
            FirebaseDatabase mFirebaseInstance;
            mFirebaseInstance = FirebaseDatabase.getInstance();
            mFirebaseDatabase = mFirebaseInstance.getReference();
            mFirebaseDatabase.child("latitude").setValue(latitude1);
            mFirebaseDatabase.child("longitude").setValue(longitude1);

            return null;
        }
    }

}
