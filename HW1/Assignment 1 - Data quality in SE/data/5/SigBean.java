package br.com.mauricio.news.mb.contabil;

import java.io.IOException;
import java.io.Serializable;

import javax.faces.application.FacesMessage;
import javax.faces.bean.ManagedBean;
import javax.faces.context.FacesContext;
import javax.faces.view.ViewScoped;

import br.com.mauricio.news.ln.contabil.SigLN;

@ManagedBean(name="sigMB")
@ViewScoped
public class SigBean implements Serializable {

	private static final long serialVersionUID = 1L;

	private String mes="";
	private String ano="";
	private String msg;
	private Boolean gerado=false;
	
    public void gerar() { 
    	gerado=false;
    	SigLN ln = new SigLN();
        FacesContext context = FacesContext.getCurrentInstance(); 
    	msg = ln.gerarArquivosSig(Integer.parseInt(ano), Integer.parseInt(mes));
    	if(msg!=""){
            context.addMessage(null, new FacesMessage("",msg)); 
    	}else{
    		try {
				ln.retornarArquivo();
				gerado=true;
			} catch (IOException e) {
				msg="Erro ao gerar arquivo.";
				gerado=false;
				context.addMessage(null, new FacesMessage("",msg)); 
				e.printStackTrace();
			}
    	}
    }
 


	public String getMes() {
		return mes;
	}

	public void setMes(String mes) {
		this.mes = mes;
	}

	public String getAno() {
		return ano;
	}

	public void setAno(String ano) {
		this.ano = ano;
	}

	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}



	public Boolean getGerado() {
		return gerado;
	}



	public void setGerado(Boolean gerado) {
		this.gerado = gerado;
	}



	public static long getSerialversionuid() {
		return serialVersionUID;
	}


}
