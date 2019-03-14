package com.iglulabs.medine.iridium;

import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Canvas;
import android.graphics.drawable.Drawable;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.RecyclerView.ItemDecoration;
import android.view.View;

public class SavedListDecoration extends ItemDecoration {

    private static final int[] ATTRS = { android.R.attr.listDivider};
    private Drawable mDivider;

    public SavedListDecoration(Context context) {
        TypedArray a = context.obtainStyledAttributes(ATTRS);
        mDivider = a.getDrawable(0);
        a.recycle();

    }
    
    @Override
    public void onDraw(Canvas c, RecyclerView parent) {
      
      /* final int childCount = parent.getChildCount();
       
       for (int i = 0; i < childCount; i++) {
    	   	View child = parent.getChildAt(i);
      }*/
   }
   
    @Override
    public void onDrawOver(Canvas c, RecyclerView parent) {

        int left = parent.getPaddingLeft();
        int right = parent.getWidth() - parent.getPaddingRight();

        int childCount = parent.getChildCount();

        for (int i = 0; i < childCount; i++) {

            View child = parent.getChildAt(i);

            RecyclerView.LayoutParams params = (RecyclerView.LayoutParams) child .getLayoutParams();

            int top = child.getBottom() + params.bottomMargin;
            int bottom = top + mDivider.getIntrinsicHeight();

            mDivider.setBounds(left, top, right, bottom);
            mDivider.draw(c);
            
           /* TextView rowTypeTextView  = (TextView)child.findViewById(R.id.rowType);
		    if ( rowTypeTextView.getText().toString().equals("1")) { //Header
		    	  child.setBackgroundColor(Color.parseColor("#ffecb3"));
		     }	  
		     else if (rowTypeTextView.getText().toString().equals("2") || rowTypeTextView.getText().toString().equals("3")) {  //Footer
		    	  child.setBackgroundColor(Color.parseColor("#ccff90")); 
		     }
		     else{
		    	  //child.setBackgroundColor(Color.parseColor("#FFFFFF"));
		    	  child.setBackgroundColor(Color.parseColor("#ccff90"));
		     } */
        }
    }
    
    
}
