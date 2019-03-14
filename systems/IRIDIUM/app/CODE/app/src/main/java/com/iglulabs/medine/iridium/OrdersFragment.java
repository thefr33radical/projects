package com.iglulabs.medine.iridium;

import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.util.ArrayList;
import java.util.HashMap;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * {@link OrdersFragment.OnFragmentInteractionListener} interface
 * to handle interaction events.
 * Use the {@link OrdersFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class OrdersFragment extends Fragment {

    ActionBar actionBar;
    public static ArrayList<HashMap<String, String>> showSavedListArray;
    public static RecyclerView mShowSavedItemListView;
    public static MyOrdersRecycleAdapter mOrderItemListAdapter;
    public static RecyclerView.LayoutManager mShowSavedListLayoutManager;
    public static RecyclerView.ItemDecoration mShowSavedLayoutManager;

    public OrdersFragment() {}

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        actionBar = ((AppCompatActivity) getActivity()).getSupportActionBar();
        if (actionBar != null) {
            actionBar.setTitle(R.string.action_my_orders);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View view =  inflater.inflate(R.layout.fragment_orders, container, false);

        mShowSavedItemListView = (RecyclerView) view.findViewById(R.id.my_orders_list);
        mShowSavedListLayoutManager = new LinearLayoutManager(getActivity());
        mShowSavedItemListView.setLayoutManager(mShowSavedListLayoutManager);
        showSavedListArray = new ArrayList<HashMap<String, String>>() ;
        addTempData();

        mOrderItemListAdapter = new MyOrdersRecycleAdapter(showSavedListArray);
        mShowSavedItemListView.setAdapter(mOrderItemListAdapter);

        mShowSavedLayoutManager = new SavedListDecoration(getActivity());
        mShowSavedItemListView.addItemDecoration(mShowSavedLayoutManager);
        mShowSavedItemListView.setItemAnimator(new DefaultItemAnimator());

        return view;
    }


    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
    }

    @Override
    public void onDetach() {
        super.onDetach();
        if (actionBar != null) {
            actionBar.setTitle(R.string.app_name);
        }
    }

    //Adding the test data
    private void addTempData(){

        for(int i=0; i<100; i++) {
            HashMap<String, String> addNewItem = new HashMap<String, String>();
            addNewItem.put(Constants.SAVED_TEXT_DETAIL, "Shivaraj,22,22");
            addNewItem.put(Constants.SAVED_TEXT_COUNT, "2");
            showSavedListArray.add(addNewItem);
        }
    }
}
