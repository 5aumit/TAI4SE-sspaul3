package com.dongkwon.finance.service;

import static org.assertj.core.api.Assertions.assertThat;

import java.io.File;
import java.io.FileInputStream;
import java.util.List;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.util.Pair;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.util.ResourceUtils;

import com.dongkwon.finance.FinanceApplication;
import com.dongkwon.finance.domain.SupportSummary;
import com.dongkwon.finance.exception.DataNotFoundException;
import com.dongkwon.finance.model.AmountByYear;
import com.dongkwon.finance.model.Prediction;
import com.fasterxml.jackson.databind.MappingIterator;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = FinanceApplication.class)
@Transactional
public class InstituteSupportServiceTest {
    @Autowired
    private InstituteSupportService instituteSupportService;
    @Autowired
    private InstituteSupportBatchService instituteSupportBatchService;
    @Autowired
    private CsvService csvService;

    @Before
    public void init() throws Exception {
        File csvFile = ResourceUtils.getFile(getClass().getResource("/simpledata.csv"));
        MappingIterator<String[]> csvIterator = csvService.readCsvWithHeader(new FileInputStream(csvFile));
        instituteSupportBatchService.setInstituteSupports(csvIterator);
        instituteSupportBatchService.calculateInstituteSupportSummaries();
    }

    @Test
    public void getAllInstituteNamesTest() {
        // when
        List<String> names = instituteSupportService.getAllInstituteNames();

        // then
        assertThat(names.size()).isEqualTo(2);
        assertThat(names.get(0)).isEqualTo("A-은행");
        assertThat(names.get(1)).isEqualTo("B 기금");
    }

    @Test
    public void getAmountsByYearTest() {
        // when
        List<AmountByYear> result = instituteSupportService.getAmountsByYear();

        // then
        assertThat(result.size()).isEqualTo(2);
        assertThat(result.get(0).getYear()).isEqualTo("2005년");
        assertThat(result.get(0).getTotalAmount()).isEqualTo("928");
        assertThat(result.get(0).getDetailAmount().get("A-은행")).isEqualTo("846");
        assertThat(result.get(0).getDetailAmount().get("B 기금")).isEqualTo("82");
        assertThat(result.get(1).getYear()).isEqualTo("2017년");
        assertThat(result.get(1).getTotalAmount()).isEqualTo("11933");
        assertThat(result.get(1).getDetailAmount().get("A-은행")).isEqualTo("5278");
        assertThat(result.get(1).getDetailAmount().get("B 기금")).isEqualTo("6655");
    }

    @Test
    public void getTopInstituteTest() {
        // when
        SupportSummary supportSummary = instituteSupportService.getTopInstitute();

        // then
        assertThat(supportSummary.getYear()).isEqualTo(2017);
        assertThat(supportSummary.getSumAmount()).isEqualTo(6655.0);
        assertThat(supportSummary.getAverageAmount()).isEqualTo(3327.5);
    }

    @Test
    public void getMinMaxAmountTest() {
        // when
        Pair<SupportSummary, SupportSummary> result1 = instituteSupportService.getMinMaxAmount("A-은행");
        Pair<SupportSummary, SupportSummary> result2 = instituteSupportService.getMinMaxAmount("B 기금");

        // then
        assertThat(result1.getFirst().getYear()).isEqualTo(2005);
        assertThat(result1.getFirst().getSumAmount()).isEqualTo(846.0);
        assertThat(result1.getFirst().getAverageAmount()).isEqualTo(846.0);
        assertThat(result1.getSecond().getYear()).isEqualTo(2017);
        assertThat(result1.getSecond().getSumAmount()).isEqualTo(5278.0);
        assertThat(result1.getSecond().getAverageAmount()).isEqualTo(2639.0);

        assertThat(result2.getFirst().getYear()).isEqualTo(2005);
        assertThat(result2.getFirst().getSumAmount()).isEqualTo(82.0);
        assertThat(result2.getFirst().getAverageAmount()).isEqualTo(82.0);
        assertThat(result2.getSecond().getYear()).isEqualTo(2017);
        assertThat(result2.getSecond().getSumAmount()).isEqualTo(6655.0);
        assertThat(result2.getSecond().getAverageAmount()).isEqualTo(3327.5);
    }

    @Test(expected = DataNotFoundException.class)
    public void getMinMaxAmountFailureTest() {
        // when
        instituteSupportService.getMinMaxAmount("존재하지않는은행");

        // then
        // Expect DataNotFoundException to be thrown
    }

    @Test
    public void predict2018Test() {
        // when
        Prediction prediction = instituteSupportService.predict2018("A-은행", 6);

        // then
        assertThat(prediction.getYear()).isEqualTo(2018);
        assertThat(prediction.getMonth()).isEqualTo(6);
        assertThat(prediction.getBank()).isNotBlank();
        assertThat(prediction.getAmount()).isNotNull();
    }
}
