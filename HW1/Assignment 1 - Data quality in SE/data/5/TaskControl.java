package net.bitacademy.java41.controls.task;

import java.io.File;
import java.util.List;

import javax.servlet.ServletContext;

import net.bitacademy.java41.services.ProjectService;
import net.bitacademy.java41.services.TaskService;
import net.bitacademy.java41.vo.Project;
import net.bitacademy.java41.vo.Task;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.multipart.MultipartFile;

@Controller
@RequestMapping("/task")
public class TaskControl {
	@Autowired TaskService taskService;
	@Autowired ProjectService projectService;
	@Autowired ServletContext sc;
	long currTime = 0;
	int count = 0;

	
	@RequestMapping(value="/addForm", method=RequestMethod.GET)
	public String addForm(int projectNo, Model model) throws Exception {
		
		Project project = projectService.getProject(projectNo);
		model.addAttribute("project", project);
		
		return "task/taskAddForm";
	}
	
	@RequestMapping(value="/add", method=RequestMethod.POST)
	public String add(MultipartFile uiProto,
			Task task) throws Exception {
		
		String filename = null;
		if(uiProto.getSize()>0){
		filename = this.getNewFileName();
		String path = sc.getAttribute("rootRealPath") + "file/" + filename;
		uiProto.transferTo(new File(path));
		}
		task.setUiProtoUrl( filename );
		taskService.taskAdd(task);
		return "redirect:../task/list.do?projectNo=" + task.getProjectNo();
	}
	
	
	@RequestMapping(value="/updateForm", method=RequestMethod.GET)
	public String updateForm(
					int projectNo, int taskNo,
					Model model) throws Exception {
		
		
		Project project = projectService.getProject(projectNo);
		Task task = taskService.getTask(projectNo, taskNo);

		model.addAttribute("project", project);
		model.addAttribute("task", task);
		
		return "task/taskUpdateForm";
	}
	
	@RequestMapping(value="/update", method=RequestMethod.POST)
	public String update(@RequestParam("uiProto")MultipartFile uiProtoUrl
							,String oldUiProtoUrl
							,Model model
							,Task task
							,int projectNo
							,int taskNo) throws Exception {

		String filename = null;
		if(uiProtoUrl.getSize()>0){
		filename = this.getNewFileName();
		String path = sc.getAttribute("rootRealPath") + "file/" + filename;
		uiProtoUrl.transferTo(new File(path));
		task.setUiProtoUrl(filename);
		}else{
			task.setUiProtoUrl(oldUiProtoUrl);
		}
		
		
		String returnUrl = sc.getAttribute("rootPath") + "/main.do";
		String resutlStatus = "";
		
		if (taskService.taskUpdate(task) > 0) {
			returnUrl = sc.getAttribute("rootPath") + "/task/view.do?projectNo=" + projectNo + "&taskNo=" + taskNo;
			resutlStatus = "UPDATE_SUCCESS";
		} else {
			returnUrl = sc.getAttribute("rootPath") + "/task/update.do?projectNo=" + projectNo + "&taskNo=" + taskNo;
			resutlStatus = "UPDATE_FAIL";
		}
		
		model.addAttribute("returnUrl", returnUrl);
		model.addAttribute("resultStatus", resutlStatus);
		return "task/taskResult";
	}

	synchronized private String getNewFileName() {
		long millis = System.currentTimeMillis();
		if (currTime != millis) {
			currTime = millis;
			count = 0;
		}
		return "task" + millis + "_" + (++count);
	}
	
	@RequestMapping("/list")
	public String list(int projectNo, Model model) throws Exception {
	
		Project project = projectService.getProject(projectNo);
		List<Task> taskList = taskService.getTaskList(projectNo);
		
		model.addAttribute("project", project);
		model.addAttribute("taskList", taskList);
		
		return "task/taskList";
	}
	
	@RequestMapping("/delete")
	public String delete(int projectNo, int taskNo
								,Model model) throws Exception {
		
		String returnUrl = sc.getAttribute("rootPath") + "/main.do";
		String resutlStatus = "";
		
		if (taskService.taskDelete(projectNo, taskNo) > 0) {
			returnUrl = sc.getAttribute("rootPath") + "/task/list.do?projectNo=" + projectNo;
			resutlStatus = "DELETE_SUCCESS";
		} else {
			returnUrl = sc.getAttribute("rootPath") + "/task/view.do?projectNo=" + projectNo + "&taskNo=" + taskNo;
			resutlStatus = "DELETE_FAIL";
		}
		
		model.addAttribute("returnUrl", returnUrl);
		model.addAttribute("resultStatus", resutlStatus);
		return "task/taskResult";
	}
	
	@RequestMapping("/view")
	public String execute(int projectNo,int taskNo
							,Model model) throws Exception {
		
		model.addAttribute("project", projectService.getProject(projectNo));
		model.addAttribute("task", taskService.getTask(projectNo, taskNo));
		
		return "task/taskView";
	}
}
	