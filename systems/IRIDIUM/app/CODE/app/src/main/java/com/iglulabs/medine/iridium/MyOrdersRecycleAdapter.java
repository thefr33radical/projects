package com.iglulabs.medine.iridium;

import android.app.Activity;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by admin on 4/16/2016.
 */
public class MyOrdersRecycleAdapter extends RecyclerView.Adapter<MyOrdersRecycleAdapter.ViewHolder>   {

    public ArrayList<HashMap<String, String>> orderList;
    Activity mHostActivity;

    public MyOrdersRecycleAdapter(ArrayList<HashMap<String, String>> itemSearchArray) {
        this.orderList = itemSearchArray;
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        public View view;
        protected TextView savedTextDetails;
        protected TextView scanCount;

        public ViewHolder(View v) {
            super(v);
            savedTextDetails = (TextView) v.findViewById(R.id.saved_text_detail);
            scanCount = (TextView) v.findViewById(R.id.saved_text_count);
            view = v;
        }
    }

    @Override
    public int getItemCount() {
         return orderList.size();
    }

     @Override
     public ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {

         View inflaterView = LayoutInflater.from(parent.getContext()).inflate(R.layout.saved_location_list_column, parent, false);
         ViewHolder vh = new ViewHolder(inflaterView);

         return vh;

     }

     @Override
     public void onBindViewHolder(ViewHolder holder, final int position) {

         HashMap<String, String> map = orderList.get(position);
         holder.savedTextDetails.setText(map.get(Constants.SAVED_TEXT_DETAIL));
         holder.scanCount.setText(map.get(Constants.SAVED_TEXT_COUNT));
     }

}
