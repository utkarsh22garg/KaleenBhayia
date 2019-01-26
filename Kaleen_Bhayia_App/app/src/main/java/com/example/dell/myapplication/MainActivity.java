package com.example.dell.myapplication;
import android.Manifest;
import android.content.Context;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationManager;
import android.media.MediaPlayer;
import android.os.AsyncTask;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

public class MainActivity extends AppCompatActivity {
    TextView text,textView;
    EditText name1,mailid1,p11,p22,p33;
    Button save;
    SharedPreferences sp;
    String p111,p222,p333;
    public static String name="no name";
    public static String mailid="no mail";
    String latitude1,longitude1;
    public static int updateflag=0;
    DatabaseReference databaseReference;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        text = findViewById(R.id.text);
        name1 = findViewById(R.id.editText);
        save = findViewById(R.id.save);
        mailid1=findViewById(R.id.mail);
        textView=findViewById(R.id.textView);
        p11=findViewById(R.id.p1);
        p22=findViewById(R.id.p2);
        p33=findViewById(R.id.p3);
        SharedPreferences prefs = getSharedPreferences("user", MODE_PRIVATE);
        name = prefs.getString("name", "no_name");
        mailid=prefs.getString("mail","no_mail");
        SharedPreferences pref = getSharedPreferences("emergency", MODE_PRIVATE);
        p111 = pref.getString("person1", "no_name");
        p222=pref.getString("person2","no_mail");
        p333=pref.getString("person3","no_mail");



        if(name.contains("no_name")) {
            save.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    name = name1.getText().toString();
                    mailid = mailid1.getText().toString();
                    p111=p11.getText().toString();
                    p222=p22.getText().toString();
                    p333=p33.getText().toString();
                    if (name.equals("") || mailid1.equals("") || mailid.contains("#") || mailid.contains(".") || mailid.contains("$") || mailid.contains("[") || mailid.contains("]")||p111.length()!=10||p222.length()!=10||p333.length()!=10) {
                        Toast.makeText(getApplicationContext(), "Please Enter Name ,gmail username and emergency contacts correctly", Toast.LENGTH_LONG).show();
                    } else {
                        try {
                            SharedPreferences.Editor editor = getSharedPreferences("user", MODE_PRIVATE).edit();
                            editor.putString("name", name);
                            editor.putString("mail", mailid);
                            editor.apply();
                            DatabaseReference mFirebaseDatabase;
                            FirebaseDatabase mFirebaseInstance;
                            mFirebaseInstance = FirebaseDatabase.getInstance();
                            mFirebaseDatabase = mFirebaseInstance.getReference();
                            mFirebaseDatabase.child("person1").setValue(p111);
                            mFirebaseDatabase.child("person2").setValue(p222);
                            mFirebaseDatabase.child("person3").setValue(p333);
                            SharedPreferences.Editor editor1 = getSharedPreferences("emergency", MODE_PRIVATE).edit();
                            editor1.putString("person1", p111);
                            editor1.putString("person2", p222);
                            editor1.putString("person3", p333);
                            editor1.apply();
                            Toast.makeText(getApplicationContext(), "Credentials saved successfully", Toast.LENGTH_LONG).show();
                            mailid1.setVisibility(View.GONE);
                            name1.setVisibility(View.GONE);
                            save.setVisibility(View.GONE);
                            p11.setVisibility(View.GONE);
                            p22.setVisibility(View.GONE);
                            p33.setVisibility(View.GONE);
                            textView.setVisibility(View.GONE);
                            friendlocation();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }

                    //
                    //  MyFirebaseInstanceIDService fb=new MyFirebaseInstanceIDService();
                    // fb.friendlocation();
                }
            });
        }
        else
        {
            mailid1.setVisibility(View.GONE);
            name1.setVisibility(View.GONE);
            save.setVisibility(View.GONE);
            p11.setVisibility(View.GONE);
            p22.setVisibility(View.GONE);
            p33.setVisibility(View.GONE);
            textView.setVisibility(View.GONE);
            try {
                friendlocation();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }




    }
    public  void friendlocation() throws InterruptedException {
        name=MainActivity.name;

        // SharedPreferences sp=getSharedPreferences("friends",MODE_PRIVATE);
//        if(sp!=null) {
//            name =
//            Log.d("TAGGG", "friendlocation: "+name);
//        }
        getcoordi();
        Log.e("TAGGGGGGG", "location:"+latitude1+" "+"longitude "+longitude1 );
        if(updateflag==0)
        {
            new PushFriendsBackground().execute();
        }
        else{

            update();
        }





    }
    public void update() throws InterruptedException {
        databaseReference=FirebaseDatabase.getInstance().getReference("friends").child(mailid);
        new PushFriendsBackground().execute();

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
                    latitude1 = String.valueOf(location.getLatitude());
                    longitude1 = String.valueOf(location.getLongitude());
                }
            }
        }
    }


    public class PushFriendsBackground extends AsyncTask {

        @Override
        protected Object doInBackground(Object[] objects) {
//            DatabaseReference mDatabase = FirebaseDatabase.getInstance().getReference("users");
//            String userId = mDatabase.push().getKey();
            FriendLocation fl = new FriendLocation(latitude1, longitude1, name);
//            mDatabase.child(userId).setValue(fl);
            if (updateflag == 0) {
                updateflag = 1;
                DatabaseReference mFirebaseDatabase;
                FirebaseDatabase mFirebaseInstance;
                mFirebaseInstance = FirebaseDatabase.getInstance();
                mFirebaseDatabase = mFirebaseInstance.getReference();
                DatabaseReference newRef = mFirebaseDatabase.child("friends").child(mailid);
                newRef.setValue(fl);
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

            } else {

                databaseReference.setValue(fl);
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            return null;
        }

        @Override
        protected void onPostExecute(Object o) {
            try {
                friendlocation();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            super.onPostExecute(o);
        }
    }

}