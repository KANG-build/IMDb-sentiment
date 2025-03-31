package semicolon.aiTodoList.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.view.RedirectView;
import semicolon.aiTodoList.service.AIService;

import java.util.Map;

// REST API

@RestController
public class SentimentApiController {
    @GetMapping("/analyze")
    public RedirectView redirectToStaticHtml() {
        return new RedirectView("/analyze.html");
    }

    // POST to analyze
    @PostMapping("/analyze")
    public ResponseEntity<Map<String, String>> analyze(@RequestBody Map<String, String> payload) {
        String text = payload.get("text");
        Map<String, String> result = aiService.analyzeSentiment(text);
        return ResponseEntity.ok(result);
    }

    @Autowired
    private AIService aiService;
}
