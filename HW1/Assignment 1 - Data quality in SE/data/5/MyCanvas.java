package com.example.magicball;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.os.Build;
import android.util.AttributeSet;
import android.view.View;

public class MyCanvas extends View {
    private Panel mPanel=new Panel(this);
    private float x,y;

    public MyCanvas(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    @Override
    protected void onLayout(boolean changed, int left, int top, int right, int bottom) {
        super.onLayout(changed, left, top, right, bottom);
        mPanel.max_height=getMeasuredHeight()-Panel.height;
        mPanel.max_width=getMeasuredWidth()-Panel.width;
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        Paint p=new Paint();
        p.setStrokeWidth(5);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            canvas.drawOval(x, y, x+mPanel.width, y+mPanel.height,p);
        }
        mPanel.paint();
    }

    public void preDraw(double x,double y){
        this.x=(float)x;
        this.y=(float)y;
        invalidate();
    }
}
