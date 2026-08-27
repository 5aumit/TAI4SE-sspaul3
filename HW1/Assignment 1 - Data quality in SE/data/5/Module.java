package cn.deal.core.permission.domain;

import java.io.Serializable;
import java.util.List;


public class Module implements Serializable {
    private static final long serialVersionUID = -6849794470754667710L;

    /**
     * 模块类型
     */
    public static enum Type {
        /**
         * 根
         */
    	Product("Product"),
    	Package("Package"),
    	Module("Module"),
    	ModuleRef("ModuleRef"),
    	Version("Version");
    	
    	private String value;

    	Type(String value){
            this.value = value;
        }

        public String getValue() {
            return value;
        }

        public void setValue(String value) {
            this.value = value;
        }
    }
    
    
    private String id;
    private String type;
    private String name;
    private String description;
    
    private List<Module> versions;
    private List<Resource> menus;
    private List<Module> children;
    private List<String> includes;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Module> getVersions() {
        return versions;
    }

    public void setVersions(List<Module> versions) {
        this.versions = versions;
    }

    public List<String> getIncludes() {
        return includes;
    }

    public void setIncludes(List<String> includes) {
        this.includes = includes;
    }

    public List<Module> getChildren() {
        return children;
    }

    public void setChildren(List<Module> children) {
        this.children = children;
    }

    public List<Resource> getMenus() {
        return menus;
    }

    public void setMenus(List<Resource> menus) {
        this.menus = menus;
    }

	@Override
	public String toString() {
		return "Module [id=" + id + ", type=" + type + ", name=" + name + ", description=" + description + ", versions="
				+ versions + ", menus=" + menus + ", children=" + children + ", includes=" + includes + "]";
	}
}
