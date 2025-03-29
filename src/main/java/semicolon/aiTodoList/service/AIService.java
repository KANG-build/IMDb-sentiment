package semicolon.aiTodoList.service;

import org.springframework.stereotype.Service;

@Service
public class AIService {

    public String analyzeSentiment(String text) {
        // 목업
        if (text.toLowerCase().contains("happy") || text.toLowerCase().contains("good")) {
            return "긍정";
        } else {
            return "부정";
        }
    }
}