/*******************************************************************************
 * Copyright (c) 2019, 2019 Norvantek Technologies Corporation.
 ******************************************************************************/
package com.norvantek.phm.synapsis.data;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import java.io.File;
import java.io.IOException;
import java.util.List;

import org.apache.commons.io.FileUtils;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.context.junit4.SpringRunner;

import com.norvantek.phm.synapsis.data.param.FileTreeNode;
import com.norvantek.phm.synapsis.data.param.NodeLevel;
import com.norvantek.phm.synapsis.data.service.DataFileService;
import com.norvantek.phm.synapsis.exception.SynapsisException;

/**
 * @Version 1.0
 * @Author hanne.brekke@norvantek.com
 * @Created Dec 18, 2019 2:58:50 PM
 * @Description
 *              <p>
 * @Modification
 *               <p>
 *               Date Author Version Description
 *               <p>
 *               Dec 18, 2019 hanne.brekke@norvantek.com 1.0 create file
 */
@SpringBootTest(classes = TestApplication.class)
@RunWith(SpringRunner.class)
@ActiveProfiles("list")
public class DataFileListTest {

	private static String root = "D:/test/data";

	@Autowired
	private DataFileService service;

	/**
	 * 
	 */
	@BeforeClass
	public static void init() {
		FileUtils.deleteQuietly(new File(root));
		File rootFile = new File(root);
		if (!rootFile.exists()) {
			rootFile.mkdirs();
		}
		File folder1 = new File(rootFile, "201911");
		if (!folder1.exists()) {
			folder1.mkdirs();
		}
		File folder2 = new File(rootFile, "201912");
		if (!folder2.exists()) {
			folder2.mkdirs();
		}
		File folder21 = new File(folder2, "18");
		if (!folder21.exists()) {
			folder21.mkdirs();
		}
		File folder22 = new File(folder21, "150000");
		if (!folder22.exists()) {
			folder22.mkdirs();
		}
		File file = new File(folder22, "20191218150000.rt");
		if (!file.exists()) {
			try {
				file.createNewFile();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

	@Test
	public void test() throws SynapsisException {
		List<FileTreeNode> list = service.listRoot();
		assertNotNull(list);
		File rootDir = new File(root);
		File[] files = rootDir.listFiles();
		assertEquals(files.length, list.size());

		assertEquals(NodeLevel.Month, list.get(0).getLevel());

		list.forEach(System.out::println);
	}

	@Test
	public void testList() throws SynapsisException {
		String folerPath = root + File.separator + "201912";
		List<FileTreeNode> folders = service.listNodes(folerPath, NodeLevel.Month);
		assertNotNull(folders);
		File folder = new File(folerPath);
		File[] files = folder.listFiles();
		assertEquals(files.length, folders.size());
		folders.forEach(System.out::println);
	}

	@Test
	public void testListLeaf() throws SynapsisException {
		String folderPath = root + File.separator + "201912" + File.separator + "18";
		List<FileTreeNode> nodes = service.listNodes(folderPath, NodeLevel.Date);
		assertEquals(NodeLevel.Leaf, nodes.get(0).getLevel());
		nodes.forEach(System.out::println);
	}

	@Test(expected = SynapsisException.class)
	public void testNoFile() throws SynapsisException {
		String folderPath = root + File.separator + "201910";
		service.listNodes(folderPath, NodeLevel.Month);
	}

	@AfterClass
	public static void tearDown() {
		// FileUtils.deleteQuietly(new File(root));
	}
}
