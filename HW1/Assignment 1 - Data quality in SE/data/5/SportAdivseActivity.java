package app.zyla.activities;

import android.graphics.drawable.Drawable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.RelativeLayout;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

import app.zyla.R;

public class SportAdivseActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sport_adivse);

        RelativeLayout layout = (RelativeLayout) findViewById(R.id.activity_sport_adivse);

        Drawable bg = getResources().getDrawable( R.drawable.bg1 );
        layout.setBackground(bg);

        List<String> citations = Arrays.asList(getResources().getStringArray(R.array.famous_sport_citations));
        Random randomizer = new Random();
        String randomCitation = citations.get(randomizer.nextInt(citations.size()));

        TextView textCitation = (TextView) findViewById(R.id.textCitation);
        textCitation.setText(randomCitation);

    }
}
