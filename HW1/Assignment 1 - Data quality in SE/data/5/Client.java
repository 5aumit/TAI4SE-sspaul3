package com.lrh.composite;

import java.util.List;

/**
 *
 * 模拟 人员组织机构
 *
 */
public class Client {


	public static void main(String[] args) {
		Componsite root = new Componsite("总公司",null);
		Componsite c1 = new Componsite("研发部", root);
		Componsite c2 = new Componsite("人事部",root);
		Componsite c1_1 = new Componsite("零售研发组",c1);
		Componsite c1_2 = new Componsite("批发研发组",c1);

		Leaf p1 = new Leaf("张一", root);
		Leaf p2 = new Leaf("张三", c1);
		Leaf p3 = new Leaf("张四", c1_1);
		Leaf p4 = new Leaf("张五", c1_2);
		Leaf p5 = new Leaf("王一", c2);

		root.add(c1).add(c2).add(p1);
		c1.add(c1_1).add(c1_2).add(p2);
		c2.add(p5);
		c1_1.add(p3);
		c1_2.add(p4);

		root.doSomeThing();
		printChild(root.getChild());
	}


	/**
	 *
	 * 打印信息
	 *
	 */
	private static void printChild(List<Component> components){

		for (Component component : components) {
			component.doSomeThing();

			if (component instanceof Componsite) {
				Componsite c = (Componsite) component;
				List<Component> componentList = c.getChild();
				if (componentList != null && componentList.size() > 0) {
					printChild(componentList);
				}
			}

		}
	}



}
