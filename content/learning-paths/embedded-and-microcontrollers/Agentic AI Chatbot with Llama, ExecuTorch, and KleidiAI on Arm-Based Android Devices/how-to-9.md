---
title: Advanced Agentic Capabilities
weight: 9
layout: learningpathall
---

## Beyond Basic Tool Calling

Now that you have a working agentic chatbot, let's explore advanced capabilities that make your AI truly autonomous and intelligent.

## 1. Multi-Tool Orchestration

Enable your agent to use multiple tools in sequence to solve complex problems.

### Example: Smart Battery Advisor

```kotlin
// AdvancedToolRegistry.kt
class AdvancedToolRegistry(private val context: Context) {
    
    fun execute(command: String): ToolResult {
        val toolName = command.substringAfter("ACTION: ").substringBefore("(")
        val args = extractArguments(command)
        
        return when (toolName) {
            "check_battery_health" -> checkBatteryHealth()
            "get_running_apps" -> getRunningApps()
            "get_screen_brightness" -> getScreenBrightness()
            "suggest_battery_optimization" -> suggestBatteryOptimization()
            "check_order_status" -> checkOrderStatus(args["order_id"] ?: "")
            "search_knowledge_base" -> searchKnowledgeBase(args["query"] ?: "")
            else -> ToolResult.Error("Unknown tool: $toolName")
        }
    }
    
    private fun checkBatteryHealth(): ToolResult {
        val bm = context.getSystemService(Context.BATTERY_SERVICE) as BatteryManager
        val level = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
        val health = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_STATUS)
        val temp = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_TEMPERATURE) / 10.0
        
        return ToolResult.Success("""
            Battery Level: $level%
            Health: ${getHealthStatus(health)}
            Temperature: ${temp}°C
        """.trimIndent())
    }
    
    private fun getRunningApps(): ToolResult {
        val activityManager = context.getSystemService(Context.ACTIVITY_SERVICE) as ActivityManager
        val runningApps = activityManager.runningAppProcesses
        
        val topApps = runningApps.take(5).joinToString(", ") { 
            it.processName.substringAfterLast(".")
        }
        
        return ToolResult.Success("Top running apps: $topApps")
    }
    
    private fun getScreenBrightness(): ToolResult {
        val brightness = Settings.System.getInt(
            context.contentResolver,
            Settings.System.SCREEN_BRIGHTNESS,
            0
        )
        val percentage = (brightness / 255.0 * 100).toInt()
        
        return ToolResult.Success("Screen brightness: $percentage%")
    }
}

sealed class ToolResult {
    data class Success(val data: String) : ToolResult()
    data class Error(val message: String) : ToolResult()
}
```

### Enhanced System Prompt for Multi-Tool Usage

```kotlin
val advancedSystemPrompt = """
<|start_header_id|>system<|end_header_id|>
You are an intelligent Android Assistant with advanced reasoning capabilities.

Available Tools:
1. check_battery_health() - Returns battery level, health status, and temperature
2. get_running_apps() - Lists currently running applications
3. get_screen_brightness() - Returns current screen brightness level
4. check_order_status(order_id) - Checks the status of an order
5. search_knowledge_base(query) - Searches the knowledge base for information

You can use MULTIPLE tools to solve a problem. Output each tool call on a new line:
ACTION: tool_name(arguments)

Example Multi-Tool Usage:
User: "Why is my battery draining so fast?"
Assistant: 
ACTION: check_battery_health()
ACTION: get_running_apps()
ACTION: get_screen_brightness()

After receiving tool results, provide a comprehensive answer based on ALL the data.

If no tools are needed, respond conversationally.
<|eot_id|>
""".trimIndent()
```

### Multi-Tool Orchestrator

```kotlin
// MultiToolOrchestrator.kt
class MultiToolOrchestrator(
    private val modelRunner: ModelRunner,
    private val toolRegistry: AdvancedToolRegistry
) {
    private var conversationHistory = advancedSystemPrompt
    
    suspend fun chat(userMessage: String): String {
        conversationHistory += "<|start_header_id|>user<|end_header_id|>\n$userMessage<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"
        
        // First Pass: Get agent's plan
        var response = modelRunner.generate(conversationHistory)
        
        // Extract all ACTION commands
        val actions = extractActions(response)
        
        if (actions.isNotEmpty()) {
            val toolResults = mutableListOf<String>()
            
            // Execute all tools
            actions.forEach { action ->
                Log.d("Orchestrator", "Executing: $action")
                val result = toolRegistry.execute(action)
                
                when (result) {
                    is ToolResult.Success -> toolResults.add(result.data)
                    is ToolResult.Error -> toolResults.add("Error: ${result.message}")
                }
            }
            
            // Feed all results back to the model
            val toolOutput = toolResults.joinToString("\n---\n")
            conversationHistory += "$response\n<|start_header_id|>tool<|end_header_id|>\n$toolOutput<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n"
            
            // Second Pass: Synthesize final answer
            response = modelRunner.generate(conversationHistory)
        }
        
        conversationHistory += response
        return response
    }
    
    private fun extractActions(text: String): List<String> {
        val actionRegex = Regex("ACTION:\\s*([a-z_]+\\([^)]*\\))")
        return actionRegex.findAll(text).map { it.groupValues[1] }.toList()
    }
}
```

## 2. Context-Aware Conversations

Maintain conversation context to provide personalized responses.

```kotlin
// ConversationContext.kt
data class ConversationContext(
    val userId: String,
    val previousQueries: MutableList<String> = mutableListOf(),
    val userPreferences: MutableMap<String, String> = mutableMapOf(),
    val sessionStartTime: Long = System.currentTimeMillis()
) {
    fun addQuery(query: String) {
        previousQueries.add(query)
        if (previousQueries.size > 10) {
            previousQueries.removeAt(0) // Keep last 10 queries
        }
    }
    
    fun getRecentContext(): String {
        return if (previousQueries.isEmpty()) {
            "New conversation"
        } else {
            "Recent topics: ${previousQueries.takeLast(3).joinToString(", ")}"
        }
    }
}

// Enhanced Orchestrator with Context
class ContextAwareOrchestrator(
    private val modelRunner: ModelRunner,
    private val toolRegistry: AdvancedToolRegistry,
    private val context: ConversationContext
) {
    suspend fun chat(userMessage: String): String {
        context.addQuery(userMessage)
        
        // Inject context into the prompt
        val contextualPrompt = """
            User Context: ${context.getRecentContext()}
            Session Duration: ${getSessionDuration()} minutes
            
            User: $userMessage
        """.trimIndent()
        
        // ... rest of the orchestration logic
    }
    
    private fun getSessionDuration(): Long {
        return (System.currentTimeMillis() - context.sessionStartTime) / 60000
    }
}
```

## 3. Proactive Suggestions

Make your agent proactive by suggesting actions based on device state.

```kotlin
// ProactiveAgent.kt
class ProactiveAgent(
    private val context: Context,
    private val orchestrator: MultiToolOrchestrator
) {
    
    fun checkForProactiveSuggestions(): String? {
        val bm = context.getSystemService(Context.BATTERY_SERVICE) as BatteryManager
        val batteryLevel = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)
        val isCharging = bm.isCharging
        
        return when {
            batteryLevel < 20 && !isCharging -> {
                "💡 I noticed your battery is low (${batteryLevel}%). Would you like me to suggest battery-saving tips?"
            }
            batteryLevel == 100 && isCharging -> {
                "💡 Your battery is fully charged. You can unplug your device to preserve battery health."
            }
            isDeviceOverheating() -> {
                "⚠️ Your device temperature is high. Would you like me to check what's causing this?"
            }
            else -> null
        }
    }
    
    private fun isDeviceOverheating(): Boolean {
        val bm = context.getSystemService(Context.BATTERY_SERVICE) as BatteryManager
        val temp = bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_TEMPERATURE) / 10.0
        return temp > 40.0 // Over 40°C
    }
}

// In MainActivity
lifecycleScope.launch {
    while (isActive) {
        delay(60000) // Check every minute
        
        val suggestion = proactiveAgent.checkForProactiveSuggestions()
        if (suggestion != null) {
            showProactiveSuggestion(suggestion)
        }
    }
}
```

## 4. Learning from User Feedback

Implement a simple feedback mechanism to improve responses over time.

```kotlin
// FeedbackManager.kt
data class Feedback(
    val query: String,
    val response: String,
    val rating: Int, // 1-5 stars
    val timestamp: Long
)

class FeedbackManager(private val context: Context) {
    private val feedbackStore = mutableListOf<Feedback>()
    
    fun recordFeedback(query: String, response: String, rating: Int) {
        val feedback = Feedback(query, response, rating, System.currentTimeMillis())
        feedbackStore.add(feedback)
        
        // Save to persistent storage
        saveFeedback(feedback)
        
        // Analyze patterns
        if (rating <= 2) {
            Log.w("Feedback", "Poor response for query: $query")
            // Could trigger retraining or prompt adjustment
        }
    }
    
    fun getAverageRating(): Double {
        return if (feedbackStore.isEmpty()) 0.0
        else feedbackStore.map { it.rating }.average()
    }
    
    fun getPoorlyRatedQueries(): List<String> {
        return feedbackStore
            .filter { it.rating <= 2 }
            .map { it.query }
            .distinct()
    }
}

// UI Integration
fun showResponseWithFeedback(response: String) {
    chatAdapter.addMessage(response)
    
    // Show rating buttons
    showRatingDialog { rating ->
        feedbackManager.recordFeedback(
            query = lastUserQuery,
            response = response,
            rating = rating
        )
    }
}
```

## 5. Fallback Strategies

Implement intelligent fallbacks when the model is uncertain.

```kotlin
// IntelligentFallback.kt
class IntelligentFallback(private val context: Context) {
    
    fun shouldUseFallback(response: String): Boolean {
        return response.contains("I don't know", ignoreCase = true) ||
               response.contains("I'm not sure", ignoreCase = true) ||
               response.length < 10
    }
    
    fun getFallbackResponse(query: String): String {
        return when {
            query.contains("battery", ignoreCase = true) -> {
                "I can check your battery status. Would you like me to do that?"
            }
            query.contains("order", ignoreCase = true) -> {
                "I can help you track your order. Please provide your order number."
            }
            query.contains("help", ignoreCase = true) -> {
                """
                I can assist you with:
                • Battery and device health
                • Order tracking
                • General questions
                
                What would you like help with?
                """.trimIndent()
            }
            else -> {
                "I'm not sure I understood that correctly. Could you rephrase your question?"
            }
        }
    }
}

// In Orchestrator
suspend fun chatWithFallback(userMessage: String): String {
    val response = chat(userMessage)
    
    return if (intelligentFallback.shouldUseFallback(response)) {
        intelligentFallback.getFallbackResponse(userMessage)
    } else {
        response
    }
}
```

## 6. Confidence Scoring

Add confidence scores to agent responses.

```kotlin
// ConfidenceEstimator.kt
class ConfidenceEstimator {
    
    fun estimateConfidence(
        response: String,
        toolsUsed: List<String>,
        responseTime: Long
    ): ConfidenceScore {
        var score = 0.5 // Base confidence
        
        // Higher confidence if tools were used
        if (toolsUsed.isNotEmpty()) {
            score += 0.3
        }
        
        // Lower confidence for vague responses
        if (response.contains("maybe", ignoreCase = true) ||
            response.contains("possibly", ignoreCase = true)) {
            score -= 0.2
        }
        
        // Lower confidence for very fast responses (might be cached/generic)
        if (responseTime < 500) {
            score -= 0.1
        }
        
        // Clamp between 0 and 1
        score = score.coerceIn(0.0, 1.0)
        
        return when {
            score >= 0.8 -> ConfidenceScore.HIGH
            score >= 0.5 -> ConfidenceScore.MEDIUM
            else -> ConfidenceScore.LOW
        }
    }
}

enum class ConfidenceScore {
    HIGH, MEDIUM, LOW
}

// Display confidence in UI
fun displayResponseWithConfidence(response: String, confidence: ConfidenceScore) {
    val confidenceIcon = when (confidence) {
        ConfidenceScore.HIGH -> "✅"
        ConfidenceScore.MEDIUM -> "⚠️"
        ConfidenceScore.LOW -> "❓"
    }
    
    chatAdapter.addMessage("$confidenceIcon $response")
}
```

## 7. Task Planning and Execution

Enable your agent to break down complex tasks into steps.

```kotlin
// TaskPlanner.kt
data class Task(
    val description: String,
    val steps: List<String>,
    val estimatedTime: Int // seconds
)

class TaskPlanner(private val modelRunner: ModelRunner) {
    
    suspend fun planTask(userGoal: String): Task {
        val planningPrompt = """
            User wants to: $userGoal
            
            Break this down into specific steps.
            Output format:
            STEP 1: [action]
            STEP 2: [action]
            ...
        """.trimIndent()
        
        val plan = modelRunner.generate(planningPrompt)
        val steps = extractSteps(plan)
        
        return Task(
            description = userGoal,
            steps = steps,
            estimatedTime = steps.size * 30 // 30 seconds per step
        )
    }
    
    private fun extractSteps(plan: String): List<String> {
        val stepRegex = Regex("STEP \\d+: (.+)")
        return stepRegex.findAll(plan).map { it.groupValues[1] }.toList()
    }
}

// Usage
val task = taskPlanner.planTask("Optimize my phone's battery life")
// Returns:
// Task(
//   description = "Optimize my phone's battery life",
//   steps = [
//     "Check current battery health",
//     "Identify battery-draining apps",
//     "Adjust screen brightness",
//     "Enable battery saver mode"
//   ],
//   estimatedTime = 120
// )
```

## Summary

With these advanced capabilities, your Agentic AI chatbot can:

- **Multi-Tool Orchestration**: Use multiple tools to solve complex problems
- **Context Awareness**: Remember conversation history and user preferences
- **Proactive Suggestions**: Offer help before being asked
- **Learning**: Improve from user feedback
- **Intelligent Fallbacks**: Handle uncertainty gracefully
- **Confidence Scoring**: Communicate certainty levels
- **Task Planning**: Break down complex goals into actionable steps

These features transform your chatbot from a reactive Q&A system into a truly autonomous AI assistant! 
