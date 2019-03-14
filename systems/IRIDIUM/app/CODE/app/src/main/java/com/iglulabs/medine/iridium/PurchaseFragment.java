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
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Spinner;
import android.widget.Toast;

import com.google.gson.JsonObject;
import com.koushikdutta.async.future.FutureCallback;
import com.koushikdutta.ion.Ion;
import com.koushikdutta.ion.Response;

public class PurchaseFragment extends Fragment {

    ActionBar actionBar;
    public PurchaseFragment() {}

    EditText purchaseCardNumber, purchaseNameOnCard, purchaseExpiryDate, purchaseCardCVV, purchaseCardPin;
    Spinner bankAccBankName;
    RadioGroup radioProductsId;
    RadioButton radioProductButton ;


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        actionBar = ((AppCompatActivity) getActivity()).getSupportActionBar();
        if (actionBar != null) {
            actionBar.setTitle(R.string.action_purchase);
        }

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        // Inflate the layout for this fragment
        final  View view=  inflater.inflate(R.layout.fragment_purchase, container, false);
        Spinner spinner = (Spinner) view.findViewById(R.id.credit_card_bank_spinner);

        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(getActivity(),
                R.array.planets_array, android.R.layout.simple_spinner_item);
        // Specify the layout to use when the list of choices appears
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        // Apply the adapter to the spinner
        spinner.setAdapter(adapter);

        purchaseCardNumber = (EditText) view.findViewById(R.id.purchase_card_number_id);
        purchaseNameOnCard = (EditText) view.findViewById(R.id.name_on_card_id);
        purchaseExpiryDate = (EditText) view.findViewById(R.id.purchase_expiry_date_id);
        purchaseCardCVV = (EditText) view.findViewById(R.id.purchase_cvv_id);
        purchaseCardPin = (EditText) view.findViewById(R.id.purchase_card_pin_id);
        bankAccBankName = (Spinner) view.findViewById(R.id.credit_card_bank_spinner);

        radioProductsId = (RadioGroup) view.findViewById(R.id.products_id);
        radioProductsId.check(R.id.products_id1);

        Button purchaseSubmit = (Button) view.findViewById(R.id.purchase_submit);

        purchaseSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean  validated = validateForm();
                Log.e(" validated"," "+validated);
                JsonObject json = new JsonObject();
                int selectedId = radioProductsId.getCheckedRadioButtonId();
                radioProductButton = (RadioButton) view.findViewById(selectedId);
                Toast.makeText(getActivity(), radioProductButton.getText().toString(), Toast.LENGTH_SHORT).show();
                final String productName = radioProductButton.getText().toString();

                if (validated) {
                    json.addProperty("purchase_card_number", purchaseCardNumber.getText().toString());
                    json.addProperty("purchase_name_on_Card", purchaseNameOnCard.getText().toString());
                    json.addProperty("purchase_expiry_date", purchaseExpiryDate.getText().toString());
                    json.addProperty("purchase_card_cvv", purchaseCardCVV.getText().toString());
                    json.addProperty("purchase_card_pin", purchaseCardPin.getText().toString());
                    json.addProperty("bank_name", bankAccBankName.getSelectedItem().toString());
                    json.addProperty("product_bought", productName);

                    postData(json);
                }
            }
        });

        return view;
    }



    //Validate the form
    public boolean validateForm() {

        String purchaseCardNumberText = purchaseCardNumber.getText().toString();
        String purchaseNameOnCardText = purchaseNameOnCard.getText().toString();
        String purchaseExpiryDateText =   purchaseExpiryDate.getText().toString();
        String purchaseCardCVVText = purchaseCardCVV.getText().toString();
        String purchaseCardPinText = purchaseCardPin.getText().toString();

        boolean validated = true;

        if (purchaseCardNumberText != null && purchaseCardNumberText.length() < 4) {
            purchaseCardNumber.setError("please Enter card number");
            purchaseCardNumber.requestFocus();
            validated = false;

        }

        else if (purchaseNameOnCardText != null && purchaseNameOnCardText.length() < 4) {
            purchaseNameOnCard.setError("please Enter valid name");
            purchaseNameOnCard.requestFocus();
            validated = false;
        }

        else if (purchaseExpiryDateText != null && purchaseExpiryDateText.length() < 4) {
            purchaseExpiryDate.setError("please Enter valid expiry date");
            purchaseExpiryDate.requestFocus();
            validated = false;
        }

        else if (purchaseCardCVVText != null && purchaseCardCVVText.length() < 3) {
            purchaseCardCVV.setError("please Enter valid cvv");
            purchaseCardCVV.requestFocus();
            validated = false;
        }

        else if (purchaseCardPinText != null && purchaseCardPinText.length() < 4) {
            purchaseCardPin.setError("please Enter valid pin");
            purchaseCardPin.requestFocus();
            validated = false;
        }
        return  validated;
    }

    public void postData(JsonObject json) {

        //String url = "http://iridium123.comxa.com/addBankDetails.php";
        String url = "http://192.168.1.9/Iridium/purchase.php";
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
                                    Toast.makeText(getActivity(),R.string.purchase_submit_text,Toast.LENGTH_SHORT).show();
                                    FragmentManager fragmentManager = getActivity().getSupportFragmentManager();
                                    int count = fragmentManager.getBackStackEntryCount() ;
                                    for(int i=0;i<count;i++){
                                        fragmentManager.popBackStack();
                                    }
                                    RefreshFragment reloadAct = new RefreshFragment(getActivity());
                                    reloadAct.reloadFragment(new PurchaseFragment(), fragmentManager);

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
