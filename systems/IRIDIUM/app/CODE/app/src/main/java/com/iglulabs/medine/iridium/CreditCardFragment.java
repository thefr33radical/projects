package com.iglulabs.medine.iridium;

import android.app.ProgressDialog;
import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
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


public class CreditCardFragment extends Fragment {

    ActionBar actionBar;
    EditText creditCardNumber, creditCardType, creditCardExpiry, creditCardCVV, creditCardPin;
    Spinner bankAccBankName;

    public CreditCardFragment() {}

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        actionBar = ((AppCompatActivity) getActivity()).getSupportActionBar();
        if (actionBar != null) {
            actionBar.setTitle(R.string.action_credit_card);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        // Inflate the layout for this fragment
        View view=  inflater.inflate(R.layout.fragment_credit_card, container, false);
        Spinner spinner = (Spinner) view.findViewById(R.id.credit_card_bank_spinner);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(getActivity(),
                R.array.planets_array, android.R.layout.simple_spinner_item);
        // Specify the layout to use when the list of choices appears
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        // Apply the adapter to the spinner
        spinner.setAdapter(adapter);

        creditCardNumber  = (EditText) view.findViewById(R.id.purchase_card_number_id);
        creditCardType  = (EditText) view.findViewById(R.id.card_type_id);
        creditCardExpiry  = (EditText) view.findViewById(R.id.purchase_expiry_date_id);
        creditCardCVV  = (EditText) view.findViewById(R.id.purchase_cvv_id);
        creditCardPin  = (EditText) view.findViewById(R.id.purchase_card_pin_id);
        bankAccBankName = (Spinner) view.findViewById(R.id.credit_card_bank_spinner);

        Button creditCardSubmit = (Button) view.findViewById(R.id.credit_card_submit);

        creditCardSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean  validated = validateForm();
                Log.e(" validated"," "+validated);
                JsonObject json = new JsonObject();

                if (validated) {
                    json.addProperty("credit_card_number", creditCardNumber.getText().toString());
                    json.addProperty("credit_card_type", creditCardType.getText().toString());
                    json.addProperty("credit_card_bank_name", bankAccBankName.getSelectedItem().toString());
                    json.addProperty("credit_card_exp_date", creditCardExpiry.getText().toString());
                    json.addProperty("credit_card_cvv", creditCardCVV.getText().toString());
                    json.addProperty("credit_card_pin", creditCardPin.getText().toString());
                    postData(json);
                }
            }
        });

        return view;
    }

    //Validate the form
    public boolean validateForm() {

        String creditCardNumberText = creditCardNumber.getText().toString();
        String creditCardTypeText = creditCardType.getText().toString();
        String bankAccBankNameText = bankAccBankName.getSelectedItem().toString();
        String creditCardExpiryText =   creditCardExpiry.getText().toString();
        String creditCardCVVText = creditCardCVV.getText().toString();
        String creditCardPinText = creditCardPin.getText().toString();

        boolean validated = true;

        if (creditCardNumberText != null && creditCardNumberText.length() < 4) {
            creditCardNumber.setError("please Enter valid card number");
            creditCardNumber.requestFocus();
            validated = false;
        }
        else if (creditCardTypeText != null && creditCardTypeText.length() < 2) {
            creditCardType.setError("please Enter valid card type");
            creditCardType.requestFocus();
            validated = false;
        }
        else if (creditCardExpiryText != null && creditCardExpiryText.length() < 4) {
            creditCardExpiry.setError("please Enter valid  expiry date");
            creditCardExpiry.requestFocus();
            validated = false;
        }
        else if (creditCardCVVText != null && creditCardCVVText.length() < 2) {
            creditCardCVV.setError("please Enter valid cvv");
            creditCardCVV.requestFocus();
            validated = false;
        }
        else if (creditCardPinText != null && creditCardPinText.length() < 4) {
            creditCardPin.setError("please Enter valid pin");
            creditCardPin.requestFocus();
            validated = false;
        }
        return  validated;
    }



    public void postData(JsonObject json) {

        //String url = "http://iridium123.comxa.com/addBankDetails.php";
        String url = "http://192.168.1.9/Iridium/creditCard.php";
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
                                    Toast.makeText(getActivity(),R.string.credit_card_form_submit,Toast.LENGTH_SHORT).show();
                                    FragmentManager fragmentManager = getActivity().getSupportFragmentManager();
                                    int count = fragmentManager.getBackStackEntryCount() ;
                                    for(int i=0;i<count;i++){
                                        fragmentManager.popBackStack();
                                    }
                                    RefreshFragment reloadAct = new RefreshFragment(getActivity());
                                    reloadAct.reloadFragment(new CreditCardFragment(), fragmentManager);

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


}
