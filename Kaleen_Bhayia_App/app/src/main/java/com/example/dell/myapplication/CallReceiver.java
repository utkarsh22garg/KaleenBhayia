package com.example.dell.myapplication;

import android.content.Context;
import android.media.MediaPlayer;
import android.os.AsyncTask;
import android.speech.tts.TextToSpeech;
import android.telephony.mbms.MbmsErrors;
import android.util.Log;

import java.util.Date;
import java.util.Locale;

public class CallReceiver extends PhonecallReceiver {
    TextToSpeech tts;
    Context context_1;

    @Override
    protected void onIncomingCallReceived(Context ctx, String number, Date start)
    {
        Log.e("TAGG","Incomming callreceived");
    }

    @Override
    protected void onIncomingCallAnswered(Context ctx, String number,String name, Date start)
    {
        Log.e("TAGG","Incomming callanswered"+name);
        context_1=ctx;
    }


    @Override
    protected void onIncomingCallEnded(Context ctx, String number, Date start, Date end)
    {
        Log.e("TAGG","Incomming callEnded");
    }

    @Override
    protected void onOutgoingCallStarted(Context ctx, String number, Date start)
    {
        Log.e("TAGG","outgoing callstarted");
    }

    @Override
    protected void onOutgoingCallEnded(Context ctx, String number, Date start, Date end)
    {
        Log.e("TAGG","outgoing call ended");
    }

    @Override
    protected void onMissedCall(Context ctx, String number, Date start)
    {
        Log.e("TAGG","missed call");
    }



}
