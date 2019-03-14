package com.iglulabs.medine.iridium;



import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.ShareCompat;
import android.util.Log;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.TextView;

import com.daimajia.slider.library.SliderLayout;
import com.daimajia.slider.library.SliderTypes.TextSliderView;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    SliderLayout sliderShow;
    public SharedPreferences.Editor regPrefeditor;
    public SharedPreferences regPref;
    int userLogIn;
    MenuItem actionLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        regPref = getSharedPreferences("deviceInfo", 0); // 0 - for private mode
        regPrefeditor = regPref.edit();
        userLogIn = regPref.getInt("user_log_in", 1);
        Log.e("userLogIn","userLogIn "+userLogIn);
        if (userLogIn == 1) {
            Log.e("LogIn","user is not login");
        }else {
            Log.e("LogIn","user login");
        }

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);

        sliderShow = (SliderLayout) findViewById(R.id.slider);

        TextSliderView textSliderView1 = new TextSliderView(this);
        textSliderView1
                .description("Best Credit Card For You.")
                .image(R.drawable.first1);

        sliderShow.addSlider(textSliderView1);

        TextSliderView textSliderView2 = new TextSliderView(this);
        textSliderView2
                .description("Get Your Credit Card Today.")
                .image(R.drawable.second1);

        sliderShow.addSlider(textSliderView2);

        TextSliderView textSliderView3 = new TextSliderView(this);
        textSliderView3
                .description("Apply For Bank Account.")
                .image(R.drawable.third1);

        sliderShow.addSlider(textSliderView3);

        TextSliderView textSliderView4 = new TextSliderView(this);
        textSliderView4
                .description("We Provide Best Credit Card Service.")
                .image(R.drawable.fourth1);

        sliderShow.addSlider(textSliderView4);

     TextView applyCrdCard = (TextView) findViewById(R.id.home_app_crd_card_textview);

     applyCrdCard.setOnClickListener(new View.OnClickListener() {

         public void onClick(View v) {
            Log.e("applyCrdCard","applyCrdCard");
         }

        });

        TextView applyBnkAcc = (TextView) findViewById(R.id.home_app_bbk_acc_textView);

        applyBnkAcc.setOnClickListener(new View.OnClickListener() {

            public void onClick(View v) {
                Log.e("applyBnkAcc","applyBnkAcc");
            }

        });

    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        actionLogin = menu.findItem(R.id.action_login);

        if (userLogIn == 2) {
            actionLogin.setTitle(R.string.action_logout);
        }
        else {
            actionLogin.setTitle(R.string.action_login);
        }

        return true;
    }

    @Override
    protected void onStop() {
        sliderShow.stopAutoCycle();
        super.onStop();
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        int id = item.getItemId();
        //noinspection SimplifiableIfStatement
        if (id == R.id.action_login) {

            if (userLogIn != 2) {
                Intent intent = new Intent(this, LoginActivity.class);
                intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                finish();
                startActivity(intent);
            }
            else {
                regPrefeditor.putInt("user_log_in",1);
                regPrefeditor.commit();
                Log.e("Logout","logout");
                userLogIn = 1;
                actionLogin.setTitle(R.string.action_login);
                Intent intent = new Intent(this, LoginActivity.class);
                intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);
                finish();
                startActivity(intent);

            }
            //return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    protected void onResume() {
        userLogIn = regPref.getInt("user_log_in", 1);
        super.onResume();
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        int count = getSupportFragmentManager().getBackStackEntryCount() ;
        for(int i=0;i<count;i++){
            getSupportFragmentManager().popBackStack();
        }

        if (id == R.id.nav_about) {
            Log.e("about","about");
            Fragment newFragment = new AboutFragment();
            FragmentManager fragmentManager = getSupportFragmentManager();
            fragmentManager.beginTransaction()
                    .replace(R.id.fragment, newFragment)
                    .addToBackStack(null)
                    .commit();

        } else if (id == R.id.nav_purchase) {
            Log.e("nav_purchase","nav_purchase");
            Fragment newFragment = new PurchaseFragment();
            FragmentManager fragmentManager = getSupportFragmentManager();
            fragmentManager.beginTransaction()
                    .replace(R.id.fragment, newFragment)
                    .addToBackStack(null)
                    .commit();

        } else if (id == R.id.nav_bnk_accounts) {
            Log.e("nav_bnk_accounts","nav_bnk_accounts");
            Fragment newFragment = new BankAccountFragment();
            FragmentManager fragmentManager = getSupportFragmentManager();
            fragmentManager.beginTransaction()
                    .replace(R.id.fragment, newFragment, "bankAccFragment")
                    .addToBackStack(null)
                    .commit();

        } else if (id == R.id.nav_crd_cards) {
            Fragment newFragment = new CreditCardFragment();
            FragmentManager fragmentManager = getSupportFragmentManager();
            fragmentManager.beginTransaction()
                    .replace(R.id.fragment, newFragment)
                    .addToBackStack(null)
                    .commit();
            Log.e("nav_crd_cards","nav_crd_cards");
        }
        else if (id == R.id.nav_my_orders) {
            Fragment newFragment = new OrdersFragment();
            FragmentManager fragmentManager = getSupportFragmentManager();
            fragmentManager.beginTransaction()
                    .replace(R.id.fragment, newFragment)
                    .addToBackStack(null)
                    .commit();
            Log.e("nav_crd_cards","nav_crd_cards");
        }
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}