package app.cal.schedule.business.entity;

import java.util.LinkedList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

import app.cal.schedule.common.UUIDGenerator;

@Entity
@Table(name="CLIENT_GROUP")
public class ClientGroup extends AggregateRoot {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	@Id
	@Column(name="GROUP_ID")
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private long groupId;
	
	@Column(name="PRIM_PARENT_EMAIL_ID")
	private String priParentEmail;

	@Column(name="SEC_PARENT_EMAIL_ID")
	private String secParentEmail;
	
	@Column(name="PRIM_CONTACT_NO")
	private String priParentContactNo;
	
	@Column(name="SEC_CONTACT_NO")
	private String secParentContactNo;
	
	
	@OneToMany(cascade=CascadeType.ALL, fetch=FetchType.LAZY, orphanRemoval=true, mappedBy="clientGrp")
	private List<ClientInfo> clientInfo = new LinkedList<>();
	
	
	@Override
	public Long getId() {
		return groupId;
	}

	public long getGroupId() {
		return groupId;
	}

	public void setGroupId(long groupId) {
		this.groupId = groupId;
	}

	public String getPriParentEmail() {
		return priParentEmail;
	}

	public void setPriParentEmail(String priParentEmail) {
		this.priParentEmail = priParentEmail;
	}

	public String getSecParentEmail() {
		return secParentEmail;
	}

	public void setSecParentEmail(String secParentEmail) {
		this.secParentEmail = secParentEmail;
	}

	public String getPriParentContactNo() {
		return priParentContactNo;
	}

	public void setPriParentContactNo(String priParentContactNo) {
		this.priParentContactNo = priParentContactNo;
	}

	public String getSecParentContactNo() {
		return secParentContactNo;
	}

	public void setSecParentContactNo(String secParentContactNo) {
		this.secParentContactNo = secParentContactNo;
	}

	public List<ClientInfo> getClientInfo() {
		return clientInfo;
	}

	public void setClientInfo(List<ClientInfo> clientInfo) {
		this.clientInfo = clientInfo;
	}
	
	public ClientGroup() {}
	
	public ClientGroup( String priParentContactNo, 
			String priParentEmail,
			String secParentContactNo,
			String secParentEmail){
		this.setRefId(UUIDGenerator.newRefId());
		this.priParentContactNo = priParentContactNo;
		this.priParentEmail = priParentEmail;
		this.secParentContactNo = secParentContactNo;
		this.secParentEmail = secParentEmail;		
	}
}
