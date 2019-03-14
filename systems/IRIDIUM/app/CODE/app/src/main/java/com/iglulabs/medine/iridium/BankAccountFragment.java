package com.iglulabs.medine.iridium;

import android.app.ProgressDialog;
import android.content.Context;
import android.os.Bundle;
import android.provider.SyncStateContract;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import com.google.gson.JsonObject;
import com.koushikdutta.async.future.FutureCallback;
import com.koushikdutta.ion.Ion;
import com.koushikdutta.ion.Response;

import org.json.JSONObject;

public class BankAccountFragment extends Fragment {

    ActionBar actionBar;
    EditText bankAccUserName, bankAccPassword, bankAccBranch, bankAccCity, bankAccPinCode,
            bankAccState, bankAccBalance;
    Spinner bankAccBankName;

    public BankAccountFragment() {}

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        actionBar = ((AppCompatActivity) getActivity()).getSupportActionBar();
        if (actionBar != null) {
            actionBar.setTitle(R.string.action_bank_account);
        }

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        // Inflate the layout for this fragment
        View view =  inflater.inflate(R.layout.fragment_bank_account, container, false);
        Spinner spinner = (Spinner) view.findViewById(R.id.credit_card_bank_spinner);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(getActivity(),
                R.array.planets_array, android.R.layout.simple_spinner_item);
        // Specify the layout to use when the list of choices appears
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        // Apply the adapter to the spinner
        spinner.setAdapter(adapter);

        bankAccUserName  = (EditText) view.findViewById(R.id.bank_acc_user_name_id);
        bankAccPassword = (EditText) view.findViewById(R.id.bank_acc_user_password_id);
        bankAccBankName = (Spinner) view.findViewById(R.id.credit_card_bank_spinner);
        bankAccBranch = (EditText) view.findViewById(R.id.bank_acc_branch_id);
        bankAccCity = (EditText) view.findViewById(R.id.bank_acc_branch_city_id);
        bankAccPinCode = (EditText) view.findViewById(R.id.bank_acc_branch_pincode_id);
        bankAccState = (EditText) view.findViewById(R.id.bank_acc_branch_state_id);
        bankAccBalance = (EditText) view.findViewById(R.id.bank_acc_branch_balance_id);

        Button bankAccReg = (Button) view.findViewById(R.id.bank_acc_register_id);

        bankAccReg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean  validated = validateForm();
                Log.e(" validated"," "+validated);
                JsonObject json = new JsonObject();
                if (validated) {
                    json.addProperty("bank_user_name", bankAccUserName.getText().toString());
                    json.addProperty("bank_password", bankAccPassword.getText().toString());
                    json.addProperty("bank_branch", bankAccBranch.getText().toString());
                    json.addProperty("bank_city", bankAccCity.getText().toString());
                    json.addProperty("bank_pin_code", bankAccPinCode.getText().toString());
                    json.addProperty("bank_state", bankAccState.getText().toString());
                    json.addProperty("bank_balance", bankAccBalance.getText().toString());
                    json.addProperty("bank_name", bankAccBankName.getSelectedItem().toString());
                    postData(json);
                }
            }
        });
        return view;

    }


   public void postData(JsonObject json) {

        //String url = "http://iridium123.comxa.com/addBankDetails.php";
        String url = "http://192.168.1.9/Iridium/addBankDetails.php";
        Log.d("addProfileData", " json " + json.toString());
        Log.d("url", url);
        final ProgressDialog dlg = new ProgressDialog(getActivity());
        dlg.setTitle(R.string.loading_str);
        dlg.setIndeterminate(false);
        dlg.setProgressStyle(ProgressDialog.STYLE_SPINNER);
        dlg.show();
        Ion.with(getActivity())
                .load(url)
                .progressDialog(dlg)
                .setLogging("IonLogs", Log.VERBOSE)
                .setJsonObjectBody(json)
                .asJsonObject()
                .withResponse()
                .setCallback(new FutureCallback<Response<JsonObject>>() {
                    @Override
                    public void onCompleted(Exception e, Response<JsonObject> result) {
                        dlg.cancel();
                        if (e != null) {
                            Log.e("exception", "exception " + e);
                            return;
                        }

                        if (result.getHeaders() != null) {
                            if (result.getHeaders().code() == 200) {
                                JsonObject test = result.getResult();
                                if (test != null){
           //                           Log.e("addprofiledata","status "+test.get("status").getAsBoolean());
                                        Log.e("addBankDetails","addBankDetails"+test.getAsJsonObject());
                                        Toast.makeText(getActivity(),R.string.bank_acc_register_submit,Toast.LENGTH_SHORT).show();
                                        FragmentManager fragmentManager = getActivity().getSupportFragmentManager();
                                        int count = fragmentManager.getBackStackEntryCount() ;
                                        for(int i=0;i<count;i++){
                                            fragmentManager.popBackStack();
                                        }
                                        RefreshFragment reloadAct = new RefreshFragment(getActivity());
                                        reloadAct.reloadFragment(new BankAccountFragment(), fragmentManager);

                                }else {
                                    Log.e("test","test "+test);
                                }

                            }
                        }
                    }
                });
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

    //Validate the form
    public boolean validateForm() {

        String bankAccUserNameText = bankAccUserName.getText().toString();
        String bankAccPasswordText = bankAccPassword.getText().toString();
        String bankAccBankNameText = bankAccBankName.getSelectedItem().toString();
        String bankAccBranchText =   bankAccBranch.getText().toString();
        String bankAccCityText = bankAccCity.getText().toString();
        String bankAccPinCodeText = bankAccPinCode.getText().toString();
        String bankAccStateText = bankAccState.getText().toString();
        String bankAccBalanceText = bankAccBalance.getText().toString();

        boolean validated = true;

        if (bankAccUserNameText != null && bankAccUserNameText.length() < 4) {
            bankAccUserName.setError("please Enter valid user name");
            bankAccPassword.requestFocus();
            validated = false;

        }

        else if (bankAccPasswordText != null && bankAccPasswordText.length() < 4) {
            bankAccPassword.setError("please Enter valid user name");
            bankAccPassword.requestFocus();
            validated = false;
        }

        else if (bankAccBranchText != null && bankAccBranchText.length() < 4) {
            bankAccBranch.setError("please Enter valid user name");
            bankAccBranch.requestFocus();
            validated = false;
        }

        else if (bankAccCityText != null && bankAccCityText.length() < 4) {
            bankAccCity.setError("please Enter valid user name");
            bankAccCity.requestFocus();
            validated = false;
        }

        else if (bankAccPinCodeText != null && bankAccPinCodeText.length() < 4) {
            bankAccPinCode.setError("please Enter valid user name");
            bankAccPinCode.requestFocus();
            validated = false;
        }

        else if (bankAccStateText != null && bankAccStateText.length() < 4) {
            bankAccState.setError("please Enter valid user name");
            bankAccState.requestFocus();
            validated = false;
        }

        else if (bankAccBalanceText != null && bankAccBalanceText.length() < 4) {
            bankAccBalance.setError("please Enter valid user name");
            bankAccBalance.requestFocus();
            validated = false;
        }

        return  validated;
    }
}
