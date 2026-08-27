package com.ilovefundy.entity.funding;

import com.fasterxml.jackson.annotation.JsonIdentityInfo;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.ObjectIdGenerators;
import com.ilovefundy.entity.pay.PayInfo;
import com.ilovefundy.entity.user.User;
import lombok.*;
import org.hibernate.annotations.BatchSize;
import org.hibernate.annotations.ColumnDefault;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

@JsonIdentityInfo(generator= ObjectIdGenerators.PropertyGenerator.class, property="fundingId")
@Getter
@Setter
@Entity
@Table(name = "funding_project")
@AllArgsConstructor
@NoArgsConstructor
public class FundingProject {
    @Id
    @GeneratedValue
    @Column(name = "funding_id")
    private Integer fundingId;

    @BatchSize(size=10)
    @OneToMany(mappedBy = "funding")
    private List<FundingNotice> fundingNotices = new ArrayList<>();

    @BatchSize(size=10)
    @OneToMany(mappedBy = "funding")
    private List<FundingComment> fundingComments = new ArrayList<>();

    @BatchSize(size=10)
//    @JsonBackReference
    @JsonIgnore
    @ManyToMany(mappedBy = "fundings")
    private Set<User> users = new LinkedHashSet<>();

    @BatchSize(size=10)
//    @JsonBackReference
//    @JsonIgnore
    @OneToMany(mappedBy = "funding")
    private List<PayInfo> userPays = new ArrayList<>();

    @Column(name = "donation_place_id")
    private Integer donationPlaceId;

    @Column(name = "idol_id")
    private Integer idolId;
    @Column(name = "user_id")
    private Integer userId;
//    @ManyToOne
//    @JoinColumn(name = "user_id")
//    private User user;

    @Column(name = "funding_type")
    @ColumnDefault("1")
    private FundingType fundingType; // 펀딩 타입
    @Column(name = "funding_name")
    private String fundingName;
    @Column(name = "funding_subtitle")
    private String fundingSubtitle;
    @Column(name = "idol_name")
    private String idolName;
    @Column(name = "funding_goal_amount")
    private Integer fundingGoalAmount;
    @Column(name = "funding_start_time")
    private LocalDateTime fundingStartTime; // 펀딩 시작 시간
    @Column(name = "funding_end_time")
    private LocalDateTime fundingEndTime; // 펀딩 종료 시간
    @Column(name = "funding_content", columnDefinition = "LONGTEXT")
    private String fundingContent;
    @Column(name = "funding_thumbnail")
    private String fundingThumbnail;
    @Column(name = "donation_rate")
    @ColumnDefault("0")
    private Integer donationRate; // 기부 옵션 선택 여부
    @Column(name = "is_Confirm")
    @ColumnDefault("0")
    private FundingConfirm isConfirm; // 펀딩 승인 여부
    @Column(name = "is_good_funding")
    @Enumerated(EnumType.STRING)
    @ColumnDefault("'N'")
    private YesOrNo isGoodFunding; // 굿프로젝트 여부

    public enum FundingType{
        Donation, Basic;
    }
    public enum FundingConfirm {
        Wait, ApprovePre, ApproveIng, ApprovePost, Decline, Success, Fail;
    }
    public enum YesOrNo {
        Y, N;
    }
}
