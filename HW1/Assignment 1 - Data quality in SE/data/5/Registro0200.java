package br.com.orlandoburli.core.extras.sped.registros.bloco0;

import java.math.BigDecimal;

import br.com.orlandoburli.core.extras.sped.interfaces.CampoSped;
import br.com.orlandoburli.core.extras.sped.registros.RegistroSped;

public class Registro0200 extends RegistroSped implements Bloco0 {

	private String codigoItem;
	private String descricaoItem;
	private String codigoBarra;
	private String codigoAnteriorItem;
	private String unidade;
	private String tipoItem;
	private String codigoNcm;
	private String exTipi;
	private String codigoGenero;
	private String codigoLst;
	private BigDecimal aliquota;

	@Override
	@CampoSped(name = "REG", order = 1)
	public String getRegistro() {
		return "0200";
	}

	@CampoSped(name = "COD_ITEM", order = 2)
	public String getCodigoItem() {
		return codigoItem;
	}

	public void setCodigoItem(String codigoItem) {
		this.codigoItem = codigoItem;
	}

	@CampoSped(name = "DESCR_ITEM", order = 3)
	public String getDescricaoItem() {
		return descricaoItem;
	}

	public void setDescricaoItem(String descricaoItem) {
		this.descricaoItem = descricaoItem;
	}

	@CampoSped(name = "COD_BARRA", order = 4)
	public String getCodigoBarra() {
		return codigoBarra;
	}

	public void setCodigoBarra(String codigoBarra) {
		this.codigoBarra = codigoBarra;
	}

	@CampoSped(name = "COD_ANT_ITEM", order = 5)
	public String getCodigoAnteriorItem() {
		return codigoAnteriorItem;
	}

	public void setCodigoAnteriorItem(String codigoAnteriorItem) {
		this.codigoAnteriorItem = codigoAnteriorItem;
	}

	@CampoSped(name = "UNID_INV", order = 6)
	public String getUnidade() {
		return unidade;
	}

	public void setUnidade(String unidade) {
		this.unidade = unidade;
	}

	@CampoSped(name = "TIPO_ITEM", order = 7)
	public String getTipoItem() {
		return tipoItem;
	}

	public void setTipoItem(String tipoItem) {
		this.tipoItem = tipoItem;
	}

	@CampoSped(name = "COD_NCM", order = 8)
	public String getCodigoNcm() {
		return codigoNcm;
	}

	public void setCodigoNcm(String codigoNcm) {
		this.codigoNcm = codigoNcm;
	}

	@CampoSped(name = "EX_IPI", order = 9)
	public String getExTipi() {
		return exTipi;
	}

	public void setExTipi(String exTipi) {
		this.exTipi = exTipi;
	}

	@CampoSped(name = "COD_GEN", order = 10)
	public String getCodigoGenero() {
		return codigoGenero;
	}

	public void setCodigoGenero(String codigoGenero) {
		this.codigoGenero = codigoGenero;
	}

	@CampoSped(name = "COD_LST", order = 11)
	public String getCodigoLst() {
		return codigoLst;
	}

	public void setCodigoLst(String codigoLst) {
		this.codigoLst = codigoLst;
	}

	@CampoSped(name = "ALIQ_ICMS", order = 12)
	public BigDecimal getAliquota() {
		return aliquota;
	}

	public void setAliquota(BigDecimal aliquota) {
		this.aliquota = aliquota;
	}
}