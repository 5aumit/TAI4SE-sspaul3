package com.otapp.net.Events.Adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.otapp.net.R;
import com.otapp.net.model.CountryCodePojo;

import java.util.List;

public class CountryCodeListAdapter extends BaseAdapter {
    private Context context; //context
    private List<CountryCodePojo.CountryCode> countryCodes=null;

    public CountryCodeListAdapter(Context context, List<CountryCodePojo.CountryCode> countryCodes) {
        this.context = context;
        this.countryCodes = countryCodes;
    }

    @Override
    public int getCount() {
        return countryCodes.size();
    }

    @Override
    public Object getItem(int position) {
        return countryCodes.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).
                    inflate(R.layout.country_code_list, parent, false);
        }
        TextView textViewCoutryName=convertView.findViewById(R.id.tvCountryName);
        TextView textViewCoutryCode=convertView.findViewById(R.id.tvCountryCode);

        textViewCoutryCode.setText(countryCodes.get(position).code);
       textViewCoutryName.setText(countryCodes.get(position).name);

        return convertView;
    }
}
