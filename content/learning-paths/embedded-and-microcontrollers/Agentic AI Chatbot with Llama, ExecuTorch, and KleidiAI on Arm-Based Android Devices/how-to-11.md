---
title: Testing and Verification
weight: 11 
layout: learningpathall
---

## 1. Verify the Build
Before testing the Agent, ensure the app builds and runs on your Arm device.
1.  Connect your Android phone via USB.
2.  Run `adb devices` to confirm connection.
3.  In Android Studio, click **Run**.
4.  The App should launch without crashing.

## 2. Verify Agentic Behavior
We need to test if the Agent correctly "thinks" and "acts".

### Test Case 1: General Knowledge (No Tool)
**User Input**: "What is the capital of France?"
**Expected Behavior**:
- The Agent should *not* trigger any tool.
- **Log Output**: `ACTION:` should NOT appear in the logs.
- **UI Output**: "The capital of France is Paris."

### Test Case 2: Battery Check (Tool Call)
**User Input**: "My phone feels hot. How is the battery?"
**Expected Behavior**:
- The Agent should recognize the intent.
- **Log Output**: `AgentOrchestrator: Detected Action: check_battery_status()`
- **Log Output**: `ToolRegistry: Executing check_battery_status... Result: Battery Level is 85%.`
- **UI Output**: "The battery level is 85%. If it's heating up, try closing unused apps."

### Test Case 3: Order Status (Mock Tool)
**User Input**: "Where is my order #12345?"
**Expected Behavior**:
- **Log Output**: `AgentOrchestrator: Detected Action: check_order_status("12345")`
- **UI Output**: "Order #12345 is currently Out for Delivery."

### Test Case 4: Multi-Step Reasoning
**User Input**: "My phone is hot and draining battery fast. What should I do?"
**Expected Behavior**:
- The Agent should call `check_battery_status()` first
- **Log Output**: `AgentOrchestrator: Detected Action: check_battery_status()`
- **Log Output**: `ToolRegistry: Result: Battery Level is 45%.`
- **UI Output**: "Your battery is at 45%. The heating might be due to background apps. Try closing unused apps and enabling battery saver mode."

### Test Case 5: No Tool Needed (Conversational)
**User Input**: "Thank you for your help!"
**Expected Behavior**:
- No tool should be triggered
- **Log Output**: No ACTION detected
- **UI Output**: "You're welcome! Feel free to ask if you need anything else."

### Test Case 6: Invalid Tool Request
**User Input**: "Can you send an email to my boss?"
**Expected Behavior**:
- Agent should recognize it doesn't have this capability
- **UI Output**: "I don't have the ability to send emails, but I can help you with battery status, order tracking, and general questions."

### Test Case 7: Chained Actions (Advanced)
**User Input**: "Check my battery and tell me if I should charge now"
**Expected Behavior**:
- Call `check_battery_status()`
- Use the result to provide recommendation
- **UI Output**: "Your battery is at 25%. Yes, I recommend charging your device soon."

## 3. Debugging Tips
If the Agent is not calling tools:
- **Check the System Prompt**: Is it exactly as defined in `AgentOrchestrator`?
- **Check the Model**: Are you using the Instruct version of Llama 3? Base models do not follow instructions well.
- **Check Logs**: Look at the raw output from `modelRunner.generate()`. Is it outputting "I will check the battery..." instead of "ACTION: check_battery_status()"? If so, make the prompt stricter.
- **Verify KleidiAI**: Ensure KleidiAI is active for optimal performance: `adb logcat | grep -i kleidiai`

## 4. Performance Benchmarking
Monitor the latency of the "Think" step vs the "Act" step.
- **Think Latency**: Time for the first LLM pass (~500-1500ms with KleidiAI)
- **Act Latency**: Time for the Kotlin function (should be <10ms)
- **Response Latency**: Time for the second LLM pass (~500-1500ms)

Total Latency = Think + Act + Response.

### Expected Performance (with KleidiAI)
On modern Arm devices:
- **Pixel 8 Pro**: ~1.5-2s total latency
- **Budget Device (6GB RAM)**: ~4-6s total latency

### Benchmarking Code
```kotlin
// In MainActivity or Test Class
fun benchmarkAgenticLoop() {
    val testCases = listOf(
        "What is AI?",                          // No tool
        "Check my battery",                     // Single tool
        "My phone is hot, check battery"        // Reasoning + tool
    )
    
    testCases.forEach { query ->
        val startTime = System.currentTimeMillis()
        val response = runBlocking { agentOrchestrator.chat(query) }
        val endTime = System.currentTimeMillis()
        
        Log.d("Benchmark", "Query: $query")
        Log.d("Benchmark", "Latency: ${endTime - startTime}ms")
        Log.d("Benchmark", "Response: $response\n")
    }
}
```

## 5. Unit Testing the Agent

Create unit tests for your agentic components:

```kotlin
// AgentOrchestratorTest.kt
@Test
fun testToolCalling() {
    val mockModelRunner = MockModelRunner()
    val toolRegistry = ToolRegistry(context)
    val orchestrator = AgentOrchestrator(mockModelRunner, toolRegistry)
    
    // Simulate model output with ACTION
    mockModelRunner.setResponse("ACTION: check_battery_status()")
    
    val result = runBlocking { orchestrator.chat("How's my battery?") }
    
    assertTrue(result.contains("Battery Level"))
}

@Test
fun testNoToolNeeded() {
    val mockModelRunner = MockModelRunner()
    val orchestrator = AgentOrchestrator(mockModelRunner, ToolRegistry(context))
    
    mockModelRunner.setResponse("Hello! How can I help you today?")
    
    val result = runBlocking { orchestrator.chat("Hi") }
    
    assertFalse(result.contains("ACTION:"))
    assertTrue(result.contains("Hello"))
}
```

## Summary
Comprehensive testing ensures your Agentic AI chatbot:
- Correctly identifies when to use tools
- Executes tools reliably
- Provides helpful responses
- Performs efficiently with KleidiAI optimization
- Handles edge cases gracefully

