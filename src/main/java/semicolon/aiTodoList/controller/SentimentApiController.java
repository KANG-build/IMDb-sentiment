package semicolon.aiTodoList.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import semicolon.aiTodoList.service.AIService;

import java.util.Map;

// REST API
@RestController
public class SentimentApiController {
    // POST to analyze
    @PostMapping("/analyze")
    public ResponseEntity<Map<String, String>> analyze(@RequestBody Map<String, String> payload) {
        String text = payload.get("text");
        String result = aiService.analyzeSentiment(text);
        return ResponseEntity.ok(Map.of("result", result));
    }

    @Autowired
    private AIService aiService;
}
