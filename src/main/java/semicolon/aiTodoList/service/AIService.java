package semicolon.aiTodoList.service;

import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Service
public class AIService {

    public Map<String, String> analyzeSentiment(String text) {
        RestTemplate restTemplate = new RestTemplate();
        String flaskUrl = "http://localhost:5000/classify";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        Map<String, String> request = new HashMap<>();
        request.put("text", text);  // <- key는 "text"로 보내야 Flask가 알아먹음

        HttpEntity<Map<String, String>> entity = new HttpEntity<>(request, headers);

        try {
            ResponseEntity<Map> response = restTemplate.postForEntity(flaskUrl, entity, Map.class);

            if (response.getStatusCode() == HttpStatus.OK && response.getBody() != null) {
                Map<String, Object> responseBody = response.getBody();

                String sentiment = (String) responseBody.get("sentiment");
                String emoji = (String) responseBody.get("emoji");

                // 프론트에서 직접 key로 꺼낼 수 있도록 반환!
                Map<String, String> result = new HashMap<>();
                result.put("sentiment", sentiment);
                result.put("emoji", emoji);
                return result;
            } else {
                return Map.of("sentiment", "error", "emoji", "❌");
            }

        } catch (Exception e) {
            e.printStackTrace();
            return Map.of("sentiment", "error", "emoji", "❌");
        }
    }
}
