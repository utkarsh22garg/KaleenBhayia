package com.example.dell.myapplication;

import android.media.MediaPlayer;
import android.os.AsyncTask;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

import java.io.BufferedReader;

public class Player extends AppCompatActivity {
    MediaPlayer mPlayer;
    Button playerStop;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_player);
        playerStop=findViewById(R.id.stop);
        this.Player_alarm();
        playerStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mPlayer.stop();
                new Back().execute();
            }
        });
    }

    public void Player_alarm()
    {
        mPlayer = MediaPlayer.create(this, R.raw.lostphone);
        mPlayer.setLooping(true);
        mPlayer.start();

    }
    public class Back extends AsyncTask
    {

        @Override
        protected Object doInBackground(Object[] objects) {
            try {
                Thread.sleep(200);
                finish();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            return null;
        }
    }
}
