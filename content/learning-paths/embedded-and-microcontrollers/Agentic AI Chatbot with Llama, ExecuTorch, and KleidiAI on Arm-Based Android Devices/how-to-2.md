---
title: System Architecture Overview
weight: 2
layout: learningpathall
---

## Complete System Architecture

Understanding the architecture of your Agentic AI Chatbot is crucial for successful implementation. This section provides a comprehensive overview of all components and their interactions.

## High-Level Architecture Diagram

```mermaid
graph TB
    subgraph "User Interface Layer"
        UI[Android UI<br/>MainActivity + Compose]
        Chat[Chat Interface]
        Feedback[Feedback System]
    end
    
    subgraph "Orchestration Layer"
        Orch[Agent Orchestrator]
        Context[Conversation Context]
        Planner[Task Planner]
        Fallback[Intelligent Fallback]
    end
    
    subgraph "AI Inference Layer"
        Model[Model Runner]
        ExecuTorch[ExecuTorch Runtime]
        KleidiAI[KleidiAI Kernels]
        XNNPACK[XNNPACK Backend]
    end
    
    subgraph "Tool Execution Layer"
        Registry[Tool Registry]
        Battery[Battery Manager]
        Apps[App Manager]
        Orders[Order System]
        KB[Knowledge Base]
    end
    
    subgraph "Storage Layer"
        ModelFile[Model File<br/>.pte]
        ChatHistory[Chat History<br/>Encrypted]
        UserPrefs[User Preferences]
    end
    
    UI --> Chat
    Chat --> Orch
    Orch --> Context
    Orch --> Model
    Orch --> Planner
    Model --> ExecuTorch
    ExecuTorch --> KleidiAI
    ExecuTorch --> XNNPACK
    Orch --> Registry
    Registry --> Battery
    Registry --> Apps
    Registry --> Orders
    Registry --> KB
    Orch --> Fallback
    Model -.->|loads| ModelFile
    Context -.->|reads/writes| ChatHistory
    Context -.->|reads/writes| UserPrefs
    Chat --> Feedback
    
    style KleidiAI fill:#ff6b6b
    style ExecuTorch fill:#4ecdc4
    style Orch fill:#95e1d3
    style Model fill:#f38181
```

## Agentic Loop Flow

```mermaid
sequenceDiagram
    participant User
    participant UI
    participant Orchestrator
    participant LLM as Model Runner
    participant Tools as Tool Registry
    participant Android as Android System
    
    User->>UI: "My battery is draining fast"
    UI->>Orchestrator: chat(message)
    
    Note over Orchestrator: OBSERVE Phase
    Orchestrator->>Orchestrator: Add to context
    
    Note over Orchestrator: THINK Phase
    Orchestrator->>LLM: Generate response
    LLM-->>Orchestrator: "ACTION: check_battery_health()"
    
    Note over Orchestrator: ACT Phase
    Orchestrator->>Tools: execute("check_battery_health")
    Tools->>Android: getBatteryInfo()
    Android-->>Tools: Battery: 45%, Temp: 38°C
    Tools-->>Orchestrator: ToolResult.Success(data)
    
    Note over Orchestrator: RESULT Phase
    Orchestrator->>LLM: Generate final response<br/>with tool results
    
    Note over Orchestrator: RESPONSE Phase
    LLM-->>Orchestrator: "Your battery is at 45%..."
    Orchestrator-->>UI: Final response
    UI-->>User: Display message
```

## Data Flow Architecture

```mermaid
flowchart LR
    subgraph Input
        UserQuery[User Query]
        SystemPrompt[System Prompt]
        Context[Conversation Context]
    end
    
    subgraph Processing
        Tokenizer[Tokenizer]
        Quantized[Quantized Model<br/>8da4w]
        KV[KV Cache]
    end
    
    subgraph Optimization
        XNNPACK[XNNPACK<br/>Extended Ops]
        KleidiAI[KleidiAI<br/>i8mm Kernels]
        ARM[ARM CPU<br/>Neoverse/Cortex]
    end
    
    subgraph Output
        Tokens[Output Tokens]
        Detokenizer[Detokenizer]
        Response[Response Text]
        ActionParser[Action Parser]
    end
    
    UserQuery --> Tokenizer
    SystemPrompt --> Tokenizer
    Context --> Tokenizer
    Tokenizer --> Quantized
    Quantized --> KV
    KV --> XNNPACK
    XNNPACK --> KleidiAI
    KleidiAI --> ARM
    ARM --> Tokens
    Tokens --> Detokenizer
    Detokenizer --> Response
    Response --> ActionParser
    
    style KleidiAI fill:#ff6b6b
    style ARM fill:#ffd93d
    style Quantized fill:#6bcf7f
```

## Component Responsibilities

### 1. **User Interface Layer**
- **MainActivity**: Entry point, lifecycle management
- **Chat Interface**: Message display, user input
- **Feedback System**: Collect user ratings and feedback

**Key Files:**
- `MainActivity.kt`
- `ChatAdapter.kt`
- `MessageItem.kt`

### 2. **Orchestration Layer**
- **Agent Orchestrator**: Core agentic loop (Observe → Think → Act → Result → Response)
- **Conversation Context**: Maintains chat history and user preferences
- **Task Planner**: Breaks down complex goals into steps
- **Intelligent Fallback**: Handles uncertain or failed responses

**Key Files:**
- `AgentOrchestrator.kt`
- `ConversationContext.kt`
- `TaskPlanner.kt`
- `IntelligentFallback.kt`

### 3. **AI Inference Layer**
- **Model Runner**: Wrapper around ExecuTorch for inference
- **ExecuTorch Runtime**: PyTorch mobile runtime
- **KleidiAI**: Arm-optimized kernels (2-3x speedup)
- **XNNPACK**: Neural network operator library

**Key Files:**
- `ModelRunner.kt`
- `llama3_1B_kv_sdpa_xnn_kleidiai_qe_4_64_1024.pte` (model file)
- `tokenizer.bin`

### 4. **Tool Execution Layer**
- **Tool Registry**: Maps ACTION commands to Kotlin functions
- **Battery Manager**: Device battery information
- **App Manager**: Running applications info
- **Order System**: Mock order tracking
- **Knowledge Base**: FAQ and product information

**Key Files:**
- `ToolRegistry.kt`
- `AdvancedToolRegistry.kt`
- `BatteryTools.kt`
- `OrderTools.kt`

### 5. **Storage Layer**
- **Model File**: Quantized .pte model (~500MB-2GB)
- **Chat History**: Encrypted conversation logs
- **User Preferences**: Settings and personalization

**Key Files:**
- `SecureStorage.kt`
- `chat_history.json` (encrypted)
- `user_prefs.json`

## Performance Optimization Stack

```mermaid
graph TD
    A[Llama 3.2 1B/3B Model] --> B[Quantization<br/>8-bit activation, 4-bit weights]
    B --> C[ExecuTorch Export<br/>.pte format]
    C --> D[XNNPACK Backend<br/>Extended operations]
    D --> E[KleidiAI Kernels<br/>i8mm optimization]
    E --> F[ARM CPU Execution<br/>Neoverse/Cortex]
    
    G[Memory Optimization] --> H[KV Cache]
    G --> I[Embedding Quantization]
    G --> J[Group-wise Quantization]
    
    H --> F
    I --> F
    J --> F
    
    style E fill:#ff6b6b
    style F fill:#ffd93d
    style B fill:#6bcf7f
```

## Memory Layout

```
┌─────────────────────────────────────────┐
│         Android App Memory              │
├─────────────────────────────────────────┤
│  UI & App Logic          ~50-100 MB     │
├─────────────────────────────────────────┤
│  Model Weights           ~500-1500 MB   │
│  (Quantized 4-bit)                      │
├─────────────────────────────────────────┤
│  KV Cache                ~100-200 MB    │
│  (Dynamic, grows with context)          │
├─────────────────────────────────────────┤
│  Activation Buffers      ~50-100 MB     │
│  (Temporary during inference)           │
├─────────────────────────────────────────┤
│  Chat History            ~5-10 MB       │
├─────────────────────────────────────────┤
│  System Overhead         ~100-200 MB    │
└─────────────────────────────────────────┘
Total: ~800-2000 MB (depending on model size)
```

## Inference Pipeline

```mermaid
flowchart TD
    Start([User Input]) --> A[Tokenization]
    A --> B{First Pass?}
    B -->|Yes| C[Encode Prompt]
    B -->|No| D[Use KV Cache]
    C --> E[Matrix Multiplication<br/>via KleidiAI]
    D --> E
    E --> F[Attention Mechanism<br/>SDPA]
    F --> G[Feed Forward Network]
    G --> H[Output Projection]
    H --> I{Generate More?}
    I -->|Yes| J[Update KV Cache]
    J --> D
    I -->|No| K[Detokenization]
    K --> L{Contains ACTION?}
    L -->|Yes| M[Execute Tool]
    M --> N[Second Pass with Results]
    N --> A
    L -->|No| End([Return Response])
    
    style E fill:#ff6b6b
    style F fill:#4ecdc4
    style M fill:#95e1d3
```

## Deployment Architecture

```mermaid
graph TB
    subgraph "Development"
        Dev[Developer Machine]
        Python[Python Environment]
        Export[Model Export Script]
    end
    
    subgraph "Build"
        Gradle[Gradle Build]
        NDK[Android NDK]
        CMake[CMake]
    end
    
    subgraph "Distribution"
        CDN[CDN<br/>Model Hosting]
        PlayStore[Google Play Store<br/>APK/AAB]
    end
    
    subgraph "Device"
        Download[Model Download]
        App[Android App]
        Inference[On-Device Inference]
    end
    
    Dev --> Python
    Python --> Export
    Export -->|.pte file| CDN
    Export --> Gradle
    Gradle --> NDK
    NDK --> CMake
    CMake --> PlayStore
    PlayStore --> App
    CDN --> Download
    Download --> App
    App --> Inference
    
    style CDN fill:#4ecdc4
    style Inference fill:#ff6b6b
```

## Security Architecture

```mermaid
flowchart LR
    subgraph "User Data"
        Input[User Input]
        History[Chat History]
    end
    
    subgraph "Processing"
        OnDevice[On-Device Processing<br/>No Cloud]
        Encryption[AES-256 Encryption]
    end
    
    subgraph "Storage"
        Encrypted[Encrypted Storage]
        Keystore[Android Keystore]
    end
    
    Input --> OnDevice
    OnDevice --> Encryption
    Encryption --> Encrypted
    Keystore -.->|Keys| Encryption
    History --> Encryption
    
    style OnDevice fill:#6bcf7f
    style Encryption fill:#ff6b6b
    style Keystore fill:#ffd93d
```

## Key Design Decisions

### 1. **Why ExecuTorch?**
- Optimized for mobile/edge devices
- Small binary size (~2MB)
- Supports quantization out-of-the-box
- Active development by Meta/PyTorch team

### 2. **Why KleidiAI?**
- 2-3x performance improvement on Arm CPUs
- Leverages hardware features (i8mm)
- Optimized for quantized models
- Low power consumption

### 3. **Why On-Device?**
- Privacy: No data leaves the device
- Offline: Works without internet
- Latency: No network round-trip
- Cost: No API fees

### 4. **Why Agentic Architecture?**
- Autonomous: Can perform actions
- Contextual: Understands user intent
- Extensible: Easy to add new tools
- Intelligent: Multi-step reasoning

## Performance Characteristics

| Metric | Value | Notes |
|--------|-------|-------|
| **Model Size** | 500MB - 1.5GB | Depends on Llama variant |
| **First Token Latency** | 500-1000ms | With KleidiAI |
| **Tokens/Second** | 30-40 tok/s | On modern Arm devices |
| **Memory Usage** | 800MB - 2GB | Peak during inference |
| **Battery Drain** | ~3-5% per 10 msgs | Typical usage |
| **Cold Start** | 2-5 seconds | Model loading time |

## Summary

This architecture provides:
- **Scalable**: Easy to add new tools and capabilities
- **Performant**: Optimized with KleidiAI for Arm
- **Private**: All processing on-device
- **Intelligent**: True agentic behavior with multi-step reasoning
- **Production-Ready**: Robust error handling and fallbacks

Understanding this architecture will help you customize and extend the chatbot for your specific use case.
