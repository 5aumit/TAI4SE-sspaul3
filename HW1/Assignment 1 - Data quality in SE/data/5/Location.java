package com.trainpuzzle.model.board;

public class Location implements java.io.Serializable {
	
	private static final long serialVersionUID = 1L;
	
	private int row;
	private int column;
	
	public Location(int row, int column) {
		this.row = row;
		this.column = column;
	}
	public Location(Location location) {
		this.row = location.getRow();
		this.column = location.getColumn();
	}
	
	@Override
	public boolean equals(Object object) {
		if(object == null) {
			return false;
		}
		Location location = (Location) object;
		return this.row == location.getRow() && this.column == location.getColumn();
	}
	
	@Override
	public String toString() {
		return "(" + this.column + ", " + this.row + ")";
	}
	
	public int getRow() {
		return row;
	}

	public void setRow(int row) {
		this.row = row;
	}

	public int getColumn() {
		return column;
	}

	public void setColumn(int column) {
		this.column = column;
	}
}