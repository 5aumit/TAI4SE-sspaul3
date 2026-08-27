#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyautogui
#import random
from random import randint
import cv2
import h5py
import numpy as np
from matplotlib import pyplot as plt
from pylab import *
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.backends.backend_tkagg as tkagg

import numpy as np

from TaskerOrbitPlotter2 import TaskerOrbitPlotter
from datetime import datetime, timedelta


trace = 0
plotButton = False
raster = "default"

        
class TaskerCanvas(ttk.Frame):
    """
    Displays the map and plot

    :ivar TaskerGui parent: The parent application
    :ivar int canvas_width: The width of the canvas
    :ivar int canvas_height: The height of the canvas
    :ivar TaskerOrbitPlotter plotter: Manages orbit data and plotting for the canvas
    :ivar FigureCanvasTkAgg canvas: The canvas

    :param int width: The desired width of the canvas
    :param int height: The desired height of the canvas
    """
    def __init__(self, mainframe, width=500, height=500):
        ttk.Frame.__init__(self, master=mainframe)

        self.parent = mainframe
        
        # Vertical and horizontal scrollbars for canvas
        vbar = tk.Scrollbar(self, orient='vertical')
        hbar = tk.Scrollbar(self, orient='horizontal')
        
        # Create canvas and put map on it
        self.canvas_width = width
        self.canvas_height = height

        self.plotter = TaskerOrbitPlotter(self)
        fig = self.plotter.show()
        t = np.arange(0, 3, .01)
        self.canvas = FigureCanvasTkAgg(fig, master = mainframe)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top",fill=tk.BOTH,expand=True)

    def enableZoomIn(self):
        """
        Enables zooming in when clicking on the map and changes the cursor.
        """
        self.zoomInID = self.canvas.mpl_connect('button_press_event', self.onZoomIn)
        self.master.config(cursor = "cross")

    def disableZoomIn(self):
        """
        Disables zooming in. Changes cursor back to normal.
        """
        self.canvas.mpl_disconnect(self.zoomInID)
        self.master.config(cursor = "arrow")

    def enableZoomOut(self):
        """
        Enables zooming out when clicking on the map and changes the cursor.
        """
        self.zoomOutID = self.canvas.mpl_connect('button_press_event', self.onZoomOut)
        self.master.config(cursor = "cross")

    def disableZoomOut(self):
        """
        Disables zooming out. Changes cursor back to normal.
        """
        self.canvas.mpl_disconnect(self.zoomOutID)
        self.master.config(cursor = "arrow")

    
    def onZoomIn(self, event):
        """
        Called when the map is clicked. Zooms in on the quadrant clicked on.
        """
        try:
            print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
                ('double' if event.dblclick else 'single', event.button,
                event.x, event.y, event.xdata, event.ydata))
        except:
            return


        self.plotter.zoomIn(event)

    def onZoomOut(self, event):
        """
        Called when the map is clicked. Zooms out by one zoom level.
        """
        self.plotter.zoomOut(event)
            
    def on_resize_parent(self,event):
        """
        Called when app is resized
        """
        #print("parent event size="+str(event.width)+" X "+str(event.height))
        self.canvas_width = event.width
        self.canvas_height = event.height
        self.canvas.get_tk_widget().config(width=self.canvas_width, height=self.canvas_height)
        self.show_image()
        
    def on_resize_parentx(self,event):
        """
        Called only by Panedwindow to resize in x-dir only.
        """
        ##print("parent event size="+str(event.width)+" X "+str(event.height))
        self.canvas_width = event.width
        self.canvas.get_tk_widget().config(width=self.canvas_width)
        self.show_image()
 
    def event_subscribe(self, obj_ref):
        """
        Subscribes obj_ref to the TaskerGui.

        :param obj_ref: object to be subscribed to TaskerGui
        """
        self.subscribers.append(obj_ref)
    
    def event_publish(self, cmd):
        """
        Publishes an event to all subscribers

        :param str cmd: Command to be published
        """
        for sub in self.subscribers:
            sub.event_receive(cmd)
    
    def event_receive(self,event):
        """
        Receives an event from a subscription

        :param event: The event received from a subscription
        """

        pass