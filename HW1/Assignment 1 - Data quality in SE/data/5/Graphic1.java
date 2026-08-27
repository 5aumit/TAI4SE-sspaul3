//imports
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Graphic1 extends JPanel {

public void paintComponent (Graphics gWin) {
  
  //declare variables
  String stryear;//will use to draw years on graph
  String strvalue;//will use to draw mortage values on graph
  int intdiv;//will use this to convert yearly mortage values to a smaller number that 
  int yspace = 625;//the posistion where we will start graphing horizontal lines
  int xspace = 45;//the posistion where we will start graphing vertical lines
  int intcnt = 0;//use this to go through every index in the intYptarr
  
  int intYptarr[] = ICS_SAD_STATS_Q1.returnArray();//recieve values from ICS_SAD_STATS_Q1 class and store them into array

   super.paintComponent (gWin); //setup up a paint componenent that will let you draw on jframe
   //set two different font styles
   Font one = new Font("Calbri" , Font.PLAIN, 8);
   Font two = new Font("Calbri" , Font.PLAIN, 5);
   
   this.setBackground (Color.WHITE);//set background color to white

   gWin.setColor (Color.BLACK); //setup what color you will draw by setting gWin to a specific color
   
   //create the the x and y axis by using the fillrect commmand on gWin which creates shapes
   //of specific sizes at specific posistion based on what the user enters for the x and y posistion
   //and size of the x and y for shape.
   gWin.fillRect(25, 625, 1250, 5);
   gWin.fillRect(25, 0, 5, 625); 
   
   gWin.setFont(two);//set the font will you use
   
   //scale used in for loop
   for(int value = 250000; value <= 3000000; value = value + 250000)//use for loop to plot horizontal lines and y values on graph 
   {
     strvalue = Integer.toString(value);//convert strvalue to string
     yspace = yspace  - 50;//decrease yspace to move down horizontal lines on the graph
     gWin.drawString(strvalue, 2,yspace + 4);//put values  on the y axis
     gWin.fillRect(25, yspace, 1500, 1);//plot horizontal lines on graph
   }  
  
   gWin.setFont(one);//set the font you will use
   
   //scale used in for loop
   for(int year = 1982; year <= 2018; year++)//use for loop to put years/bars/points/lines and vertical lines on graph
   {
      stryear = Integer.toString(year);//convert year to string to plot on graph 
      gWin.drawString(stryear, xspace + 4, 650);//put stryear on graph under x axis
       
      xspace = xspace  + 33;//increase xspace to space out years and vertical gridlines on graph
      gWin.fillRect(xspace - 24, 0, 1, 625);//create vertical gridlines
      intdiv = (intYptarr[intcnt])/5000;//convert intYptarr to smaller sizes to plot  and match scale on graph
      
      gWin.setColor (Color.RED);//set color to red
      gWin.fillRect( xspace - 25, 625 - intdiv , 8, intdiv);//plot the bars on the graph
     
      gWin.setColor (Color.GREEN);//set color to Green
      gWin.fillRect( xspace - 24, 625 - intdiv, 5, 5);//plot the points on the graph
       
      if (year > 1982)//checks to see if we pass first year
       {
         gWin.setColor(Color.BLUE);//set color to blue
         gWin.drawLine((xspace - 33) - 24, 625 - ((intYptarr[intcnt - 1])/5000), xspace - 24, 625 - intdiv);//plot the lines on the graph which connect all the points toghter
         // to draw a line between two points we will subtract the previous x,y componets with the new x,y componets and divide by the value of x by the value of y to find slope
         //the commmmand drawline will draw the slope on the graph or in other terms the line connecting two points toghter
      }
      
      intcnt++;//increase intcnt by 1 to go to next year
      gWin.setColor (Color.BLACK);//set color to black
   }
  

} 
}
