package com.iglulabs.medine.iridium;

import android.app.Activity;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;

/**
 * Created by admin on 4/16/2016.
 */
public class RefreshFragment {

    public Activity mActivity;
    public RefreshFragment(Activity activity){
        mActivity = activity;
    }

    public void reloadFragment(Fragment reloadFrag, FragmentManager fragmentManager) {

        fragmentManager.beginTransaction()
                .replace(R.id.fragment, reloadFrag)
                .addToBackStack(null)
                .commit();

    }
}
