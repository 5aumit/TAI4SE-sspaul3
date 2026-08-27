package com.example.homepage.Adapter;
import android.content.Intent;
import android.graphics.Paint;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RatingBar;
import android.widget.RelativeLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.homepage.Activity.ShowDwnloadImageRvActivity;
import com.example.homepage.Activity.ShowMenzImageRv;
import com.example.homepage.R;
import com.example.homepage.phonehelper;
import com.example.homepage.productHelper2;
import com.example.homepage.productHelper5;

import java.util.ArrayList;

public class adapterProduct5 extends RecyclerView.Adapter<adapterProduct5.PhoneViewHold>  {

    ArrayList<productHelper5> phoneLaocations5;
    final private ListItemClickListener mOnClickListener;

    public adapterProduct5(ArrayList<productHelper5> phoneLaocations, ListItemClickListener listener) {
        this.phoneLaocations5=phoneLaocations;
        mOnClickListener = listener;
    }

    @NonNull

    @Override
    public PhoneViewHold onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.fifthrecycview, parent, false);
        return new PhoneViewHold(view);

    }

    @Override
    public void onBindViewHolder(@NonNull PhoneViewHold holder, int position) {


        productHelper5 phonehelper = phoneLaocations5.get(position);
        holder.image.setImageResource(phonehelper.getImage());
        holder.title.setText(phonehelper.getTitle());
        holder.oldPrice.setText(phonehelper.getOldprice());
        holder.newPrice.setText(phonehelper.getNewprice());
        holder.rating.setNumStars(phonehelper.getRating());
        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent=new Intent(v.getContext(), ShowMenzImageRv.class);
                v.getContext().startActivity(intent);
            }
        });







    }

    @Override
    public int getItemCount() {
        return phoneLaocations5.size();

    }

    public interface ListItemClickListener {
        void onphoneListClick(int clickedItemIndex);
    }

    public class PhoneViewHold extends RecyclerView.ViewHolder implements View.OnClickListener {


        ImageView image;
        TextView title;
        TextView oldPrice;
        TextView newPrice;
        RatingBar rating;
        RelativeLayout relativeLayout;


        public PhoneViewHold(@NonNull View itemView) {
            super(itemView);
            itemView.setOnClickListener(this);
            //hooks

            image = itemView.findViewById(R.id.phone_image5);

            title = itemView.findViewById(R.id.fifthrvttl);
            oldPrice = itemView.findViewById(R.id.previousPriceId);
            oldPrice.setPaintFlags(oldPrice.getPaintFlags() | Paint.STRIKE_THRU_TEXT_FLAG);
            newPrice = itemView.findViewById(R.id.newpriceId);
            rating= itemView.findViewById(R.id.ratingbar);


        }

        @Override
        public void onClick(View v) {
            int clickedPosition = getAdapterPosition();
            mOnClickListener.onphoneListClick(clickedPosition);
        }
    }

}