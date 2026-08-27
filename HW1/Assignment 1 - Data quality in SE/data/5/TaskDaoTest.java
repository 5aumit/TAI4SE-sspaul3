import dao.TaskDao;
import model.Task;
import model.TaskManager;
import model.TaskManagerDefault;
import org.junit.Test;
import org.mockito.Mockito;

import java.sql.Connection;
import java.sql.Date;
import java.sql.SQLException;
import java.util.List;
import java.util.Random;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.mockito.Matchers.anyInt;
import static org.mockito.Mockito.*;

public class TaskDaoTest {

    @Test
    public void shouldBeAddedTask_whenAddNewTask() throws SQLException {
        TaskDao mock = Mockito.mock(TaskDao.class);
        int id = new Random().nextInt();
        Task task = new Task();

        when(mock.get(anyInt())).thenReturn(task);

        assertEquals(task, mock.get(id));
    }


    @Test
    public void taskManagerTest() throws SQLException {
        TaskDao mock = Mockito.mock(TaskDao.class);
        TaskManager taskManager = new TaskManagerDefault(mock);

        when(mock.get(anyInt())).thenReturn(new Task());
        taskManager.get(anyInt());

        verify(mock, atLeastOnce()).get(anyInt());
    }



}
