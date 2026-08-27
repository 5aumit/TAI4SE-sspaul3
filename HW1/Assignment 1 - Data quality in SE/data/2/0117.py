# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:47:30 2019
Title: MP4-Medical Image Processing
@author: MP4 Team

"""

# Validate window controller
class ValidateWindowCtr(object):
    # Initialization
    def __init__(self, fig, im_trans, im_truth, im_segmen, vol_trans, vol_truth, vol_segmen, ax_trans, ax_truth, ax_segmen, index_trans, index_truth, index_segmen):
        self.fig = fig
        self.im_trans, self.im_truth, self.im_segmen = im_trans, im_truth, im_segmen
        self.vol_trans, self.vol_truth, self.vol_segmen = vol_trans, vol_truth, vol_segmen
        self.ax_trans, self.ax_truth, self.ax_segmen = ax_trans, ax_truth, ax_segmen
        self.index_trans, self.index_truth, self.index_segmen = index_trans, index_truth, index_segmen
        
        self.txt_trans = self.ax_trans.text(0, 600, 'Slice No: '+str(self.index_trans[-1]), color='b')
        self.txt_truth = self.ax_truth.text(0, 10, 'Slice No: '+str(self.index_truth[-1]), color='b')
        self.txt_segmen = self.ax_segmen.text(0, 600, 'Slice No: '+str(self.index_segmen[-1]), color='b')
        
        self.scroll_trans = None
        self.scroll_truth = None
        self.scroll_segmen = None
        self.fig.canvas.mpl_connect('axes_enter_event', self.fig_enter_event)
        self.fig.canvas.mpl_connect('axes_leave_event', self.fig_leave_event)
        
    # Enable scrolling image
    def fig_enter_event(self, event):
        if self.ax_trans.in_axes(event):
            self.scroll_trans = self.fig.canvas.mpl_connect('scroll_event', self.trans_subplot_scroll)
            
        elif self.ax_truth.in_axes(event):
            self.scroll_truth = self.fig.canvas.mpl_connect('scroll_event', self.truth_subplot_scroll)
            
        elif self.ax_segmen.in_axes(event):
            self.scroll_segmen = self.fig.canvas.mpl_connect('scroll_event', self.segmen_subplot_scroll)
            
    # Disable scrolling image
    def fig_leave_event(self, event):
        self.fig.canvas.mpl_disconnect(self.scroll_trans)
        self.fig.canvas.mpl_disconnect(self.scroll_truth)
        self.fig.canvas.mpl_disconnect(self.scroll_segmen)
        
    # Scroll voxel image
    def trans_subplot_scroll(self, event):       
        if event.button == 'down' and (self.index_trans[-1] > -1*self.vol_trans.shape[0]):
            self.index_trans[-1] -= 1
            
        if event.button == 'up' and (self.index_trans[-1] < self.vol_trans.shape[0]-1):
            self.index_trans[-1] += 1
            
        self.im_trans.set_data(self.vol_trans[self.index_trans[-1]])
        self.txt_trans.set_text('Slice No: '+str(self.index_trans[-1]))
        self.fig.canvas.draw_idle()
    
    # Scroll ground truth image
    def truth_subplot_scroll(self, event):       
        if event.button == 'down' and (self.index_truth[-1] > -1*self.vol_truth.shape[0]):
            self.index_truth[-1] -= 1
            
        if event.button == 'up' and (self.index_truth[-1] < self.vol_truth.shape[0]-1):
            self.index_truth[-1] += 1
            
        self.im_truth.set_data(self.vol_truth[self.index_truth[-1]])
        self.txt_truth.set_text('Slice No: '+str(self.index_truth[-1]))
        self.fig.canvas.draw_idle()
    
    # Scroll segmented image
    def segmen_subplot_scroll(self, event):       
        if event.button == 'down' and (self.index_segmen[-1] > -1*self.vol_segmen.shape[0]):
            self.index_segmen[-1] -= 1
            
        if event.button == 'up' and (self.index_segmen[-1] < self.vol_segmen.shape[0]-1):
            self.index_segmen[-1] += 1
            
        self.im_segmen.set_data(self.vol_segmen[self.index_segmen[-1]])
        self.txt_segmen.set_text('Slice No: '+str(self.index_segmen[-1]))        
        self.fig.canvas.draw_idle()
        