// 
// Decompiled by Procyon v0.5.30
// 

package de.cisha.android.board.video.model.filter;

import android.content.res.Resources;

public class PriceSettingItem implements SettingItem
{
    private int _priceCat;
    
    public PriceSettingItem(final int priceCat) {
        this._priceCat = priceCat;
    }
    
    private static String getTitleFromCat(final int n) {
        switch (n) {
            default: {
                return "";
            }
            case 3: {
                return "## 15 - 20 eur ##";
            }
            case 2: {
                return "## 10 - 15 Eur ##";
            }
            case 1: {
                return "## 5 - 10 Eur ##";
            }
            case 0: {
                return "## 0 - 5 Eur ##";
            }
        }
    }
    
    @Override
    public String getTitle(final Resources resources) {
        return getTitleFromCat(this._priceCat);
    }
}
