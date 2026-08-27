package quiz;
import java.util.*;
public class MultipleChoice implements Question{
	
	// Multiple choice question, choices should be fairly important 
	// TODO: Think about how choices should be stored: 
	// TODO: Decide if choices should be included in Question, Answer, or not at all 
	private List<Answer> answerChoices;
	private String question; 
	private Answer correctAnswer; 
	private int questionId; 
	private String questionType; 
	
	public MultipleChoice(String question, Answer correctAnswer, List<Answer> answerChoices, int questionId) {
		this.questionType = "multiplechoice"; 
		this.question = question; 
		this.correctAnswer = correctAnswer; 
		this.answerChoices = answerChoices; 
		this.questionId = questionId; 
	}
	
	public Answer getAnswer() {
		return correctAnswer; 
	}
	
	//TODO: Decide if responses should be case-sensitive
	public boolean checkAnswer(Answer userResponse) {
		// Check if userResponse is in choices  
		String urStr = userResponse.toString(); 
		if(correctAnswer.toString().equals(urStr)) {
			return true; 
		}
		return false; 
	}
	
	//Temporary implementation
	public boolean checkAnswer(String userResponse) {
		String lowercaseResponse = userResponse.toLowerCase();
		String lowercaseAnswer = correctAnswer.toString().toLowerCase();
		if (lowercaseAnswer.equals(lowercaseResponse)) {
			return true; 
		}
		return false; 
	}
	
	//Override of toString
	public String toString() {
		return question; 
	}
	
	public int getId() {
		return questionId; 
	}
	
	public List<Answer> getAnswerChoices() {
		return answerChoices; 
	}
	
	public String getQuestionType() {
		return questionType; 
	}
	
}
