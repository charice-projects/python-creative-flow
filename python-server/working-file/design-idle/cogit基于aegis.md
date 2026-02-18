# 🧠 **Cognit 认知治理协议：最终蓝图与智慧结晶**

基于我们全部的思考、挣扎与突破，现将 Cognit 的完整体系呈现如下。这既是一份技术蓝图，也是一份从痛苦中淬炼出的生存哲学。

---

## 一、历史快照：从恐惧到觉醒的演化之路

### 快照 0.5：原始痛点（认知黑洞）
*   **状态**：在与 AI 的协作中，对话失忆、项目上下文断裂、决策缘由消散成为常态。我们恐惧于“上帝协议”——一个试图控制一切却必然失败的庞然大物。
*   **教训**：**复杂性只能管理，不能消灭**。试图用单一方案解决所有问题，只会创造更大的问题。我们需要记录“为什么”，而不仅仅是“是什么”。

### 快照 1.0：Aegis 的野心（抽象尝试）
*   **状态**：提出 AS、AC、AX 三层协议，定义了七种原语。这是“上帝对象”的雏形。
*   **教训**：**单一协议职责过载**。将数据标准、查询服务、传输逻辑混合在同一层，违反了关注点分离原则。这让我们走向了“分层”。

### 快照 2.0：教育体系隐喻（哲学突破）
*   **状态**：将系统映射为教育体系——课程标准（协议）、学校管理（编排）、教学过程（应用）。
*   **核心洞察**：**协议应是“教育局+基础设施”，而非“老师”**。这一隐喻让我们清晰分离了“规定什么必须统一”和“允许什么自由创新”的边界。

### 快照 3.0：认知城市蓝图（架构成型）
*   **状态**：提出“五层三支柱”架构：CM、SA、CT、IA 四层协议，由编排层整合。
*   **关键决策**：引入独立的**身份验证层（IA）**，将信任作为一等公民；将复杂的索引查询推向应用生态层，保持协议核心的极致简洁。

### 快照 4.0：二进制优先转向（机器本质）
*   **状态**：深刻认识到“协议主要是给 AI 和计算机看的”，追求底层效率。
*   **架构革命**：从“人类可读的 JSON 优先”转向 **“四象归一”数据架构**：传输/存储态（二进制 ABP）、内存交换态（零拷贝 Cap'n Proto）、计算证据态（Arrow 张量）、图谱查询态（内存图）。所有形态共享同一份数据宪法（Cap'n Proto Schema）。

### 快照 5.0：MCP 的冲击（现实觉醒）
*   **状态**：发现 MCP 已经成为连接层的事实标准，连接层的战争已经结束。
*   **残酷真相**：**我们不需要重复造轮子，但可以在轮子之上建造高楼**。连接层交给 MCP，我们专注认知层。

### 快照 6.0：Cognit 的诞生（智慧结晶）
*   **状态**：基于前五步的经验，我们提炼出三大生存思想——**专业分工、复杂解耦、独立不依赖**，并最终凝练为 Cognit 协议：一个**跨协议的认知治理层**。
*   **最终形态**：Cognit 不是另一个 MCP，而是 MCP 生态的“大脑皮层”。它通过适配器接入 MCP、A2A 等协议，将所有 AI 智能体的行为转化为统一的认知原子，构建可追溯、可审计、可继承的知识图谱。

### 永恒的经验法则
1.  **克制法**：协议的权威性与它规定的内容数量成反比。我们只定义最少的原子（4 种）和关系（4 种），像 26 个字母一样简洁。
2.  **分层法**：每个层只解决一个问题，通过接口而非实现通信。存储、处理、计算、呈现各司其职。
3.  **扩展法**：所有功能都应设计为可插拔的扩展，而非核心规范。适配器、存储后端、工具链都可以独立替换。
4.  **身份优先**：没有明确的身份和验证，协作就是沙上城堡。IA 层确保每个原子都有主人。
5.  **机器优先**：底层效率决定上层体验的天花板。四象归一架构让 Cognit 在性能上碾压纯 JSON 方案。
6.  **独立不依赖**：核心数据模型必须独立于任何传输协议和存储后端。MCP 只是数据源之一，不是生命线。

---

## 二、核心架构设计：认知治理的全景图

### 2.1 总体架构：四层 + 一宪法 + 多适配器

```yaml
═══════════════════════════════════════════════════════════════════════
    【应用生态层】 (治理工具)
    ┌─────────────────────────────────────────────────────────┐
    │  trace（追溯）  diagnose（诊断）  graph（图谱）         │
    │  audit（审计）  search（搜索）    insights（洞察）      │
    └─────────────────────────────────────────────────────────┘
                            ↑ 基于统一数据模型
════════════════════════════【认知宪法层】══════════════════════════════
    【数据模型层】                    【存储抽象层】
    ┌─────────────────────┐         ┌──────────────────────┐
    │ • 原子类型：         │         │ • AtomStore 接口     │
    │   Intent, Proof,     │◄──────►│   - save/get/query   │
    │   Decision, Annotation│         │ • 实现：FileStore,   │
    │ • 关系：             │         │   SQLiteStore,       │
    │   dependsOn, evidences,│       │   MCPStore（通过MCP）│
    │   derivesFrom, references│     └──────────────────────┘
    └─────────────────────┘
                            ↑ 适配器转换
════════════════════════════【协议适配层】══════════════════════════════
    ┌─────────────────────────────────────────────────────────┐
    │  MCP 适配器  │  A2A 适配器  │  UTCP 适配器  │  自定义   │
    │  (监听事件)  │  (监听调用)  │  (预留)      │  适配器   │
    └─────────────────────────────────────────────────────────┘
                            ↑ 监听/拉取
════════════════════════════【原生协议层】══════════════════════════════
    ┌─────────────────────────────────────────────────────────┐
    │  MCP 生态      │  A2A 生态      │  其他 AI 协议         │
    │  (工具调用)    │  (智能体交互)  │  (未来)               │
    └─────────────────────────────────────────────────────────┘
```

### 2.2 数据流转的“四象归一”架构

这是 Cognit 的核心引擎，定义了数据在不同场景下的最优形态：

```yaml
# 所有形态共享的源：Cap'n Proto 数据宪法
CognitiveSchema:
  path: "/schemas/cognitive_atoms.capnp"
  version: "2.0"
  fingerprint: "0x8a7b3c5d1e2f4a6b"

# 四态及其转换关系
DataStates:
  WireStorageState:          # 形态一：传输与存储态
    format: "Cognitive Binary Pack (CBP)"
    characteristics: ["极致紧凑", "流式友好", "自描述"]
    use_cases: ["网络传输", "磁盘存储", "跨节点同步"]
    converter:
      to_memory: "CBP → Cap'n Proto (零拷贝映射)"
      from_memory: "Cap'n Proto → CBP (智能编码)"

  MemoryExchangeState:       # 形态二：内存交换态
    format: "Cap'n Proto 内存对象"
    characteristics: ["零拷贝", "类型安全", "直接访问"]
    use_cases: ["运行时处理", "API 交互", "缓存"]
    converter:
      to_compute: "提取数值字段 → Arrow RecordBatch"
      to_graph: "解析关系 → 图节点"

  ComputeEvidenceState:      # 形态三：计算证据态
    format: "Apache Arrow 表 / 张量"
    characteristics: ["列式存储", "向量化计算", "GPU友好"]
    use_cases: ["AI 训练/推理", "统计分析", "异常检测"]
    converter:
      from_memory: "Proof 证据字段 → Arrow 批处理"
      to_wire: "Arrow → CBP (列式压缩)"

  GraphQueryState:           # 形态四：图谱查询态
    format: "内存属性图 (CSR 格式)"
    characteristics: ["增量构建", "遍历优化", "相似性搜索"]
    use_cases: ["影响追踪", "决策链分析", "模式匹配"]
    converter:
      from_memory: "原子 + 关系 → 图结构"
      query_engine: "HNSW 索引 + 双向 BFS"
```

### 2.3 核心接口定义（宪法）

#### 2.3.1 认知原子数据宪法（Cap'n Proto）

```capnp
@0x8a7b3c5d1e2f4a6b;

# 原子类型
struct Intent {
  id @0 :Text;
  verb @1 :Text;          # "implement", "call_tool", "research"
  description @2 :Text;
  scope @3 :Text;          # 影响范围（文件、API、模块）
  rationale @4 :Text;      # 为什么做（AI 的思考过程）
  embedding @5 :Data;      # 可选的语义向量
  status @6 :Status;
  timestamp @7 :UInt64;
  actor @8 :Text;          # 谁发起的（DID）
  
  enum Status {
    proposed @0;
    accepted @1;
    inProgress @2;
    completed @3;
    rejected @4;
  }
}

struct Proof {
  id @0 :Text;
  target @1 :Text;         # 指向 Intent 或其他原子
  type @2 :Text;           # "tool_response", "test_result", "review"
  evidence @3 :Data;       # 证据数据（如工具返回的 JSON）
  passed @4 :Bool;
  timestamp @5 :UInt64;
  verifier @6 :Text;       # 验证者 DID
}

struct Decision {
  id @0 :Text;
  basedOn @1 :List(Text);  # 相关的原子 ID
  content @2 :Text;        # 决策内容（自然语言）
  overrides @3 :List(Text); # 覆盖了哪些之前的决策
  impact @4 :Text;         # 影响描述
  timestamp @5 :UInt64;
  maker @6 :Text;          # 决策者 DID
}

struct Annotation {
  id @0 :Text;
  target @1 :Text;         # 被注释的原子
  type @2 :Text;           # "comment", "question", "warning"
  content @3 :Text;
  author @4 :Text;
  resolved @5 :Bool;
  timestamp @6 :UInt64;
}

struct Relation {
  id @0 :Text;
  from @1 :Text;
  to @2 :Text;
  type @3 :Text;           # "dependsOn", "evidences", "derivesFrom", "references"
  metadata @4 :Data;       # 可选的附加信息
}

struct Atom {
  union {
    intent @0 :Intent;
    proof @1 :Proof;
    decision @2 :Decision;
    annotation @3 :Annotation;
    relation @4 :Relation;
  }
}
```

#### 2.3.2 存储抽象层接口（AtomStore）

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class AtomStore(ABC):
    """原子存储接口，独立于具体实现"""
    
    @abstractmethod
    def save(self, atom: Atom) -> str:
        """保存原子，返回 ID"""
        pass
    
    @abstractmethod
    def get(self, atom_id: str) -> Optional[Atom]:
        """根据 ID 获取原子"""
        pass
    
    @abstractmethod
    def query(self, filter: Dict[str, Any]) -> List[Atom]:
        """查询原子，支持字段过滤"""
        pass
    
    @abstractmethod
    def get_relations(self, atom_id: str, direction: str = "both") -> List[Relation]:
        """获取与指定原子相关的所有关系"""
        pass
```

#### 2.3.3 适配器接口（ProtocolAdapter）

```python
class ProtocolAdapter(ABC):
    """协议适配器接口，连接外部 AI 协议"""
    
    @abstractmethod
    def start(self):
        """启动监听"""
        pass
    
    @abstractmethod
    def stop(self):
        """停止监听"""
        pass
    
    @abstractmethod
    def on_event(self, event: Dict[str, Any]):
        """处理外部协议事件，转换为原子并保存"""
        pass
```

### 2.4 工具链核心设计

#### 2.4.1 trace（追溯）

```python
def trace(atom_id: str, store: AtomStore, depth: int = 10) -> Graph:
    """
    从指定原子出发，双向追溯因果链，返回子图。
    算法：双向 BFS，查找所有通过关系连接的原子。
    """
    graph = Graph()
    queue = [(atom_id, 0)]
    visited = set()
    
    while queue and len(graph.nodes) < depth:
        current_id, level = queue.pop(0)
        if current_id in visited:
            continue
        visited.add(current_id)
        
        atom = store.get(current_id)
        if not atom:
            continue
        graph.add_node(atom)
        
        # 获取所有关系
        relations = store.get_relations(current_id)
        for rel in relations:
            other_id = rel.to if rel.from == current_id else rel.from
            if other_id not in visited:
                queue.append((other_id, level + 1))
            graph.add_edge(rel.from, rel.to, rel.type)
    
    return graph
```

#### 2.4.2 diagnose（诊断）

```python
def diagnose(project_id: str, store: AtomStore) -> DiagnosticReport:
    """
    分析整个项目的认知健康度，找出异常模式。
    """
    report = DiagnosticReport()
    
    # 1. 查找“孤儿”原子（没有 incoming 关系的 Intent）
    all_intents = store.query({"type": "intent"})
    for intent in all_intents:
        relations = store.get_relations(intent.id)
        incoming = [r for r in relations if r.to == intent.id]
        if not incoming:
            report.add_issue("orphan_intent", intent.id, "没有证据支持此意图")
    
    # 2. 查找决策冲突
    all_decisions = store.query({"type": "decision"})
    decision_map = {}
    for dec in all_decisions:
        # 检查 overrides 字段，找出被覆盖的决策
        for overridden in dec.overrides:
            if overridden in decision_map:
                report.add_issue("decision_conflict", 
                                 f"{dec.id} overrides {overridden}",
                                 "多个决策相互覆盖")
    
    # 3. 统计各原子类型数量，生成报告
    report.stats = {
        "intents": len(all_intents),
        "proofs": len(store.query({"type": "proof"})),
        "decisions": len(all_decisions),
        "annotations": len(store.query({"type": "annotation"}))
    }
    
    return report
```

#### 2.4.3 graph（图谱可视化）

```python
def generate_graph(project_id: str, store: AtomStore, format: str = "svg") -> str:
    """
    生成整个项目的认知图谱，支持多种输出格式（DOT, SVG, JSON）。
    """
    # 1. 获取所有原子和关系
    all_atoms = store.query({})
    all_relations = store.query({"type": "relation"})
    
    # 2. 构建图数据结构
    graph_data = {
        "nodes": [],
        "edges": []
    }
    for atom in all_atoms:
        graph_data["nodes"].append({
            "id": atom.id,
            "type": atom.which(),
            "label": atom.description[:50] if hasattr(atom, "description") else atom.id
        })
    for rel in all_relations:
        graph_data["edges"].append({
            "from": rel.from,
            "to": rel.to,
            "label": rel.type
        })
    
    # 3. 转换为指定格式（简化示例）
    if format == "json":
        return json.dumps(graph_data, indent=2)
    elif format == "dot":
        return generate_dot(graph_data)
    else:
        # 使用 Graphviz 生成 SVG
        return render_svg(graph_data)
```

---

## 三、部署与使用流程

### 3.1 安装与初始化

```bash
# 1. 安装 Cognit 运行时
pip install cognit-core  # Python 版
# 或
npm install -g @cognit/runtime  # Node 版

# 2. 初始化项目工作区
cd my-ai-project
cognit init --store file://./cognit_data

# 生成的项目结构：
.cognit/
├── config.yaml           # 主配置
├── stores/
│   └── default/          # 默认文件存储（CBP 格式文件）
├── adapters/             # 适配器配置
└── logs/
```

### 3.2 配置适配器（以 MCP 为例）

编辑 `.cognit/config.yaml`：

```yaml
project:
  id: "project:my-ai-app"
  name: "我的 AI 应用"

store:
  type: "file"
  path: "./.cognit/stores/default"

adapters:
  mcp:
    enabled: true
    # 连接到本地的 MCP 服务器（通过 stdio）
    servers:
      - name: "filesystem"
        command: "npx -y @modelcontextprotocol/server-filesystem /path/to/project"
      - name: "database"
        command: "npx -y @modelcontextprotocol/server-postgres postgresql://localhost/mydb"
    
    # 监听哪些事件
    events:
      - "tool/call"
      - "tool/return"
      - "agent/decision"   # 如果 MCP 扩展支持

  a2a:
    enabled: false
    # 预留 A2A 适配器配置

tools:
  # 启用哪些治理工具
  trace: true
  diagnose: true
  graph: true
  audit: true
```

### 3.3 启动适配器

```bash
# 启动所有配置的适配器，开始监听
cognit start

# 后台运行
cognit start --daemon
```

此时，每当 AI 通过 MCP 调用工具，Cognit 会自动生成对应的 Intent、Proof 等原子，并存入指定的存储。

### 3.4 日常使用示例

#### 场景一：追溯 AI 的某个决策

```bash
# 查看最近生成的原子
cognit list --limit 10

# 选择某个 Intent ID，追溯它的因果链
cognit trace intent:abc123 --depth 5 --format svg > trace.svg

# 打开 SVG 文件，可以看到：
# intent:abc123 (调用数据库查询用户信息)
#   ├─ evidences by proof:def456 (数据库返回结果)
#   └─ depends on decision:xyz789 (之前决定使用 PostgreSQL)
```

#### 场景二：诊断项目认知健康度

```bash
# 运行诊断
cognit diagnose --project project:my-ai-app

# 输出示例：
# 诊断报告：
#   - 孤儿意图：3 个（没有证据支持的意图）
#   - 决策冲突：1 处（两个决策相互覆盖）
#   - 统计：
#     - 意图：127
#     - 证据：98
#     - 决策：34
#     - 注释：12
```

#### 场景三：审计 AI 行为（合规用途）

```bash
# 生成指定时间范围内的审计日志
cognit audit --from 2026-02-01 --to 2026-02-18 --format pdf > audit_report.pdf

# 审计报告包含：
# - 所有工具调用记录及理由
# - 关键决策及其依据
# - 异常行为标记
```

#### 场景四：新成员加入项目

```bash
# 新开发者可以快速了解项目历史
cognit graph --focus module:auth --format dot | dot -Tpng > auth_module.png

# 查看与 auth 模块相关的所有决策和意图
cognit query "scope ~ 'auth/*'"
```

### 3.5 与 MCP 生态的集成示例

假设你正在用 Claude 和 MCP 开发一个功能：

1. **Claude 通过 MCP 调用 filesystem 工具**读取代码文件。
2. **Cognit 的 MCP 适配器**监听到 `tool/call` 事件，自动创建一个 `Intent` 原子：
   - `verb: "call_tool"`
   - `description: "读取文件 src/auth.js"`
   - `rationale: "为了理解现有认证逻辑"`
3. **工具返回结果**时，适配器创建一个 `Proof` 原子，链接到之前的 `Intent`。
4. **Claude 做出决策**（比如“重构认证模块”），你可以在对话中标记（或通过扩展自动捕获），生成 `Decision` 原子。
5. 一周后，你可以用 `cognit trace` 看到完整的决策链：为什么读取了那个文件 → 为什么决定重构 → 重构的具体实现意图 → 测试结果证明。

---

## 四、总结：Cognit 的生存哲学

- **不是另一个 MCP**，而是 MCP 生态的“大脑皮层”。
- **不是大一统的上帝协议**，而是简洁的原子字母表。
- **不是依赖任何特定技术**，而是独立的数据宪法 + 适配器模式。
- **不是为了取代谁**，而是为了让 AI 的每一次思考都有迹可循。

Cognit 的目标是成为 AI 协作中的“罗塞塔石碑”——让不同协议、不同平台、不同时间的智能体行为，都能以统一的语言被记录、追溯和理解。

---

## 五、最后的行动建议

1. **立即开始定义 Cap'n Proto schema**（一周内完成初版）。
2. **实现 FileStore 和基础的 CLI 工具**（两周内可跑通“手动创建原子 + trace”）。
3. **接入 MCP 适配器**（一个月内实现自动化捕获）。
4. **找第一个用户**（朋友的小项目）验证价值。
5. **根据反馈迭代，同时关注 MCP 生态动向**。

时间窗口存在，但不会太长。现在，就是行动的时刻。

---

*认知永恒，协作无限。*