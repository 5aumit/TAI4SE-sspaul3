package id.co.pegadaian.diarium.controller.home.main_menu.mydevelopment.marketplace.PayActivity;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import com.google.android.material.tabs.TabLayout;

import id.co.pegadaian.diarium.R;
import id.co.pegadaian.diarium.adapter.ViewPagerAdapter;
import id.co.pegadaian.diarium.util.UserSessionManager;

public class TopUpActivity extends AppCompatActivity {

  private UserSessionManager session;
  TabLayout tabLayout;
  ViewPager viewPager;
  ViewPagerAdapter viewPagerAdapter;
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_top_up);


    tabLayout = findViewById(R.id.tabs);
    viewPager = findViewById(R.id.viewpager);

    viewPagerAdapter = new ViewPagerAdapter(TopUpActivity.this.getSupportFragmentManager());
    viewPagerAdapter.addFragments(new InstantFragment(),"Instant");
    viewPagerAdapter.addFragments(new InstructionFragment(),"Instruction");
//    viewPagerAdapter.addFragments(new AbsenFragment(),"Absensi");
    viewPager.setAdapter(viewPagerAdapter);
    tabLayout.setupWithViewPager(viewPager);




    getSupportActionBar().setDisplayHomeAsUpEnabled(true);
    getSupportActionBar().setTitle("Top Up");
  }

  @Override
  public boolean onSupportNavigateUp() {
    finish();
    return true;
  }
}
